
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    sales_id as unique_field,
    count(*) as n_records

from `dbt_tutorial_dev`.`bronze`.`bronze_sales`
where sales_id is not null
group by sales_id
having count(*) > 1



  
  
      
    ) dbt_internal_test