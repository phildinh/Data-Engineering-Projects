# Databricks notebook source
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

# Read all Parquet files from the landing directory into a DataFrame
df = spark.read.format("parquet").load("/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/*")

# COMMAND ----------

# Add a column to capture when the data was processed
df = df.withColumn("processed_timestamp", current_timestamp())

# COMMAND ----------

# Write the DataFrame to a Unity Catalog managed Delta table in the bronze schema, overwriting any existing data
df.write.mode("overwrite").saveAsTable("nyctaxi.01_bronze.yellow_trips_raw")