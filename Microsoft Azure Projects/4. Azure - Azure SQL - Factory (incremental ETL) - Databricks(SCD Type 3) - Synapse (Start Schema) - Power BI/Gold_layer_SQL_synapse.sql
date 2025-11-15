CREATE SCHEMA gold;

CREATE VIEW gold.dim_branch
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/gold/dim_branch/',
        FORMAT = 'PARQUET'
    ) AS Quer1

CREATE VIEW gold.dim_model
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/gold/dim_model/',
        FORMAT = 'PARQUET'
    ) AS Quer2

CREATE VIEW gold.dim_dealer
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/gold/dim_dealer/',
        FORMAT = 'PARQUET'
    ) AS Quer3

CREATE VIEW gold.dim_date
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/gold/dim_date/',
        FORMAT = 'PARQUET'
    ) AS Quer4

CREATE VIEW gold.fact_sales
AS
SELECT
    *
FROM
    OPENROWSET
    (
        BULK 'https://azureprojectphil.blob.core.windows.net/gold/fact_sales/',
        FORMAT = 'PARQUET'
    ) AS Quer5