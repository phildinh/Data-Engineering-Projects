CREATE   PROCEDURE Sales.LoadDataFromStaging (@OrderYear INT)
 AS
 BEGIN
 	-- Load data into the Customer dimension table
     INSERT INTO Sales.Dim_Customer (CustomerID, CustomerName, EmailAddress)
     SELECT DISTINCT CustomerName, CustomerName, EmailAddress
     FROM [Sales].[Staging_Sales]
     WHERE YEAR(OrderDate) = @OrderYear
     AND NOT EXISTS (
         SELECT 1
         FROM Sales.Dim_Customer
         WHERE Sales.Dim_Customer.CustomerName = Sales.Staging_Sales.CustomerName
         AND Sales.Dim_Customer.EmailAddress = Sales.Staging_Sales.EmailAddress
     );
        
     -- Load data into the Item dimension table
     INSERT INTO Sales.Dim_Item (ItemID, ItemName)
     SELECT DISTINCT Item, Item
     FROM [Sales].[Staging_Sales]
     WHERE YEAR(OrderDate) = @OrderYear
     AND NOT EXISTS (
         SELECT 1
         FROM Sales.Dim_Item
         WHERE Sales.Dim_Item.ItemName = Sales.Staging_Sales.Item
     );
        
     -- Load data into the Sales fact table
     INSERT INTO Sales.Fact_Sales (CustomerID, ItemID, SalesOrderNumber, SalesOrderLineNumber, OrderDate, Quantity, TaxAmount, UnitPrice)
     SELECT CustomerName, Item, SalesOrderNumber, CAST(SalesOrderLineNumber AS INT), CAST(OrderDate AS DATE), CAST(Quantity AS INT), CAST(TaxAmount AS FLOAT), CAST(UnitPrice AS FLOAT)
     FROM [Sales].[Staging_Sales]
     WHERE YEAR(OrderDate) = @OrderYear;
 END