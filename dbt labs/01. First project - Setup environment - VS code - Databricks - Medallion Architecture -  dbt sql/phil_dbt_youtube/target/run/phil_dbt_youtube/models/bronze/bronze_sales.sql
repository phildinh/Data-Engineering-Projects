
  
  
  create or replace view `dbt_tutorial_dev`.`bronze`.`bronze_sales`
  
  as (
    SELECT
    *
    FROM
        `dbt_tutorial_dev`.`source`.`fact_sales`
  )
