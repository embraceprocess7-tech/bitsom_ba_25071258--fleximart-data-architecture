#%% md
# ## extract
#%%
import csv
#%%
import pandas as pd
from pathlib import Path
import numpy as np

#%% md
# CUSTOMER DATA
#%%
data = [
    {"customer_id": "C001", "first_name": "Rahul",   "last_name": "Sharma",   "email": "rahul.sharma@gmail.com","phone": "9876543210",     "city": "Bangalore",   "registration_date": "2023-01-15"},
    {"customer_id": "C002", "first_name": "Priya",   "last_name": "Patel",    "email": "priya.patel@yahoo.com","phone": "+91-9988776655", "city": "Mumbai",      "registration_date": "2023-02-20"},
    {"customer_id": "C003", "first_name": "Amit",    "last_name": "Kumar",    "email": "",                 "phone": "9765432109",     "city": "Delhi",       "registration_date": "2023-03-10"},
    {"customer_id": "C004", "first_name": "Sneha",   "last_name": "Reddy",    "email": "sneha.reddy@gmail.com","phone": "9123456789",     "city": "Hyderabad",   "registration_date": "15/04/2023"},
    {"customer_id": "C005", "first_name": "Vikram",  "last_name": "Singh",    "email": "vikram.singh@outlook.com", "phone": "09988112233",    "city": "Chennai",     "registration_date": "2023-05-22"},
    {"customer_id": "C006", "first_name": "Anjali",  "last_name": "Mehta",    "email": "anjali.mehta@gmail.com","phone": "9876543210",     "city": "Bangalore",   "registration_date": "2023-06-18"},
    {"customer_id": "C007", "first_name": "Ravi",    "last_name": "Verma",    "email": "",                 "phone": "+919876501234",  "city": "Pune",        "registration_date": "2023-07-25"},
    {"customer_id": "C008", "first_name": "Pooja",   "last_name": "Iyer",     "email": "pooja.iyer@gmail.com","phone": "9123456780",     "city": "Bangalore",   "registration_date": "15-08-2023"},
    {"customer_id": "C009", "first_name": "Karthik", "last_name": "Nair",     "email": "karthik.nair@yahoo.com","phone": "9988776644",     "city": "Kochi","registration_date": "2023-09-30"},
    {"customer_id": "C010", "first_name": "Deepa",   "last_name": "Gupta",    "email": "deepa.gupta@gmail.com","phone": "09871234567",    "city": "Delhi", "registration_date": "2023-10-12"},
    {"customer_id": "C001", "first_name": "Rahul",   "last_name": "Sharma","email": "rahul.sharma@gmail.com",  "phone": "9876543210",     "city": "Bangalore",   "registration_date": "2023-01-15"},
    {"customer_id": "C011", "first_name": "Arjun",   "last_name": "Rao","email": "arjun.rao@gmail.com","phone": "9876509876",     "city": "Hyderabad","registration_date": "2023-11-05"},
    {"customer_id": "C012", "first_name": "Lakshmi", "last_name": "Krishnan", "email": "",                 "phone": "9988001122",     "city": "Chennai","registration_date": "2023-12-01"},
    {"customer_id": "C013", "first_name": "Suresh",  "last_name": "Patel",    "email": "suresh.patel@outlook.com", "phone": "9123409876","city": "Mumbai",      "registration_date": "2024-01-08"},
    {"customer_id": "C014", "first_name": "Neha",    "last_name": "Shah",     "email": "neha.shah@gmail.com",     "phone": "+91-9876543221", "city": "Ahmedabad",   "registration_date": "2024-01-15"},
    {"customer_id": "C015", "first_name": "Manish",  "last_name": "Joshi",    "email": "manish.joshi@yahoo.com",  "phone": "9988776611",     "city": "Jaipur",      "registration_date": "20/01/2024"},
    {"customer_id": "C016", "first_name": "Divya",   "last_name": "Menon",    "email": "divya.menon@gmail.com",   "phone": "9123456701",     "city": "Bangalore",   "registration_date": "2024-02-05"},
    {"customer_id": "C017", "first_name": "Rajesh",  "last_name": "Kumar",    "email": "rajesh.kumar@gmail.com",  "phone": "09876123450",    "city": "Delhi",       "registration_date": "2024-02-12"},
    {"customer_id": "C018", "first_name": "Kavya",   "last_name": "Reddy",    "email": "",                      "phone": "9988112200",     "city": "Hyderabad",   "registration_date": "2024-02-18"},
    {"customer_id": "C019", "first_name": "Arun",    "last_name": "Pillai",   "email": "arun.pillai@outlook.com", "phone": "9876543298",     "city": "Kochi",       "registration_date": "25-02-2024"},
    {"customer_id": "C020", "first_name": "Swati",   "last_name": "Desai",    "email": "swati.desai@gmail.com",   "phone": "9123456712",     "city": "Pune",        "registration_date": "2024-03-01"},
    {"customer_id": "C021", "first_name": "Nikhil",  "last_name": "Bose",     "email": "nikhil.bose@gmail.com",   "phone": "+919988776600",  "city": "Kolkata",     "registration_date": "2024-03-10"},
    {"customer_id": "C022", "first_name": "Priyanka","last_name": "Jain",     "email": "priyanka.jain@yahoo.com", "phone": "9876543287",     "city": "Indore",      "registration_date": "2024-03-15"},
    {"customer_id": "C023", "first_name": "Rohit",   "last_name": "Kapoor",   "email": "",                      "phone": "9988112211",     "city": "Chandigarh",  "registration_date": "2024-03-20"},
    {"customer_id": "C024", "first_name": "Meera",   "last_name": "Nambiar",  "email": "meera.nambiar@gmail.com", "phone": "9123456723",     "city": "Trivandrum",  "registration_date": "25-03-2024"},
    {"customer_id": "C025", "first_name": "Sanjay",  "last_name": "Agarwal",  "email": "sanjay.agarwal@gmail.com", "phone": "09876543276",    "city": "Lucknow",     "registration_date": "2024-03-28"}
]
#%%
df = pd.DataFrame(data)
#%%
customers = df.to_csv("customers_raw.csv", index = False)
#%%
df1= pd.read_csv("customers_raw.csv")
#%%
print(df1.head())
#%%
df1.info()
#%%
print(df1)
#%% md
# dropping duplicates- 01 row found to be duplicate - C001
#%%
df1.drop_duplicates(subset=['customer_id'], keep = 'first', inplace=True)
df1
#%% md
# Handle missing values - drop, fill or default
#%%
df1.isna().sum()
#%%
df1.fillna("None", inplace=True)
df1
#%% md
# Standardize phone formats
#%%
import phonenumbers
import re
#%% md
# standardize phone number format
#%%

