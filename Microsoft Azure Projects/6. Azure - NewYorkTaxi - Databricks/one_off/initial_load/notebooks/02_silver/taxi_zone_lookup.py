# Databricks notebook source
from pyspark.sql.functions import current_timestamp, lit, col
from pyspark.sql.types import TimestampType, IntegerType

# COMMAND ----------

# Read the taxi zone lookup CSV (with header) into a DataFrame
df = spark.read.format("csv").option("header", True).load("/Volumes/nyctaxi/00_landing/data_sources/lookup/taxi_zone_lookup.csv")

# COMMAND ----------

# Select and rename fields, casting types, and add audit columns
df = df.select(
                col("LocationID").cast(IntegerType()).alias("location_id"),
                col("Borough").alias("borough"),
                col("Zone").alias("zone"),
                col("service_zone"),
                current_timestamp().alias("effective_date"),
                lit(None).cast(TimestampType()).alias("end_date")
            )

# COMMAND ----------

# Write to a Unity Catalog managed Delta table in the silver schema, overwriting any existing records
df.write.mode("overwrite").saveAsTable("nyctaxi.02_silver.taxi_zone_lookup")