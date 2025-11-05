# Databricks notebook source
spark.sql("""
SELECT *,
  upper(customer_name) as Customer_Name_Upper,
  date(current_timestamp()) as processDate
FROM datamodeling.bronze.bronze_table""").createOrReplaceTempView("silver_source")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM silver_source

# COMMAND ----------

# MAGIC %md
# MAGIC # MERGE Using Pyspark

# COMMAND ----------

if spark.catalog.tableExists('datamodeling.silver.silver_table'):
    pass

else:
    spark.sql("""
              CREATE TABLE IF NOT EXISTS datamodeling.silver.silver_table
              AS
              SELECT * FROM silver_source
              """)

# COMMAND ----------

# MAGIC %md
# MAGIC # MERGE Using SQL
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.silver.silver_table
# MAGIC USING silver_source
# MAGIC ON datamodeling.silver.silver_table.order_id = silver_source.order_id
# MAGIC WHEN MATCHED THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT*

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.silver.silver_table