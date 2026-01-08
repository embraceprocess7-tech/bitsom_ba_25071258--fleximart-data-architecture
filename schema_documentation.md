1. Entity–Relationship Description (Text Format)
ENTITY: customers

Purpose: Stores customer information
Attributes:

customer_id (PK): Unique identifier for each customer

first_name: Customer first name

last_name: Customer last name

email: Unique email address

phone: Contact number

created_at: Account creation date

Relationships:

One customer can place many orders (1:M with orders)

**ENTITY: orders**

Purpose: Stores order details
Attributes:

order_id (PK): Unique order identifier

customer_id (FK): References customers

order_date: Date of order

total_amount: Total order value

status: Order status

Relationships:

One order belongs to one customer

One order can have many order_items

ENTITY: products

Purpose: Stores product details
Attributes:

product_id (PK): Unique product identifier

product_name: Name of product

price: Unit price

category: Product category

Relationships:

One product can appear in many order_items

ENTITY: order_items

Purpose: Resolves M:N relationship between orders and products
Attributes:

order_item_id (PK): Unique identifier

order_id (FK): References orders

product_id (FK): References products

quantity: Number of units

unit_price: Price per unit

2. Normalization Explanation (3NF)

The database design follows Third Normal Form (3NF) to reduce redundancy and maintain data integrity.
Each table has a primary key, and all non-key attributes depend only on that key.

In the customers table, customer details depend solely on customer_id.

In the orders table, order-specific data depends only on order_id. Customer data is not repeated; instead, customer_id is used as a foreign key.

The products table stores only product-related attributes, avoiding repetition of product details in orders.

The order_items table removes the many-to-many relationship between orders and products and ensures attributes like quantity depend on the combination of order and product.

Functional Dependencies:

customer_id → first_name, last_name, email, phone

order_id → customer_id, order_date, total_amount

product_id → product_name, price, category

This design avoids:

Update anomalies (product price updated in one place)

Insert anomalies (products/customers can exist independently)

Delete anomalies (deleting an order doesn’t remove customer data)

Thus, the schema satisfies 3NF.

3. Sample Data Representation
customers

customer_id	first_name	last_name	email
1	Rahul	Sharma	rahul@gmail.com

2	Anjali	Mehta	anjali@gmail.com

orders

order_id	customer_id	order_date	total_amount
101	            1	     2024-01-10	    2500
102	            2	       2024-01-12	1800

products


product_id	product_name	price
201	        Laptop	        50000
202	        Mouse	          800

order_items

order_item_id	order_id	product_id	quantity
1	                101	        202	        2
2	                102	        201	        1