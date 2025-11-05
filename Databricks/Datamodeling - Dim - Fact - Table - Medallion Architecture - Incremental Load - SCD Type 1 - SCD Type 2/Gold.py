# Databricks notebook source
# MAGIC %md
# MAGIC # Create Dim Customer

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.DimCustomers
# MAGIC AS
# MAGIC
# MAGIC SELECT *, 
# MAGIC   row_number() OVER (ORDER BY customer_id) as DimcustomerKey 
# MAGIC FROM 
# MAGIC (
# MAGIC    SELECT DISTINCT customer_id,
# MAGIC   customer_email,
# MAGIC   customer_name,
# MAGIC   customer_name_upper
# MAGIC FROM datamodeling.silver.silver_table
# MAGIC ) 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.DimCustomers

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Dim Products

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.DimProducts
# MAGIC AS
# MAGIC
# MAGIC SELECT *, 
# MAGIC   row_number() OVER (ORDER BY product_id) as DimproductKey 
# MAGIC FROM 
# MAGIC (
# MAGIC    SELECT DISTINCT product_id,
# MAGIC   product_name,
# MAGIC   product_category
# MAGIC
# MAGIC FROM datamodeling.silver.silver_table
# MAGIC ) 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.DimProducts

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Dim PAyments

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.DimPayments
# MAGIC AS
# MAGIC
# MAGIC SELECT *, 
# MAGIC   row_number() OVER (ORDER BY payment_type) as DimpaymentKey 
# MAGIC FROM 
# MAGIC (
# MAGIC    SELECT DISTINCT payment_type
# MAGIC
# MAGIC FROM datamodeling.silver.silver_table
# MAGIC ) 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.DimPayments

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Dim Region

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.DimRegion
# MAGIC AS
# MAGIC
# MAGIC SELECT *, 
# MAGIC   row_number() OVER (ORDER BY country) as DimRegionKey
# MAGIC FROM 
# MAGIC (
# MAGIC    SELECT DISTINCT country
# MAGIC
# MAGIC FROM datamodeling.silver.silver_table
# MAGIC ) 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.DimRegion

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Dim Sales

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.DimSales
# MAGIC AS
# MAGIC
# MAGIC SELECT
# MAGIC row_number() OVER (ORDER BY order_id) as DimSaleKey,
# MAGIC   order_id,
# MAGIC  order_date,
# MAGIC  customer_id,
# MAGIC  customer_name,
# MAGIC  customer_email,
# MAGIC  product_id,
# MAGIC  product_name,
# MAGIC  product_category,
# MAGIC  payment_type,
# MAGIC  country,
# MAGIC  last_update,
# MAGIC  Customer_Name_Upper,
# MAGIC  processDate
# MAGIC FROM
# MAGIC   datamodeling.silver.silver_table

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Fact Table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.gold.FactSales
# MAGIC AS
# MAGIC
# MAGIC SELECT
# MAGIC   S.DimSaleKey,
# MAGIC   C.DimCustomerKey,
# MAGIC   P.DimProductKey,
# MAGIC   PY.DimPaymentKey,
# MAGIC   R.DimRegionKey,
# MAGIC   F.quantity,
# MAGIC   F.unit_price
# MAGIC FROM
# MAGIC   datamodeling.silver.silver_table as F
# MAGIC LEFT JOIN datamodeling.gold.DimCustomers as C
# MAGIC ON F.customer_id = C.customer_id
# MAGIC LEFT JOIN datamodeling.gold.DimProducts as P
# MAGIC ON F.product_id = P.product_id
# MAGIC LEFT JOIN datamodeling.gold.DimPayments as PY
# MAGIC ON F.payment_type = PY.payment_type
# MAGIC LEFT JOIN datamodeling.gold.DimRegion as R
# MAGIC ON F.country = R.country
# MAGIC LEFT JOIN datamodeling.gold.DimSales AS S
# MAGIC ON F.order_id = S.order_id
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.factsales