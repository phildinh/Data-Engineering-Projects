CREATE TABLE [Sales].[Fact_Sales] (

	[CustomerID] varchar(255) NOT NULL, 
	[ItemID] varchar(255) NOT NULL, 
	[SalesOrderNumber] varchar(30) NULL, 
	[SalesOrderLineNumber] int NULL, 
	[OrderDate] date NULL, 
	[Quantity] int NULL, 
	[TaxAmount] float NULL, 
	[UnitPrice] float NULL
);