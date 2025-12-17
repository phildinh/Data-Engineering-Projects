# Databricks notebook source
import sys
import os
# Go two levels up to reach the project root
project_root = os.path.abspath(os.path.join(os.getcwd(), "../.."))

if project_root not in sys.path:
    sys.path.append(project_root)

from pyspark.sql.functions import date_format

# COMMAND ----------

from datetime import date
from dateutil.relativedelta import relativedelta

# Get the first day of the month two months ago
two_months_ago_start = date.today().replace(day=1) - relativedelta(months=2)

# COMMAND ----------

# Read the 'yellow_trips_enriched' table from the 'nyctaxi.02_silver' schema
# and filter to only include trips with a pickup datetime
# later than the start date from two months ago

df = spark.read.table("nyctaxi.02_silver.yellow_trips_enriched").filter(f"tpep_pickup_datetime > '{two_months_ago_start}'")

# COMMAND ----------

# Add a year_month column, formated as yyyy-MM

df = df.withColumn("year_month", date_format("tpep_pickup_datetime", "yyyy-MM"))

# COMMAND ----------

# Write the yellow_trips data in JSON format to the External Table "yellow_trips_export"

df.write.\
    option("path", "abfss://nyctaxi@datastakeholder1.dfs.core.windows.net/yellow_trips_export/").\
    format("json").\
    mode("append").\
    partitionBy("vendor", "year_month").\
    saveAsTable("nyctaxi.04_export.yellow_trips_export")