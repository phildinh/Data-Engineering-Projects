
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    store_sk as unique_field,
    count(*) as n_records

from `dbt_tutorial_dev`.`bronze`.`bronze_store`
where store_sk is not null
group by store_sk
having count(*) > 1



  
  
      
    ) dbt_internal_test