# Databricks notebook source
# MAGIC %md
# MAGIC # SCD type 1

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS datamodeling.default.scdtype1_source;
# MAGIC CREATE TABLE IF NOT EXISTS datamodeling.default.scdtype1_source
# MAGIC (
# MAGIC   pro_id INT,
# MAGIC   pro_name STRING,
# MAGIC   pro_cat STRING,
# MAGIC   processDate DATE
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO datamodeling.default.scdtype1_source
# MAGIC VALUES
# MAGIC (1,'Product1','Category1',current_date()),
# MAGIC (2,'Product2','Category2',current_date()),
# MAGIC (3,'Product3','newcatgory',current_date())
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.default.scdtype1_source

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS datamodeling.gold.scdtype1_table
# MAGIC (
# MAGIC   pro_id INT,
# MAGIC   pro_name STRING,
# MAGIC   pro_cat STRING,
# MAGIC   processDate DATE
# MAGIC )
# MAGIC

# COMMAND ----------

spark.sql("Select * from datamodeling.default.scdtype1_source").createOrReplaceTempView("src")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM src

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.gold.scdtype1_table AS trg
# MAGIC USING src
# MAGIC ON trg.pro_id = src.pro_id
# MAGIC WHEN MATCHED AND src.processDate >= trg.processDate THEN UPDATE SET *
# MAGIC WHEN NOT MATCHED THEN INSERT *

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.scdtype1_table

# COMMAND ----------

# MAGIC %md
# MAGIC # SCD Type 2
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS datamodeling.default.scdtype2_source;
# MAGIC CREATE TABLE IF NOT EXISTS datamodeling.default.scdtype2_source
# MAGIC (
# MAGIC   pro_id INT,
# MAGIC   pro_name STRING,
# MAGIC   pro_cat STRING,
# MAGIC   processDate DATE
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO datamodeling.default.scdtype2_source
# MAGIC VALUES
# MAGIC (1,'Product1','Category1',current_date()),
# MAGIC (2,'Product2','Category2',current_date()),
# MAGIC (3,'Product3','newcategory',current_date())

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS datamodeling.gold.scdtype2_table
# MAGIC (
# MAGIC   pro_id INT,
# MAGIC   pro_name STRING,
# MAGIC   pro_cat STRING,
# MAGIC   processDate DATE,
# MAGIC   start_date DATE,
# MAGIC   end_date DATE,
# MAGIC   is_current STRING
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *,
# MAGIC     current_timestamp() as start_date,
# MAGIC     CAST('3000-01-01' AS timestamp) as end_date,
# MAGIC     'Y' as is_current
# MAGIC FROM datamodeling.default.scdtype2_source

# COMMAND ----------

spark.sql(
    """
    SELECT *,
        current_timestamp() as start_date,
        CAST('3000-01-01' AS timestamp) as end_date,
        'Y' as is_current
    FROM datamodeling.default.scdtype2_source
    """
).createOrReplaceTempView("srctype2")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM srctype2

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.gold.scdtype2_table as trg
# MAGIC USING srctype2 
# MAGIC ON srctype2.pro_id = trg.pro_id
# MAGIC AND trg.is_current = 'Y'
# MAGIC
# MAGIC -- When we have New Data with Updates
# MAGIC WHEN MATCHED AND (
# MAGIC   srctype2.pro_cat <> trg.pro_cat OR
# MAGIC   srctype2.processDate <> trg.processDate OR
# MAGIC   srctype2.pro_name <> trg.pro_name
# MAGIC ) THEN
# MAGIC UPDATE SET
# MAGIC   trg.end_date = current_timestamp(),
# MAGIC   trg.is_current = 'N'
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO datamodeling.gold.scdtype2_table as trg
# MAGIC USING srctype2 
# MAGIC ON srctype2.pro_id = trg.pro_id
# MAGIC AND trg.is_current = 'Y'
# MAGIC
# MAGIC WHEN NOT MATCHED THEN INSERT(
# MAGIC   pro_id,
# MAGIC   pro_name,
# MAGIC   pro_cat,
# MAGIC   processDate,
# MAGIC   start_date,
# MAGIC   end_date,
# MAGIC   is_current
# MAGIC ) VALUES (
# MAGIC   srctype2.pro_id,
# MAGIC   srctype2.pro_name,
# MAGIC   srctype2.pro_cat,
# MAGIC   srctype2.processDate,
# MAGIC   srctype2.start_date,
# MAGIC   srctype2.end_date,
# MAGIC   srctype2.is_current
# MAGIC )
# MAGIC   

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM datamodeling.gold.scdtype2_table