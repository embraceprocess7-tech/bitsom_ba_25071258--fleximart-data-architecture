#Section A: Limitations of RDBMS

Que-1: Products having different attributes
In an RDBMS, all records in a table must follow a fixed schema. FlexiMart sells diverse products such as electronics and fashion 
items, each requiring different attributes (e.g., RAM and processor vs size and color). Representing this diversity in relational 
tables leads to many unused (NULL) columns or multiple related tables, making the design complex and inefficient.

Que-2: Frequent schema changes
Whenever a new product type or attribute is introduced, the relational schema must be modified using operations like ALTER TABLE. 
These changes are time-consuming, risky on large datasets, and can cause downtime, making RDBMS unsuitable for frequently evolving 
product catalogs.

Que-3: Storing customer reviews as nested data
RDBMS cannot store nested data naturally. Reviews must be stored in separate tables and retrieved using JOINs, which increases 
query complexity and reduces performance as data volume grows.

#Section B: NoSQL Benefits

Que-1: Flexible schema (document structure)
MongoDB allows each product document to have its own structure. Electronics and fashion products can store different fields inside 
the same collection without schema changes, making it ideal for diverse and evolving data.

Que-2: Embedded documents (reviews within products)
MongoDB supports embedding reviews directly inside product documents. This eliminates the need for JOIN operations and improves read 
performance when fetching products along with their reviews.

Que-3: Horizontal scalability
MongoDB supports horizontal scaling through sharding, allowing data to be distributed across multiple servers. This ensures better 
performance and availability as FlexiMart’s data and user base grow.

#Section C: Trade-offs

One disadvantage of MongoDB is weaker support for complex relational queries and strict ACID transactions compared to MySQL. Although 
transactions are supported, they are less efficient for highly relational data. Another drawback is data redundancy due to embedded 
documents, which can increase storage usage and make updates more complex if duplicated data exists.