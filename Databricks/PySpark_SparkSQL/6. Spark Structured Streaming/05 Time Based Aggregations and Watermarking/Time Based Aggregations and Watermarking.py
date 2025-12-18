# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Feature Deep Dive: Watermarking in Apache Spark Structured Streaming](https://www.databricks.com/blog/feature-deep-dive-watermarking-apache-spark-structured-streaming)
# MAGIC - [Apply watermarks to control data processing thresholds](https://learn.microsoft.com/en-gb/azure/databricks/structured-streaming/watermarks)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading a Stream

# COMMAND ----------

from pyspark.sql.functions import window, avg

from pyspark.sql.types import *

# COMMAND ----------

source_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

schema = StructType([
    StructField("event_id", StringType()),
    StructField("timestamp", TimestampType()),
    StructField("city", StringType()),
    StructField("temperature_c", DoubleType()),
    StructField("humidity_percent", IntegerType()),
    StructField("wind_speed_kmh", DoubleType())
])

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    schema(schema).\
    load(source_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Appying Time Based Aggregation and Watermarking to the Streaming DataFrame

# COMMAND ----------

df.withWatermark("timestamp", "30 seconds").\
    groupBy(
        window("timestamp", "60 seconds"),
        "city").\
    agg(
        avg("temperature_c"),
        avg("humidity_percent"),
        avg("wind_speed_kmh")
        ).display()