
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select sales_id
from `dbt_tutorial_dev`.`bronze`.`bronze_sales`
where sales_id is null



  
  
      
    ) dbt_internal_test