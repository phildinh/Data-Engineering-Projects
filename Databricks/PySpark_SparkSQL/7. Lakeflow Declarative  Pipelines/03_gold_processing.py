# Databricks notebook source
# MAGIC %md
# MAGIC # Gold: 10-minute windowed metrics combining silver aggregates

# COMMAND ----------

import dlt
from pyspark.sql.functions import col, window, max, avg, round


@dlt.table(
    name="03_gold.bridge_metrics",
    comment="10-min avg temperature, max vibration & max tilt per bridge with window start/end"
)
def bridge_metrics():
    # Apply a 2-minute watermark to bound late data for stateful ops
    temp = (
      dlt.read_stream("02_silver.bridge_temperature")
         .withWatermark("event_time", "2 minutes")
    )
    vib = (
      dlt.read_stream("02_silver.bridge_vibration")
         .withWatermark("event_time", "2 minutes")
    )
    tilt = (
      dlt.read_stream("02_silver.bridge_tilt")
         .withWatermark("event_time", "2 minutes")
    )

    # Compute 10-minute tumbling average temperature, retaining metadata
    temp_agg = (
      temp
        .groupBy(
          window("event_time", "10 minutes"),
          col("bridge_id"),
          col("name"),
          col("location")
        )
        .agg(
          avg("temperature").alias("avg_temperature")
        )
        .select(
          col("bridge_id"),
          col("name"),
          col("location"),
          col("window.start").alias("window_start"),
          col("window.end").alias("window_end"),
          col("avg_temperature")
        )
    )

    # Compute 10-minute max vibration per bridge
    vib_agg = (
      vib
        .groupBy(window("event_time", "10 minutes"), col("bridge_id"))
        .agg(
          max("vibration").alias("max_vibration")
        )
        .select(
          col("bridge_id"),
          col("window.start").alias("window_start"),
          col("window.end").alias("window_end"),
          col("max_vibration")
        )
    )

    # Compute 10-minute max tilt angle per bridge
    tilt_agg = (
      tilt
        .groupBy(window("event_time", "10 minutes"), col("bridge_id"))
        .agg(
          max("tilt_angle").alias("max_tilt_angle")
        )
        .select(
          col("bridge_id"),
          col("window.start").alias("window_start"),
          col("window.end").alias("window_end"),
          col("max_tilt_angle")
        )
    )

    # Join silver aggregates on bridge_id + window bounds
    return (
      temp_agg.alias("t")
        .join(
          vib_agg.alias("v"),
          on=["bridge_id", "window_start", "window_end"],
          how="inner"
        )
        .join(
          tilt_agg.alias("l"),
          on=["bridge_id", "window_start", "window_end"],
          how="inner"
        )
        .select(
          col("bridge_id"),
          col("name"),
          col("location"),
          col("window_start"),
          col("window_end"),
          round(col("avg_temperature"),2).alias("avg_temperature"),
          col("max_vibration"),
          col("max_tilt_angle")
        )
    )