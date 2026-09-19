# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "da392e97-7867-4494-a3bf-7c1bdac8a24d",
# META       "default_lakehouse_name": "main_lakehouse",
# META       "default_lakehouse_workspace_id": "3eb4b063-99e1-40a7-b690-264006043c04",
# META       "known_lakehouses": [
# META         {
# META           "id": "da392e97-7867-4494-a3bf-7c1bdac8a24d"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df_customer = spark.read.format("csv").option("header","true").load("Files/bronze/customers.csv")
df_order = spark.read.format("csv").option("header","true").load("Files/bronze/orders.csv")
df_product = spark.read.format("csv").option("header","true").load("Files/bronze/products.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_customer.printSchema()
df_order.printSchema()
df_product.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import *

df_customer = df_customer.withColumn('customer_id', col('customer_id').cast('int'))

df_order = df_order.withColumns(
    {
        'order_id': col('order_id').cast('int'),
        'customer_id': col('customer_id').cast('int'),
        'product_id': col('product_id').cast('int'),
        'quantity': col('quantity').cast('int'),
        'order_date': col('order_date').cast('date'),
        'total_amount': col('total_amount').cast('float')
    }
)

df_product = df_product.withColumns(
    {
        'product_id': col('product_id').cast('int'),
        'price': col('price').cast('float')
    }
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("CREATE SCHEMA silver")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_customer.write.format("delta").mode("overwrite").saveAsTable("silver.customers")
df_order.write.format("delta").mode("overwrite").saveAsTable("silver.orders")
df_product.write.format("delta").mode("overwrite").saveAsTable("silver.products")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM main_lakehouse.silver.orders LIMIT 1000")
spark.sql("OPTIMIZE silver.orders")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("OPTIMIZE silver.orders ZORDER BY (quantity)")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
