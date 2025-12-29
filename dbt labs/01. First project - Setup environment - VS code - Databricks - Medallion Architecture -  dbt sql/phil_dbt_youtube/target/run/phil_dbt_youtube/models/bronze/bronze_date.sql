
  
  
  create or replace view `dbt_tutorial_dev`.`bronze`.`bronze_date`
  
  as (
    SELECT
    *
    FROM
        `dbt_tutorial_dev`.`source`.`dim_date`
  )
