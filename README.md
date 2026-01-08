# FlexiMart Data Architecture Project

**Student Name:** [Narendra Singh]
**Student ID:** [bitsom_ba_25071258]
**Email:** [embraceprocess7@gmail.com]
**Date:** [08-01-2026]

## Project Overview

[This project implements an end-to-end ETL pipeline to extract data from raw CSV files and transform it through data cleaning and validation.
The cleaned data is loaded into a MySQL-based relational data warehouse designed with primary and foreign key constraints.
Data quality checks are applied to handle duplicate records and missing values, and a data quality report is generated.further data has been 
analysed using business query implimentation and OLAP analytics query]

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

[I one from mechanical background, this is new horizon for me.I was taught basic level python and mongo was tought more of theory during our classes.SQL was taught well during foundation course.
For me GITHUB is totally new concept , i am learning this using youtube matrial from basic what GIT is and what GITHUB is.Now i am learning python by re-visiting course material , PDF book youtube vidoes.All togther i have understood like this course is guiding me to  ]

## Challenges Faced

1. [I strug]
2. [Challenge and solution]


