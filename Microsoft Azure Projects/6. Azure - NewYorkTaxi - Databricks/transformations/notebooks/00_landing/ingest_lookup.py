# Databricks notebook source
import urllib.request
import os
import shutil

try:
    # Construct the URL for the Parquet file corresponding to this month
    url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

    # Open a connection and stream the remote file
    response = urllib.request.urlopen(url)

    # Define and create the local directory for this date's data
    dir_path = f"/Volumes/nyctaxi/00_landing/data_sources/lookup"
    os.makedirs(dir_path, exist_ok=True)

    # Define the full path for the downloaded file
    local_path = f"{dir_path}/taxi_zone_lookup.csv"

    # Save the streamed content to the local file in binary mode
    with open(local_path, 'wb') as f:
        shutil.copyfileobj(response, f)  # Copy data from response to file
    
    dbutils.jobs.taskValues.set(key="continue_downstream", value="yes")
    print("File succesfully uploaded")
except Exception as e:
    dbutils.jobs.taskValues.set(key="continue_downstream", value="no")
    print(f"File download failed: {str(e)}")