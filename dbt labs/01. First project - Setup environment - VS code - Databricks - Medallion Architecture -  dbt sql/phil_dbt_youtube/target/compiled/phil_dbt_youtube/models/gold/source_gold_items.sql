with dedup_query as (

    select
        *,
        row_number() over (
            partition by id
            order by updateDate desc
        ) as deduplication_id
    from `dbt_tutorial_dev`.`source`.`items`

)

select
    id,name, category, updateDate
from dedup_query
where deduplication_id = 1