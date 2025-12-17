# Databricks notebook source
import urllib.request
import shutil
import os

# COMMAND ----------

# List of year-month strings representing the data files to download
dates_to_process = ['2025-01', '2025-02', '2025-03', '2025-04', '2025-05', '2025-05','2025-06','2025-07','2025-08','2025-09']

for date in dates_to_process:
    # Construct the URL for the Parquet file corresponding to this month
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{date}.parquet"

    # Open a connection and stream the remote file
    response = urllib.request.urlopen(url)

    # Define and create the local directory for this date's data
    dir_path = f"/Volumes/nyctaxi/00_landing/data_sources/nyctaxi_yellow/{date}"
    os.makedirs(dir_path, exist_ok=True)

    # Define the full path for the downloaded file
    local_path = f"{dir_path}/yellow_tripdata_{date}.parquet"

    # Save the streamed content to the local file in binary mode
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(response, f)  # Copy data from response to file