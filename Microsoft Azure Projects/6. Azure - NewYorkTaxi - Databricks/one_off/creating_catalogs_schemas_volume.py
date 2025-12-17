# Databricks notebook source
# Creating the catalog
# Please update the managed location path
spark.sql("create catalog if not exists nyctaxi")

# COMMAND ----------

# Creating the schemas
spark.sql("create schema if not exists nyctaxi.00_landing")
spark.sql("create schema if not exists nyctaxi.01_bronze")
spark.sql("create schema if not exists nyctaxi.02_silver")
spark.sql("create schema if not exists nyctaxi.03_gold")

# COMMAND ----------

# Creating the volume
spark.sql("create volume if not exists nyctaxi.00_landing.data_sources")