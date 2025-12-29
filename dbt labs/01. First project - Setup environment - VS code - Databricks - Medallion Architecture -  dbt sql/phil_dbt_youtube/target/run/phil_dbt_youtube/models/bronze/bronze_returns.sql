
  
    
        create or replace table `dbt_tutorial_dev`.`bronze`.`bronze_returns`
      
      
  using delta
      
      
      
      
      
      
      
      as
      SELECT
    *
    FROM
        `dbt_tutorial_dev`.`source`.`fact_returns`
  