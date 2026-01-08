#1 dim_date data

INSERT INTO fleximart_dw.dim_date (
    date_key,
    full_date,
    day_of_week,
    day_of_month,
    `month`,
    month_name,
    `quarter`,
    `year`,
    is_weekend
)
SELECT
    DATE_FORMAT(dte, '%Y%m%d') AS date_key,
    dte AS full_date,
    DAYNAME(dte),
    DAY(dte),
    MONTH(dte),
    MONTHNAME(dte),
    QUARTER(dte),
    YEAR(dte),
    DAYOFWEEK(dte) IN (1,7)
FROM (
    WITH RECURSIVE dates AS (
        SELECT MIN(order_date) AS dte
        FROM fleximart.orders
        UNION ALL
        SELECT DATE_ADD(dte, INTERVAL 1 DAY)
        FROM dates
        WHERE dte < (SELECT MAX(order_date) FROM fleximart.orders)
    )
    SELECT dte FROM dates
) x;



#2 dim_product data

INSERT INTO fleximart_dw.dim_product (
    product_id,
    product_name,
    category,
    subcategory,
    unit_price
)
SELECT DISTINCT
    p.product_id,
    p.product_name,
    p.category,
    NULL AS subcategory,
    p.price
FROM fleximart.products AS p;

select* from dim_product;



#3 dim_customer data

INSERT INTO fleximart_dw.dim_customer (
    customer_id,
    customer_name,
    city,
    state,
    customer_segment
)
SELECT DISTINCT
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.city,
     NUll as state,
    NUll as customer_segment
FROM fleximart.customers c;

select * from dim_customer;


#4 fact_sale data


INSERT INTO fleximart_dw.fact_sales (
    date_key,
    product_key,
    customer_key,
    quantity_sold,
    unit_price,
    discount_amount,
    total_amount
)
SELECT
    dd.date_key,
    dp.product_key,
    dc.customer_key,
    oi.quantity AS quantity_sold,
    oi.unit_price,
    0 AS discount_amount,
    (oi.quantity * oi.unit_price)  AS total_amount
FROM fleximart.orders o
JOIN fleximart.order_items oi
    ON o.order_id = oi.order_id
JOIN fleximart_dw.dim_date dd
    ON dd.full_date = o.order_date
JOIN fleximart_dw.dim_product dp
    ON dp.product_id = oi.product_id
JOIN fleximart_dw.dim_customer dc
    ON dc.customer_id = o.customer_id;



