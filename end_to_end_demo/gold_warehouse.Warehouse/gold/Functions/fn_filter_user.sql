CREATE FUNCTION gold.fn_filter_user(@user_name AS VARCHAR(50))
    RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN 
    SELECT 1 AS result
    WHERE @user_name = USER_NAME()

GO