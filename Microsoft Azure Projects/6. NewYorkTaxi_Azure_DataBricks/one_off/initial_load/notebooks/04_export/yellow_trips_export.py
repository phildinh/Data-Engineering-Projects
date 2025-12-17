# Databricks notebook source
from pyspark.sql.functions import date_format

# COMMAND ----------

# Add a year_month column, formated as yyyy-MM
df = spark.read.table("nyctaxi.02_silver.yellow_trips_enriched")

df = df.withColumn("year_month", date_format("tpep_pickup_datetime", "yyyy-MM"))

# COMMAND ----------

# Write the yellow_trips data in JSON format to the External Table "yellow_trips_export"

df.write.\
    option("path", "abfss://nyctaxi@datastakeholder1.dfs.core.windows.net/yellow_trips_export/").\
    format("json").\
    mode("append").\
    partitionBy("vendor", "year_month").\
    saveAsTable("nyctaxi.04_export.yellow_trips_export")