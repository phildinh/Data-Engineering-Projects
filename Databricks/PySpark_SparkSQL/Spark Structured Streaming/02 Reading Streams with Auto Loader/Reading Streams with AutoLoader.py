# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC
# MAGIC - [Structured Streaming Concepts](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts)
# MAGIC - [Structured Streaming Programming Guide](https://spark.apache.org/docs/3.5.1/structured-streaming-programming-guide.html)
# MAGIC - [What is Auto Loader?](https://learn.microsoft.com/en-us/azure/databricks/ingestion/cloud-object-storage/auto-loader/)
# MAGIC - [Schema Inference](https://learn.microsoft.com/en-gb/azure/databricks/ingestion/cloud-object-storage/auto-loader/schema)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading Streaming Data Files with Auto Loader

# COMMAND ----------

source_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    load(source_path)

# COMMAND ----------

df.display()