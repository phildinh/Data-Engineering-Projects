CREATE TABLE [Sales].[Dim_Item] (

	[ItemID] varchar(255) NOT NULL, 
	[ItemName] varchar(255) NOT NULL
);


GO
ALTER TABLE [Sales].[Dim_Item] ADD CONSTRAINT PK_Dim_Item primary key NONCLUSTERED ([ItemID]);