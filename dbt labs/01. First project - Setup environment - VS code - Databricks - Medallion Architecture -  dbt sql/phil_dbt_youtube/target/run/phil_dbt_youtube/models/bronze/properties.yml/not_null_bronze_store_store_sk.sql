
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select store_sk
from `dbt_tutorial_dev`.`bronze`.`bronze_store`
where store_sk is null



  
  
      
    ) dbt_internal_test