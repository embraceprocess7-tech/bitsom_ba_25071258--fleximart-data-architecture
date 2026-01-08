# FlexiMart Data Architecture Project

**Student Name:** [Narendra Singh]
**Student ID:** [bitsom_ba_25071258]
**Email:** [embraceprocess7@gmail.com]
**Date:** [08-01-2026]

## Project Overview

[This project implements an end-to-end ETL pipeline to extract data from raw CSV files and transform it through data cleaning and validation.
The cleaned data is loaded into a MySQL-based relational data warehouse designed with primary and foreign key constraints.
Data quality checks are applied to handle duplicate records and missing values, and a data quality report is generated.further data has been 
analysed using business query implimentation and OLAP analytics query.
##Note - Clean MySql tables prior running files. i have kept raw_data files names - output.csv for products_raw.csv, output1.csv for sales_raw.csv]

## Repository Structure
├── part1-database-etl/
│   ├── etl_pipeline.py
│   ├── schema_documentation.md
│   ├── business_queries.sql
│   └── data_quality_report.txt
├── part2-nosql/
│   ├── nosql_analysis.md
│   ├── mongodb_operations.py
│   └── products_catalog.json
├── part3-datawarehouse/
│   ├── star_schema_design.md
│   ├── warehouse_schema.sql
│   ├── warehouse_data.sql
│   └── analytics_queries.sql
└── README.md

## Technologies Used

- Python 3.14.0, pandas,numpy, path, phonenumbers, re, os,  mysql-connector-python
- JSON, Datetime, pymongo,MongoClient, 
- MySQL 8.0.44
- MongoDB 8.2.1

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql


### MongoDB Setup

mongosh < part2-nosql/mongodb_operations.py

## Key Learnings

[I have top 4 learning during the assignment.Learnings are as follows:- 
1. How to do python coding on hit and trial basis. Using youtube videos and books.

2. How to push data from Pycharm to MySql.

3. How to create repository and How to push data from Pycharm to Github. 

Note - I one from mechanical background, this is new horizon for me.I was taught basic level python and mongo was tought more of theory during our classes.SQL was taught well during foundation course.
For me GITHUB is totally new concept , i am learning this using youtube matrial from basic what GIT is and what GITHUB is.Now i am learning python by re-visiting course material ,books & youtube vidoes.All togther i have understood like this course is guiding me to right path. Only way to excel is to learn from free sources , books as our instructors have guided us]

## Challenges Faced

1. [I struggled while uploading data to MySql from Pycharm , it took me time to resolve the issue.]
2. [It took me lot of time to understand what GITHUB is how does it function.]
3. [SQL OLAP queries were quite difficult]



