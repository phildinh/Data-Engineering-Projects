-- Databricks notebook source
CREATE CATALOG IF NOT EXISTS bridge_monitoring;
CREATE SCHEMA IF NOT EXISTS bridge_monitoring.00_landing;
CREATE SCHEMA IF NOT EXISTS bridge_monitoring.01_bronze;
CREATE SCHEMA IF NOT EXISTS bridge_monitoring.02_silver;
CREATE SCHEMA IF NOT EXISTS bridge_monitoring.03_gold;
CREATE VOLUME IF NOT EXISTS bridge_monitoring.00_landing.data_sources;
