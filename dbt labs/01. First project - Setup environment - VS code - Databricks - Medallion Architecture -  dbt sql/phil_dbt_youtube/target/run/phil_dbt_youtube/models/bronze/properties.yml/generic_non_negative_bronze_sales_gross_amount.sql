
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  

SELECT
    *
FROM    
    `dbt_tutorial_dev`.`bronze`.`bronze_sales`
WHERE
    gross_amount < 0


  
  
      
    ) dbt_internal_test