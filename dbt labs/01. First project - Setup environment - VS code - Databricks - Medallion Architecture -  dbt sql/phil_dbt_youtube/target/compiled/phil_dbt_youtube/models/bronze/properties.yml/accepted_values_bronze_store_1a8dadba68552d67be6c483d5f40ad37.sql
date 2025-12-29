
    
    

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


