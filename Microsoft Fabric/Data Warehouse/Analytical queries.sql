 -- customers by total sales for the year of 2021
 ------------------------------------------------
 SELECT c.CustomerName, SUM(s.UnitPrice * s.Quantity) AS TotalSales
 FROM Sales.Fact_Sales s
 JOIN Sales.Dim_Customer c
 ON s.CustomerID = c.CustomerID
 WHERE YEAR(s.OrderDate) = 2021
 GROUP BY c.CustomerName
 ORDER BY TotalSales DESC;

-- the top-seliing items by total sales for the year of 2021
 ------------------------------------------------
 SELECT i.ItemName, SUM(s.UnitPrice * s.Quantity) AS TotalSales
 FROM Sales.Fact_Sales s
 JOIN Sales.Dim_Item i
 ON s.ItemID = i.ItemID
 WHERE YEAR(s.OrderDate) = 2021
 GROUP BY i.ItemName
 ORDER BY TotalSales DESC;

-- the top customer for each of the categories: Bike, Helmet, and Gloves, based on their total sales
  WITH CategorizedSales AS (
 SELECT
     CASE
         WHEN i.ItemName LIKE '%Helmet%' THEN 'Helmet'
         WHEN i.ItemName LIKE '%Bike%' THEN 'Bike'
         WHEN i.ItemName LIKE '%Gloves%' THEN 'Gloves'
         ELSE 'Other'
     END AS Category,
     c.CustomerName,
     s.UnitPrice * s.Quantity AS Sales
 FROM Sales.Fact_Sales s
 JOIN Sales.Dim_Customer c
 ON s.CustomerID = c.CustomerID
 JOIN Sales.Dim_Item i
 ON s.ItemID = i.ItemID
 WHERE YEAR(s.OrderDate) = 2021
 ),
 RankedSales AS (
     SELECT
         Category,
         CustomerName,
         SUM(Sales) AS TotalSales,
         ROW_NUMBER() OVER (PARTITION BY Category ORDER BY SUM(Sales) DESC) AS SalesRank
     FROM CategorizedSales
     WHERE Category IN ('Helmet', 'Bike', 'Gloves')
     GROUP BY Category, CustomerName
 )
 SELECT Category, CustomerName, TotalSales
 FROM RankedSales
 WHERE SalesRank = 1
 ORDER BY TotalSales DESC;
