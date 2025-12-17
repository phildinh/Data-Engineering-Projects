# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: raw ingestion of three delta streams

# COMMAND ----------

import dlt

# Bronze: raw ingestion of three delta streams

@dlt.table(name="01_bronze.bridge_temperature", comment="Raw temperature readings")
def bronze_bridge_temperature():
    return (
        spark.readStream
             .format("delta")
             .load("/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_temperature")
    )

@dlt.table(name="01_bronze.bridge_vibration", comment="Raw vibration readings")
def bronze_bridge_vibration():
    return (
        spark.readStream
             .format("delta")
             .load("/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_vibration")
    )

@dlt.table(name="01_bronze.bridge_tilt", comment="Raw tilt angle readings")
def bronze_bridge_tilt():
    return (
        spark.readStream
             .format("delta")
             .load("/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_tilt")
    )