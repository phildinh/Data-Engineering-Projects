# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Configure Structured Streaming batch size on Azure Databricks](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/batch-size)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Setting Max Files per Trigger 100

# COMMAND ----------

source_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.maxFilesPerTrigger", "100").\
    load(source_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Setting Max Bytes per Trigger 10 10GB

# COMMAND ----------

source_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    option("cloudFiles.maxBytesPerTrigger", "10g").\
    load(source_path)