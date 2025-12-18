# Databricks notebook source
# MAGIC %md
# MAGIC You can specify the trigger settings of a streaming query to define the timing of streaming data processing, whether the query is going to be executed as micro-batch query with a fixed batch interval or as a continuous processing query. Here are the different kinds of triggers that are supported.
# MAGIC
# MAGIC Trigger settings are applied to the **`writeStream`** part of your query, which controls how and when data is written to the sink.

# COMMAND ----------

# MAGIC %md
# MAGIC ### ProcessingTime trigger with 10-seconds micro-batch interval

# COMMAND ----------

sink_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/live_weather"

df.writeStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "parquet").\
    option("checkpointLocation", "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/checkpoints/_live_weather").\
    trigger(processingTime='10 seconds').\
    save(sink_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Available-now trigger

# COMMAND ----------

sink_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/live_weather"

df.writeStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "parquet").\
    option("checkpointLocation", "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/checkpoints/_live_weather").\
    trigger(availableNow=True).\
    save(sink_path)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Continuous Trigger

# COMMAND ----------

sink_path = "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/live_weather"

df.writeStream.\
    format("cloudFiles").\
    option("cloudFiles.format", "parquet").\
    option("checkpointLocation", "/Volumes/streaming_demo/weather_stream/weather_stream_volume/sink/checkpoints/_live_weather").\
    trigger(continuous='1 second').\
    save(sink_path)