# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Spark Streaming Programming Guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
# MAGIC - [Structured Streaming Concepts](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/concepts)
# MAGIC - [Structured Streaming Checkpoints](https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/checkpoints)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading a Stream

# COMMAND ----------

source_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/live_weather"

schema_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/source/schemas/_live_weather_schema"

df = spark.readStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "csv").\
    option("cloudFiles.schemaLocation", schema_location).\
    load(source_path)


df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Writing a Streaming DataFrame

# COMMAND ----------

sink_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/live_weather"

checkpoint_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/checkpoints/_live_weather"

df.writeStream.\
    format("parquet").\
    outputMode("append").\
    option("checkpointLocation", checkpoint_location ).\
    option("path", sink_path).\
    start()

# COMMAND ----------

spark.read.format("parquet").load(sink_path).display()