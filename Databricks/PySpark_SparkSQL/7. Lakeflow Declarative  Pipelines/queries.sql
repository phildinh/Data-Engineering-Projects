--landing
select * from delta.`/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_temperature/`;
select * from delta.`/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_tilt/`;
select * from delta.`/Volumes/bridge_monitoring/00_landing/data_sources/streaming/bridge_vibration/`;

--bronze
select * from bridge_monitoring.`01_bronze`.bridge_temperature order by event_time desc;
select * from bridge_monitoring.`01_bronze`.bridge_tilt order by event_time desc;
select * from bridge_monitoring.`01_bronze`.bridge_vibration order by event_time desc;

--silver
select * from bridge_monitoring.`02_silver`.bridge_temperature order by event_time desc;
select * from bridge_monitoring.`02_silver`.bridge_tilt order by event_time desc;
select * from bridge_monitoring.`02_silver`.bridge_vibration order by event_time desc;

--gold
select * from bridge_monitoring.`03_gold`.bridge_metrics order by window_start desc;