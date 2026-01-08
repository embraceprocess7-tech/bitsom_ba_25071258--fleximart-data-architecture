#%%
import os
os.getcwd()
#%%
import os
print(os.getcwd())
#%%
import json
import datetime
from pymongo import MongoClient
import pandas as pd
#%%
db_name = 'fleximart'
collection = 'products_catalog'
mongo_url = 'mongodb://localhost:27017/'
#%%
file_path = r"C:\Users\USER\PycharmProjects\GRADED ASSIGNMENT MODULE 2\product_catalog.json"
#%%
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)
#%%
client = MongoClient(mongo_url)
db = client[db_name]
collections = db[collection]
#%% md
# Operation -1 LOAD DATA
#%%
collections.delete_many({})  # Clear existing data
rec = collections.insert_many(data)
print(f"Inserted {len(rec.inserted_ids)} documents into {db_name}.{collection}")
#%% md
# Operation 2 : Basic Query
# . Find all products in'Electronics" category with price less than 50000
# . Return only : name, price, stock
#%%
q2 = collections.find({"category": "Electronics","price": {"$lt": 50000}},{"_id":0,"name":1,"price":1,"Stock":1})

pd.DataFrame(list(q2))
#%% md
# Operation 3: Review Analysis (2 marks)
# Find all products that have average rating >= 4.0
# Use aggregation to calculate average from reviews array
# 
#%%
pipeline3 = [
    {
        "$addFields": {
            "avg_rating": {
                "$avg": {
                    "$ifNull": ["$reviews.rating", []]
                }
            }
        }
    },
    {
        "$match": {
            "avg_rating": { "$gte": 4.0 }
        }
    },
    {
        "$project": {
            "_id": 0,
            "product_id": 1,
            "name": 1,
            "category": 1,
            "avg_rating": { "$round": ["$avg_rating", 2] }
        }
    }
]

pd.DataFrame(list(collections.aggregate(pipeline3)))
#%% md
# OPERATION 4. Update operation
# Add a new review to product "ELEC001"
# Review: {user: "U999", rating: 4, comment: "Good value", date: ISODate()}
#%%
new_review = {
    "user": "U999",
    "rating": 4,
    "comment": "Good value for money.",
    "date": datetime.datetime.now()
}
#%%
res4 = collections.update_one(
    {"product_id": "ELEC001"},
    {"$push": {"reviews": new_review}},

)

print({"matched": res4.matched_count, "modified": res4.modified_count})
#%%
updated = collections.find_one(
    {"product_id": "ELEC001"},
    {"_id": 0, "product_id": 1, "name" : 1,  "reviews": 1})

updated
#%% md
# OPERATION 5. Complex aggregation
# Calculate average price by category
# Return: category, avg_price, product_count
# Sort by avg_price descending
#%%
pipeline5 = [
    {
        "$group": {
            "_id": "$category",
            "avg_price": { "$avg": "$price" },
            "product_count": { "$sum": 1 },
        }
    },
    {
        "$project": {
            "_id": 0,
            "category": "$_id",
            "avg_price": { "$round": ["$avg_price", 2] },
           "product_count": 1,
        }
    },
    { "$sort": { "avg_price": -1 }},

]

pd.DataFrame(list(collections.aggregate(pipeline5)))
#%%
pd.read_json("product_catalog.json")