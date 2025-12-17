# Databricks notebook source
import urllib.request
import shutil
import os

# Target URL of the public csv file to download
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

# Open a connection and stream the remote file
response = urllib.request.urlopen(url)

# Create the destination directory for storing the downloaded Parquet file
dir_path = "/Volumes/nyctaxi/00_landing/data_sources/lookup"
os.makedirs(dir_path, exist_ok=True) 

# Define the full local path (including filename) where the file will be saved
local_path = f"{dir_path}/taxi_zone_lookup.csv"

# Write the contents of the response stream to the specified local file path
with open(local_path, 'wb') as f: 
    shutil.copyfileobj(response, f)