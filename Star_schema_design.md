Star Schema Design – FlexiMart Data Warehouse

# Section 1: Schema Overview

Fact Table: fact_sales

Grain
One row per product per order line item.

Business Process
Sales transactions captured from the Flipkart operational database and stored for analytical reporting in the FlexiMart data warehouse.

Measures (Numeric Facts)

quantity_sold: Number of units sold for a product

unit_price: Price per unit at the time of sale

discount_amount: Discount applied on the product

total_amount: Final sales amount

Calculated as:

(quantity_sold × unit_price) − discount_amount


Foreign Keys

date_key → dim_date

product_key → dim_product

customer_key → dim_customer

Dimension Tables
1. dim_date

Purpose
Supports time-based analysis such as daily, monthly, quarterly, and yearly sales trends.

Type
Conformed dimension

Attributes

date_key (PK): Surrogate key in YYYYMMDD format

full_date: Actual calendar date

day_of_week: Name of the day (Monday, Tuesday, etc.)

day_of_month: Day number within the month

month: Month number (1–12)

month_name: Month name (January, February, etc.)

quarter: Quarter of the year (Q1, Q2, Q3, Q4)

year: Year (e.g., 2023, 2024)

is_weekend: Boolean flag indicating weekend

2. dim_product

Purpose
Provides detailed information about products for product-level sales analysis.

Attributes

product_key (PK): Surrogate product identifier

product_id: Original product ID from source system

product_name: Name of the product

category: Product category

subcategory: Product subcategory

brand: Brand of the product

3. dim_customer

Purpose
Enables customer-based analysis such as purchase behavior and segmentation.

Attributes

customer_key (PK): Surrogate customer identifier

customer_id: Original customer ID from source system

customer_name: Customer full name

gender: Gender of the customer

city: City of residence

state: State of residence

Star Schema Justification

The design follows a star schema where:

A single central fact table (fact_sales) stores measurable business data.

Multiple dimension tables provide descriptive context.

This structure enables:

Fast query performance

Simple joins

Easy aggregation for analytical reporting

The schema supports common analytical queries such as:

Monthly and yearly sales trends

Top-selling products and categories

Customer purchase behavior analysis

# SECTION -2 Design Decisions 

1. Why you chose this granularity (transaction line-item level)

The transaction line-item level granularity was chosen because it captures 
the most detailed form of sales data, where each row represents a single 
product sold in an order. This level of detail allows flexible analysis such
as sales by product, customer, date, or category. From this granular data, higher-level
summaries like daily, monthly, or yearly sales can be easily derived using aggregation. 
Choosing a finer granularity ensures that no analytical capability is lost and supports 
both detailed and summary reporting requirements.

2. Why surrogate keys instead of natural keys

Surrogate keys are used instead of natural keys to ensure stability, consistency, and better
performance in the data warehouse. Natural keys from source systems may change over time, 
be reused, or have business meaning that evolves. Surrogate keys are system-generated, 
immutable, and compact, which improves join performance between fact and dimension tables. 
They also simplify handling slowly changing dimensions and decouple the data warehouse from 
changes in the source systems.

3. How this design supports drill-down and roll-up operations

The star schema design supports roll-up and drill-down analysis through well-structured dimension
hierarchies. For example, the date dimension allows roll-up from day to month, quarter, and year, while
drill-down enables analysis from yearly sales down to specific dates. Similarly, users can roll up sales
by product category or drill down to individual products or customers. This structure makes analytical 
queries simple, fast, and intuitive for business reporting.

# Section 3: Sample Data Flow (Using Actual Warehouse Data)

##Source Transaction (Flipkart OLTP System)

Order ID: 201

Order Date: 2023-01-15

Customer ID: C001

Customer Name: Rahul Sharma

City: Bangalore

Product: HP Laptop

Quantity: 1

Unit Price: 52,999

Discount: Null

##Transformation Process (ETL)

The order date 2023-01-15 is mapped to the date dimension and assigned
date_key = 20230115.

Customer Rahul Sharma already exists in dim_customer with
customer_key = 1.

Product HP Laptop exists in dim_product with
product_key = 7.

The total sales amount is calculated as:
(1 × 52,999)  = 52,999.

Loaded into Data Warehouse
fact_sales

date_key: 20230115

customer_key: 1

product_key: 7

quantity_sold: 1

unit_price: 52999

discount_amount: Null

total_amount: 52,999

dim_date

date_key: 20230115

full_date: 2023-01-15

month: 1

quarter: Q1

year: 2023

dim_customer

customer_key: 1

customer_name: Rahul Sharma

city: Bangalore

dim_product

product_key: 7

product_name: HP Laptop

category: Electronics

unit_price: 52999

