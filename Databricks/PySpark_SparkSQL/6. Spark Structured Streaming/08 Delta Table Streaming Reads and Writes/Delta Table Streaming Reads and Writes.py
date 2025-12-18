# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [Delta table streaming reads and writes](https://learn.microsoft.com/en-gb/azure/databricks/structured-streaming/delta-lake)

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
# MAGIC ### 📌 Writing a Stream to a Delta Table

# COMMAND ----------

checkpoint_location = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/checkpoints/streaming_demo.weather_stream.weather_data"

df.writeStream.\
    outputMode("append").\
    option("checkpointLocation", checkpoint_location ).\
	toTable("streaming_demo.weather_stream.weather_data")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Reading a Stream from a Delta Table

# COMMAND ----------

spark.readStream.\
  table("streaming_demo.weather_stream.weather_data").\
  display()