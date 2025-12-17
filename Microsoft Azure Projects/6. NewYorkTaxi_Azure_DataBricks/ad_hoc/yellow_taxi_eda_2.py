# Databricks notebook source
from pyspark.sql.functions import date_format, count, sum

# COMMAND ----------

spark.read.table("nyctaxi.`01_bronze`.yellow_trips_raw").\
    groupBy(date_format("tpep_pickup_datetime", "yyyy-MM").alias("year_month")).\
    agg(count("*").alias("total_records")).\
    orderBy("year_month").display()

# COMMAND ----------

spark.read.table("nyctaxi.`02_silver`.yellow_trips_cleansed").\
    groupBy(date_format("tpep_pickup_datetime", "yyyy-MM").alias("year_month")).\
    agg(count("*").alias("total_records")).\
    orderBy("year_month").display()

# COMMAND ----------

spark.read.table("nyctaxi.`02_silver`.yellow_trips_enriched").\
    groupBy(date_format("tpep_pickup_datetime", "yyyy-MM").alias("year_month")).\
    agg(count("*").alias("total_records")).\
    orderBy("year_month").display()

# COMMAND ----------

spark.read.table("nyctaxi.`03_gold`.daily_trip_summary").\
    groupBy(date_format("pickup_date", "yyyy-MM").alias("year_month")).\
    agg(sum("total_trips").alias("total_records")).\
    orderBy("year_month").display()

# COMMAND ----------

spark.read.table("nyctaxi.`02_silver`.taxi_zone_lookup").display()