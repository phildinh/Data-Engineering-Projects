with sales as (
    select
        sales_id,
        product_sk,
        customer_sk,
        
    unit_price * quantity
 as calculated_gross_amount,
        gross_amount,
        payment_method
    from `dbt_tutorial_dev`.`bronze`.`bronze_sales`
),

products as (
    select
        product_sk,
        category
    from `dbt_tutorial_dev`.`bronze`.`bronze_product`
),

customers as (
    select
        customer_sk,
        gender
    from `dbt_tutorial_dev`.`bronze`.`bronze_customer`
),

joined_query as (
select
    sales.sales_id,
    sales.gross_amount,
    sales.payment_method,
    products.category,
    customers.gender
from sales 
join products 
    on sales.product_sk = products.product_sk
join customers 
    on sales.customer_sk = customers.customer_sk
)

select
    category,
    gender,
    SUM(gross_amount) as total_sales
from
    joined_query
group by
    category,
    gender
order by
    total_sales desc