def normalize_phone(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    s_clean = re.sub(r'[^\d+]', '', s)     # remove spaces, dashes, parentheses, etc.
    digits = re.sub(r'\D', '', s_clean)   # digits only
    if len(digits) < 10:
        return s                           # leave short/malformed numbers as-is for review
    local = digits[-10:]                   # take last 10 digits as local number
    return "+91" + local

# apply in-place so print(df) shows the changes
df1['phone'] = df1['phone'].apply(normalize_phone)
print(df1)

#%% md
# change the date format
#%%
import pandas as pd

def clean_mixed_dates(s: pd.Series) -> pd.Series:
    # Normalize text
    s = (
        s.astype(str)
         .str.strip()
         .str.replace(r"[./_]", "-", regex=True)
         .replace({"": None, "nan": None})
    )

    # First pass: infer format
    dt = pd.to_datetime(
        s,
        errors="coerce",
        infer_datetime_format=True
    )

    # Second pass: force DD-MM-YYYY where inference failed
    mask = dt.isna() & s.str.match(r"\d{2}-\d{2}-\d{4}")
    dt.loc[mask] = pd.to_datetime(
        s[mask],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # ✅ Return datetime, NOT formatted string
    return dt

#%%
df1["registration_date"] = clean_mixed_dates(df1["registration_date"])

#%%
df1["registration_date"].dt.strftime("%d-%m-%Y").head(25)

#%%
print(df1)
#%%
df1.info()
#%% md
# 
#%% md
# converting customer_id from Object to integer
#%%
df1['customer_id'] = df1['customer_id'].str.replace(r'\D', '', regex=True).astype(int)

#%%
print(df1)
#%%
df1.info()
#%% md
# Inserting data into Mysql workbench
#%%
import mysql.connector
#%%
def upload_data_db(df : pd.DataFrame, customers :str) :
    conn = mysql.connector.Connect(
    host = 'localhost' ,
    user = 'root' ,
    password = '224709@Ab'  ,
    database = 'fleximart' ,
    autocommit=True ,
    )

    cursor = conn.cursor()

    cols_names = ",".join(df.columns)
    placeholder = ",".join(["%s"] * len(df.columns))
    sql = f"""insert into fleximart.{customers}({cols_names}) values ({placeholder})"""

    cursor.executemany(sql,df.values.tolist())

    conn.commit()

    cursor.close()
    conn.close()
#%%
upload_data_db(df1,"customers")
#%% md
# DATA QUALITY REPORT
#%%
import pandas as pd

def data_quality_metrics(df1, primary_key=None):
    metrics = {}

    metrics["records_processed"] = len(df1)

    # Duplicate handling
    if primary_key:
        duplicates = df1.duplicated(subset=[primary_key]).sum()
        df = df1.drop_duplicates(subset=[primary_key])
    else:
        duplicates = df1.duplicated().sum()
        df = df1.drop_duplicates()

    metrics["duplicates_removed"] = duplicates

    # Missing values
    missing_before = df1.isnull().sum().sum()
    df = df1.fillna(0)
    missing_after = df.isnull().sum().sum()

    metrics["missing_values_handled"] = missing_before - missing_after
    metrics["records_loaded"] = len(df)

    return df, metrics

#%%
customers_df = pd.read_csv("customers_raw.csv")

clean_customers_df, customer_metrics = data_quality_metrics(
    customers_df,
    primary_key="customer_id"
)

#%%
with open("data_quality_report.txt", "w") as file:
    file.write("DATA QUALITY REPORT\n")
    file.write("===================\n\n")

    file.write("Customers Data\n")
    file.write(f"Records processed: {customer_metrics['records_processed']}\n")
    file.write(f"Duplicates removed: {customer_metrics['duplicates_removed']}\n")
    file.write(f"Missing values handled: {customer_metrics['missing_values_handled']}\n")
    file.write(f"Records loaded successfully: {customer_metrics['records_loaded']}\n")

#%%
import os
print(os.getcwd())

#%% md
# file named- data_quality_report.txt exist locally in above mentioed file path.
#%% md
# PRODUCT DATA
#%%
data1 = [{'product_id': 'P001', 'product_name' : 'Samsung Galaxy S21', 'category' : 'Electronics' ,'price': 45999.00 , 'stock_quantity' : 150 },
{'product_id': 'P002', 'product_name' : 'Nike Running Shoes', 'category' : 'fashion', 'price': 3499.00, 'stock_quantity' : 80  },
{'product_id': 'P003', 'product_name' : 'Apple MacBook Pro', 'category' : 'ELECTRONICS', 'stock_quantity' : 45  },
{'product_id': 'P004', 'product_name' : 'Levi Jeans', 'category' : 'fashion', 'price': 2999.00, 'stock_quantity' : 120 },
{'product_id': 'P005', 'product_name' : 'Sony Headphones', 'category' : 'Electronics', 'price': 1999.00, 'stock_quantity' : 200 },
{'product_id': 'P006', 'product_name' : 'Organic Almonds', 'category' : 'Groceries' , 'price' :  899.00  },
{'product_id': 'P007', 'product_name' : 'HP Laptop' , 'category' : 'Electronics' , 'price': 52999.00 ,'stock_quantity' : 60   },
{'product_id': 'P008', 'product_name' : 'Adidas T-Shirt' , 'category' : 'fashion', 'price': 1299.00, 'stock_quantity' : 150},
{'product_id': 'P009', 'product_name' : 'Basmati Rice 5kg','category' : 'Groceries' ,'price': 650.00, 'stock_quantity' : 300  },
{'product_id': 'P010', 'product_name' : 'OnePlus Nord', 'category' : 'Electronics' ,'stock_quantity' : 95 },
{'product_id': 'P011', 'product_name' : 'Puma Sneakers', 'category' : 'fashion', 'price': 4599.00, 'stock_quantity' : 70  },
{'product_id': 'P012', 'product_name' : 'Dell Monitor 24inch', 'category' : 'Electronics' ,'price': 12999.00, 'stock_quantity' : 40 },
{'product_id': 'P013', 'product_name' : 'Woodland Shoes', 'category' : 'fashion', 'price': 5499.00, 'stock_quantity' : 55},
{ 'product_id': 'P014', 'product_name' : 'iPhone 13', 'category' : 'Electronics' ,'price': 69999.00, 'stock_quantity' : 80  } ,
{'product_id': 'P015', 'product_name' : 'Organic Honey 500g', 'category' : 'Groceries' ,'price': 450.00, 'stock_quantity' : 200   },
{'product_id': 'P016', 'product_name' : 'Samsung TV 43inch', 'category' : 'Electronics' ,'price': 32999.00, 'stock_quantity' : 35},
{'product_id': 'P017', 'product_name' : 'H&M Shirt', 'category' : 'fashion',  'stock_quantity' : 90 },
{'product_id': 'P018', 'product_name' :'Masoor Dal 1kg', 'category' : 'Groceries', 'price': 120.00, 'stock_quantity' : 500  },
{'product_id': 'P019', 'product_name' : 'Boat Earbuds', 'category' : 'Electronics' ,'price': 1499.00, 'stock_quantity' : 250 },
{'product_id': 'P020', 'product_name' : 'Reebok Trackpants', 'category' : 'fashion', 'price': 1899.00, 'stock_quantity' : 110 }]
#%%
df= pd.DataFrame(data1)
#%%
product = df.to_csv("output1.csv", index = False)
#%%
df = pd.read_csv("output1.csv")
#%%
df.shape
#%%
df.info()
#%%
print(df.head())
#%% md
# Standardize category names (eg. "electronics" to "Electronics")
#%%
df['category'] = df['category'].astype(str).str.capitalize()
print(df)

#%% md
# handling missing values
#%%
df.isna().sum()
#%%
df.info()
#%%
df['price'] = df['price'].fillna(
    df.groupby('category')['price'].transform('median')
)
#%%
df['stock_quantity'] = df['stock_quantity'].fillna(
    df.groupby('category')['stock_quantity'].transform('median')
)

#%%
df.isna().sum()
#%%
df.info()
#%%
print(df)
#%% md
# Extra spaces in some product names
#%%
df['product_name'] = (
    df['product_name']
    .astype(str)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
)

#%%
print(df)
#%% md
# converting customer_id from Object to integer
#%%
df['product_id'] = df['product_id'].str.replace(r'\D', '', regex=True).astype(int)

#%%
df.info()
#%%
print(df)
#%% md
# inserting data to the MYSQL database tables
#%%
import mysql.connector
#%%
def upload_data_db(df : pd.DataFrame, products :str) :
    conn = mysql.connector.Connect(
    host = 'localhost' ,
    user = 'root' ,
    password = '224709@Ab'  ,
    database = 'fleximart' ,
    autocommit=True ,
    )

    cursor = conn.cursor()

    cols_names = ",".join(df.columns)
    placeholder = ",".join(["%s"] * len(df.columns))
    sql = f"""insert into fleximart.{products}({cols_names}) values ({placeholder})"""

    cursor.executemany(sql,df.values.tolist())

    conn.commit()

    cursor.close()
    conn.close()
#%%
upload_data_db(df,"products")
#%% md
# SALES TRANSACTION DATA
#%%
data2 = [{'transaction_id' :'T001', 'customer_id' : 'C001' , 'product_id' : 'P001' , 'quantity' : 1 , 'unit_price' : 45999.00, 'transaction_date' : '2024-01-15' , 'status' : 'Completed' },
  {'transaction_id' :'T002', 'customer_id' : 'C002' , 'product_id' : 'P004' , 'quantity' : 2 , 'unit_price' : 2999.00, 'transaction_date' : '2024-01-16' , 'status' : 'Completed' }
    ,{'transaction_id' :'T003', 'customer_id' : 'C003' , 'product_id' : 'P007' , 'quantity' : 1 , 'unit_price' : 52999.00, 'transaction_date' : '15/01/2024' , 'status' : 'Completed'  },
    {'transaction_id' :'T004', 'product_id' : 'P002' , 'quantity' : 1 , 'unit_price' : 3499.00,'transaction_date' : '2024-01-18' , 'status' : 'Pending' },
    {'transaction_id' :'T005', 'customer_id' : 'C005' , 'product_id' : 'P009' , 'quantity' : 3 , 'unit_price' : 650.00, 'transaction_date' : '2024-01-20' , 'status' : 'Completed' },
    {'transaction_id' :'T006', 'customer_id' : 'C006' , 'product_id' : 'P012' , 'quantity' : 1 , 'unit_price' : 12999.00, 'transaction_date' : '2024-01-22' , 'status' : 'Completed' },
    {'transaction_id' :'T007', 'customer_id' : 'C007' , 'product_id' : 'P005' , 'quantity' : 2 , 'unit_price' : 1999.00, 'transaction_date' : '2024-01-25' , 'status' : 'Completed' },
    {'transaction_id' :'T008', 'customer_id' : 'C008' , 'quantity' : 1 , 'unit_price' : 1299.00, 'transaction_date' : '2024-01-25' , 'status' : 'Completed' },
    {'transaction_id' :'T009', 'customer_id' : 'C009' , 'product_id' : 'P011' , 'quantity' : 1 , 'unit_price' : 4599.00, 'transaction_date' : '2024-01-28' , 'status' : 'Cancelled' },
    {'transaction_id' :'T010', 'customer_id' : 'C010' , 'product_id' : 'P006' , 'quantity' : 5 , 'unit_price' : 899.00, 'transaction_date' : '2024-02-01' , 'status' : 'Completed' },
    {'transaction_id' :'T001', 'customer_id' : 'C001' , 'product_id' : 'P001' , 'quantity' : 1 , 'unit_price' : 45999.00, 'transaction_date' : '2024-01-15' , 'status' : 'Completed'},
    {'transaction_id' :'T011', 'customer_id' : 'C011' , 'product_id' : 'P014' , 'quantity' : 1 , 'unit_price' :69999.00,'transaction_date' : '02/02/2024' , 'status' : 'Completed' },
    {'transaction_id' :'T012', 'customer_id' : 'C012' , 'product_id' : 'P003' , 'quantity' : 1 , 'unit_price' : 52999.00, 'transaction_date' : '2024-02-05' , 'status' : 'Completed'},
    {'transaction_id' :'T013', 'customer_id' : 'C013' , 'product_id' : 'P015' , 'quantity' : 3, 'unit_price' : 450.00, 'transaction_date' : '2024-02-08' , 'status' : 'Completed' },
    {'transaction_id' :'T014', 'customer_id' : 'C014' , 'product_id' : 'P019' , 'quantity' : 2 , 'unit_price' : 1499.00, 'transaction_date' : '02-10-2024' , 'status' : 'Completed' },
    {'transaction_id' :'T015', 'customer_id' : 'C015' , 'product_id' : 'P008' , 'quantity' : 3 , 'unit_price' : 1299.00, 'transaction_date' : '2024-02-12' , 'status' : 'Completed' },
    {'transaction_id' :'T016',  'product_id' : 'P013' , 'quantity' : 1 , 'unit_price' : 5499.00, 'transaction_date' : '2024-02-15' , 'status' : 'Pending'  },
    {'transaction_id' :'T017', 'customer_id' : 'C017' , 'product_id' : 'P016' , 'quantity' : 1, 'unit_price' : 32999.00, 'transaction_date' : '2024-02-18' , 'status' : 'Completed' },
    {'transaction_id' :'T018', 'customer_id' : 'C018' , 'product_id' : 'P020' , 'quantity' : 2, 'unit_price' : 1899.00, 'transaction_date' : '2024-02-20' , 'status' : 'Completed' },
    {'transaction_id' :'T019', 'customer_id' : 'C019' , 'product_id' : 'P018' , 'quantity' : 10, 'unit_price' : 120.00, 'transaction_date' : '2024-02-22' , 'status' : 'Completed' },
    {'transaction_id' :'T020', 'customer_id' : 'C020' , 'product_id' : 'P010' , 'quantity' : 1, 'unit_price' : 45999.00, 'transaction_date' : '2024-02-25' , 'status' : 'Completed' },
    {'transaction_id' :'T021', 'customer_id' : 'C021' , 'product_id' : 'P017' , 'quantity' : 2, 'unit_price' :2999.00, 'transaction_date' : '2024-02-28' , 'status' : 'Completed' },
    {'transaction_id' :'T022', 'customer_id' : 'C002' , 'product_id' : 'P001' , 'quantity' : 1, 'unit_price' :45999.00, 'transaction_date' : '2024-03-01' , 'status' : 'Completed' },
    {'transaction_id' :'T023', 'customer_id' : 'C003' , 'product_id' : 'P019' , 'quantity' : 3, 'unit_price' : 1499.00,  'transaction_date' : '03-02-2024' , 'status' : 'Completed' },
    {'transaction_id' :'T024', 'customer_id' : 'C004' , 'product_id' : 'P009' , 'quantity' : 5, 'unit_price' : 650.00, 'transaction_date' : '2024-03-05' , 'status' : 'Completed' },
    {'transaction_id' :'T025', 'customer_id' : 'C005' ,  'quantity' : 1, 'unit_price' : 1999.00,  'transaction_date' : '2024-03-08' , 'status' : 'Completed' },
    {'transaction_id' :'T026', 'customer_id' : 'C006' , 'product_id' : 'P011' , 'quantity' : 1, 'unit_price' : 4599.00,  'transaction_date' : '2024-03-10' , 'status' : 'Completed' },
    {'transaction_id' :'T027', 'customer_id' : 'C007' , 'product_id' : 'P002' , 'quantity' : 2, 'unit_price' : 3499.00,  'transaction_date' : '03/12/2024' , 'status' : 'Completed' },
    {'transaction_id' :'T028', 'customer_id' : 'C008' , 'product_id' : 'P015' , 'quantity' : 4, 'unit_price' : 450.00,  'transaction_date' : '2024-03-15' , 'status' : 'Completed' },
    {'transaction_id' :'T029', 'customer_id' : 'C009' , 'product_id' : 'P007' , 'quantity' : 1, 'unit_price' : 52999.00, 'transaction_date' : '2024-03-18' , 'status' : 'Completed' },
    {'transaction_id' :'T030',  'product_id' : 'P004' , 'quantity' : 3, 'unit_price' : 2999.00,  'transaction_date' : '2024-03-20' , 'status' : 'Pending' },
    {'transaction_id' :'T031', 'customer_id' : 'C011' , 'product_id' : 'P012' , 'quantity' : 1, 'unit_price' : 12999.00, 'transaction_date' : '2024-03-22' , 'status' : 'Completed' },
    {'transaction_id' :'T032', 'customer_id' : 'C012' , 'product_id' : 'P016' , 'quantity' : 1, 'unit_price' : 32999.00,  'transaction_date' : '2024-03-25' , 'status' : 'Completed' },
    {'transaction_id' :'T033', 'customer_id' : 'C013' , 'product_id' : 'P005' , 'quantity' : 2, 'unit_price' : 1999.00, 'transaction_date' : '2024-03-28' , 'status' : 'Completed' },
    {'transaction_id' :'T034', 'customer_id' : 'C014' , 'product_id' : 'P008' , 'quantity' : 2, 'unit_price' : 1299.00,  'transaction_date' : '2024-03-30' , 'status' : 'Completed' },
    {'transaction_id' :'T035', 'customer_id' : 'C015' , 'product_id' : 'P018' , 'quantity' : 8, 'unit_price' : 120.00, 'transaction_date' : '04/01/2024' , 'status' : 'Completed' },
    {'transaction_id' :'T036', 'customer_id' : 'C016' , 'product_id' : 'P014' , 'quantity' : 1, 'unit_price' : 69999.00, 'transaction_date' : '2024-04-03' , 'status' : 'Completed' },
    {'transaction_id' :'T037', 'customer_id' : 'C017' , 'product_id' : 'P006' , 'quantity' : 4, 'unit_price' : 899.00,  'transaction_date' : '2024-04-05' , 'status' : 'Completed' },
    {'transaction_id' :'T038', 'customer_id' : 'C018' , 'product_id' : 'P020' , 'quantity' : 1, 'unit_price' : 1899.00,  'transaction_date' : '04-08-2024' , 'status' : 'Completed' },
    {'transaction_id' :'T039', 'customer_id' : 'C019' , 'product_id' : 'P019' , 'quantity' : 2, 'unit_price' : 1499.00, 'transaction_date' : '2024-04-10' , 'status' : 'Completed' },
    {'transaction_id' :'T040', 'customer_id' : 'C020' , 'product_id' : 'P013' , 'quantity' : 1, 'unit_price' : 5499.00, 'transaction_date' : '2024-04-12' , 'status' : 'Completed' }]
#%%
df= pd.DataFrame(data2)
#%%
sales = df.to_csv("output2.csv", index = False)

#%%
Sales = pd.read_csv("output2.csv")
#%%
print(Sales.head())
#%%
Sales.info()
#%% md
# FOR KNOWING FILES PATH -RAW.CSV
#%%
from pathlib import Path
out = Path("data/output.csv")               # relative or absolute
out.parent.mkdir(parents=True, exist_ok=True)  # create folder if needed
df.to_csv(out, index=False)
print("CSV saved to:", out.resolve())

#%%
from pathlib import Path
out = Path("data/output1.csv")               # relative or absolute
out.parent.mkdir(parents=True, exist_ok=True)  # create folder if needed
df.to_csv(out, index=False)
print("CSV saved to:", out.resolve())

#%%
from pathlib import Path
out = Path("data/output2.csv")               # relative or absolute
out.parent.mkdir(parents=True, exist_ok=True)  # create folder if needed
df.to_csv(out, index=False)
print("CSV saved to:", out.resolve())

#%% md
# ## Transform
#%% md
# remove duplicate records
#%%
import re
#%% md
# drop duplicate data -TOO1
#%%
df.drop_duplicates(subset=['transaction_id'], keep = 'first', inplace=True)
#%%
print(df)
#%% md
# HANDLE MISSING VALUES
#%%
df.isna().sum()
#%%
df.info()
#%%
df = df.dropna()
df
#%% md
# STANDARDIZE THE DATE FORMAT
#%%
import pandas as pd

def clean_mixed_dates(s: pd.Series) -> pd.Series:
    # Normalize text
    s = (
        s.astype(str)
         .str.strip()
         .str.replace(r"[./_]", "-", regex=True)
         .replace({"": None, "nan": None})
    )

    # First pass: infer format
    dt = pd.to_datetime(
        s,
        errors="coerce",
        infer_datetime_format=True
    )

    # Second pass: force DD-MM-YYYY where inference failed
    mask = dt.isna() & s.str.match(r"\d{2}-\d{2}-\d{4}")
    dt.loc[mask] = pd.to_datetime(
        s[mask],
        format="%d-%m-%Y",
        errors="coerce"
    )

    # ✅ Return datetime, NOT formatted string
    return dt

#%%
df["transaction_date"] = clean_mixed_dates(df["transaction_date"])
#%%
df["transaction_date"].dt.strftime("%d-%m-%Y").head()
#%%
print(df)
#%%
df['total_amount'] = (df['unit_price'] * df['quantity']).round(2)

#%%

df = df.rename(columns={'transaction_id': 'order_id', 'transaction_date': 'order_date'})

#%%
print(df)
#%% md
# covert order_id , customer_id datatype from object to integer
#%%
df['order_id'] = df['order_id'].str.replace(r'\D', '', regex=True).astype(int)

#%%
df['customer_id'] = df['customer_id'].str.replace(r'\D', '', regex=True).astype(int)

#%%
df['product_id'] = df['product_id'].str.replace(r'\D', '', regex=True).astype(int)

#%%
print(df)
#%% md
# slicing order table from df
#%%
orders = df[['order_id', 'customer_id','order_date', 'total_amount','status']]
print(orders)
#%%
orders.info()
#%% md
# uploading order table data to mysql
#%%
import mysql.connector
#%%
def upload_data_db(df : pd.DataFrame, orders :str) :
    conn = mysql.connector.Connect(
    host = 'localhost' ,
    user = 'root' ,
    password = '224709@Ab'  ,
    database = 'Fleximart' ,
    autocommit=True ,
    )

    cursor = conn.cursor()

    cols_names = ",".join(df.columns)
    placeholder = ",".join(["%s"] * len(df.columns))
    sql = f"""insert into Fleximart.{orders}({cols_names}) values ({placeholder})"""

    cursor.executemany(sql,df.values.tolist())

    conn.commit()

    cursor.close()
    conn.close()
#%%
upload_data_db(orders,"orders")
#%% md
# slicing order_items table from df
#%%
df['order_item_id'] = range(1, 36)

#%%
df = df.rename(columns={'total_amount': 'subtotal'})
#%%
order_item = df[['order_item_id', 'order_id', 'product_id', 'quantity', 'unit_price', 'subtotal']]
#%%
order_item.info()
#%% md
# inserting data into Mysql workbench
#%%
import mysql.connector
#%%
def upload_data_db(df : pd.DataFrame, order_items :str) :
    conn = mysql.connector.Connect(
    host = 'localhost' ,
    user = 'root' ,
    password = '224709@Ab'  ,
    database = 'fleximart' ,
    autocommit=True ,
    )

    cursor = conn.cursor()

    cols_names = ",".join(df.columns)
    placeholder = ",".join(["%s"] * len(df.columns))
    sql = f"""insert into fleximart.{order_items}({cols_names}) values ({placeholder})"""

    cursor.executemany(sql,df.values.tolist())

    conn.commit()

    cursor.close()
    conn.close()
#%%
upload_data_db(order_item,"order_items")