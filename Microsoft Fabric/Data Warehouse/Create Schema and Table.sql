```sql

 CREATE SCHEMA [Sales]
 GO
        
 IF OBJECT_ID('Sales.Fact_Sales', 'U') IS NULL
 	CREATE TABLE Sales.Fact_Sales (
 		CustomerID VARCHAR(255) NOT NULL,
 		ItemID VARCHAR(255) NOT NULL,
 		SalesOrderNumber VARCHAR(30),
 		SalesOrderLineNumber INT,
 		OrderDate DATE,
 		Quantity INT,
 		TaxAmount FLOAT,
 		UnitPrice FLOAT
 	);
    
 IF OBJECT_ID('Sales.Dim_Customer', 'U') IS NULL
     CREATE TABLE Sales.Dim_Customer (
         CustomerID VARCHAR(255) NOT NULL,
         CustomerName VARCHAR(255) NOT NULL,
         EmailAddress VARCHAR(255) NOT NULL
     );
        
 ALTER TABLE Sales.Dim_Customer add CONSTRAINT PK_Dim_Customer PRIMARY KEY NONCLUSTERED (CustomerID) NOT ENFORCED
 GO
    
 IF OBJECT_ID('Sales.Dim_Item', 'U') IS NULL
     CREATE TABLE Sales.Dim_Item (
         ItemID VARCHAR(255) NOT NULL,
         ItemName VARCHAR(255) NOT NULL
     );
        
 ALTER TABLE Sales.Dim_Item add CONSTRAINT PK_Dim_Item PRIMARY KEY NONCLUSTERED (ItemID) NOT ENFORCED
 GO

```
