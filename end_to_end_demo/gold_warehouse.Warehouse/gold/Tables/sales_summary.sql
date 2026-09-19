CREATE TABLE [gold].[sales_summary] (
    [Category]        VARCHAR (100)   NOT NULL,
    [Country]         VARCHAR (100)   NOT NULL,
    [TotalRevenue]    DECIMAL (18, 2) NOT NULL,
    [TotalQuantity]   INT             NOT NULL,
    [OrderCount]      INT             NOT NULL,
    [UniqueCustomers] INT             NOT NULL,
    [AvgOrderValue]   DECIMAL (18, 2) NOT NULL
);


GO