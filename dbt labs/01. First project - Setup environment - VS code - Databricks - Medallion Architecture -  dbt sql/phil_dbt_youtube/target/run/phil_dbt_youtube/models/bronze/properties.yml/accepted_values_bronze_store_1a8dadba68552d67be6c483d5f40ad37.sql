
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

with all_values as (

    select
        store_name as value_field,
        count(*) as n_records

    from `dbt_tutorial_dev`.`bronze`.`bronze_store`
    group by store_name

)

select *
from all_values
where value_field not in (
    'Megamart Manhattan','Megamart Brooklyn','Megamart Austin','Megamart San Jose','Megamart Toronto'
)



  
  
      
    ) dbt_internal_test