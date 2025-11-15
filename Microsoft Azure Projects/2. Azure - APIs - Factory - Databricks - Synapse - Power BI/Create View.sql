-- CREATE VIEW CALENDAR
CREATE VIEW gold.calendar
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Calendar/',
        FORMAT = 'PARQUET'
    ) AS QUER1

-- CREATE VIEW Customer
CREATE VIEW gold.customers
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Customers/',
        FORMAT = 'PARQUET'
    ) AS QUER2

-- CREATE VIEW Products
CREATE VIEW gold.Products
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Products/',
        FORMAT = 'PARQUET'
    ) AS QUER1

-- CREATE VIEW Returns
CREATE VIEW gold.Returns
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Returns/',
        FORMAT = 'PARQUET'
    ) AS QUER1

-- CREATE VIEW Sales
CREATE VIEW gold.Sales
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Sales/',
        FORMAT = 'PARQUET'
    ) AS QUER1

-- CREATE VIEW Subcategories
CREATE VIEW gold.Subcategories
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Subcategories/',
        FORMAT = 'PARQUET'
    ) AS QUER1

-- CREATE VIEW Territories
CREATE VIEW gold.Territories
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/silver/AdventureWorks_Territories/',
        FORMAT = 'PARQUET'
    ) AS QUER1