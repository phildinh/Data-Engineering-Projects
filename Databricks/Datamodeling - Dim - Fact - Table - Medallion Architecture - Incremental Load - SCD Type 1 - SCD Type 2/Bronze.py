# Databricks notebook source
if spark.catalog.tableExists('datamodeling.default.source_data'):
    last_load_date = spark.sql("""SELECT MAX(order_date) FROM datamodeling.default.source_data""").collect()[0][0]

else:
    last_load_date = '1000-01-01'

# COMMAND ----------

if spark.catalog.tableExists('datamodeling.bronze.bronze_table'):
    last_load_date = spark.sql("""SELECT MAX(order_date) FROM datamodeling.bronze.bronze_table""").collect()[0][0]

else:
    last_load_date = '1000-01-01'

# COMMAND ----------

last_load_date

# COMMAND ----------

spark.sql(f"""SELECT * FROM datamodeling.default.source_data 
          WHERE last_update > '{last_load_date}'""").createOrReplaceTempView("bronze_source")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronze_source

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE datamodeling.bronze.bronze_table
# MAGIC AS  
# MAGIC SELECT * FROM bronze_source