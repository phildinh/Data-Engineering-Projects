-- Databricks notebook source
CREATE CATALOG IF NOT EXISTS streaming_demo;
CREATE SCHEMA IF NOT EXISTS streaming_demo.weather_stream;
CREATE VOLUME streaming_demo.weather_stream.weather_stream_volume;