#List of Customer names
customer_names = ["Harry", "Michael", "Jonas", "Eleven", "Cooper"]

# List of Customer orders in tuples
customer_orders = [
    ("Harry", "Laptop", 900, "Electronics"),
    ("Michael", "T-Shirt", 25, "Clothing"),
    ("Jonas", "Headphones", 80, "Electronics"),
    ("Eleven", "Shoes", 60, "Clothing"),
    ("Cooper", "Smartphone", 700, "Electronics"),
    ("Harry", "Jeans", 40, "Clothing"),
    ("Michael", "Blender", 120, "Home Essentials"),
    ("Jonas", "Coffee Maker", 75, "Home Essentials"),
    ("Eleven", "Smartwatch", 150, "Electronics"),
    ("Cooper", "Towel Set", 35, "Home Essentials"),
]

# Dictionary to store customer orders
customer_order_dict = {}

for orders in customer_orders:
    customer, product, price, category = orders
    if customer not in customer_order_dict:
        customer_order_dict[customer] = []
    customer_order_dict[customer].append((product, price, category))

print("Customer Orders")
for customer, orders in customer_order_dict.items():
    print(f"{customer} : {orders}")

# Order Classification Products to Category
products_category_dict = {}

for orders in customer_orders:
    customer, product, price, category = orders
    products_category_dict[product] = category

# Storing all the unique categories bought by the customers
unique_categories = set(products_category_dict.values())

print("\nUnique Product Categories:", unique_categories)

# Display category wise products
category_wise_products = {}

for _, product, price, category in customer_orders:
    if category not in category_wise_products:
        category_wise_products[category] = []
    category_wise_products[category].append((product))

print("\nProducts Classified by Category:")
for category, products in category_wise_products.items():
    print(f"{category}: {products}")

# # Creating a dictiory for storing the money spent by each customer
customer_order_totals = {}

for customer, orders in customer_order_dict.items():
    total_spent = sum([price for _, price, _ in orders])
    customer_order_totals[customer] = total_spent

# # Classifying customers on the basis of money spent

customer_classification = {}

for customer, total_spent in customer_order_totals.items():
    if total_spent>100:
        customer_classification[customer] = "High-Value Buyer"

    elif 50<= total_spent <= 100:
        customer_classification[customer] = "Moderate Buyer"

    else:
        customer_classification[customer] = "Low-Value Buyer"

print("\nCustomer Classification based on spending")

for customer, category in customer_classification.items():
    print(f"{customer} : {category} (Spent = {customer_order_totals[customer]})")

# Calculating total revenue per category
category_revenue = {}

for _, _, price, category in customer_orders:
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += price

print("\nTotal Sales by Product Category:")
for category, total_sales in category_revenue.items():
    print(f"{category}: ${total_sales}")

# Unique products sold

unique_products = set(products_category_dict.keys())
print("\nUnique Products Sold:", unique_products)

# Customers who purchased electronics

electronic_buyers = []

for customer, product, price, category in customer_orders:
    if category == "Electronics":
        electronic_buyers.append(customer)

print("\nCustomers Who Purchased Electronics:", electronic_buyers)

# Identifying the top 3 highest spending customers using sorting.

pairs = list(customer_order_totals.items())

sorted_pairs = sorted(pairs, key=lambda x : x[1], reverse=True)

top3_pairs = sorted_pairs[:3]
print(top3_pairs)

#  Print customer names with their total spending and classification

print("Final Customer Spending Summary:")
for customer, total_spent in customer_order_totals.items():
    print(f"{customer} spent {total_spent}, Category: {customer_classification[customer]}")

# Find customers who purchased from multiple categories

customer_category = {}

for customer, orders in customer_order_dict.items():
    customer_category[customer] = {category for product, price, category in orders}

multicategory_customer = [customer for customer, categories in customer_category.items() if len(categories)>1]

print("\nCustomers Who Purchased from Multiple Categories:", multicategory_customer)

# Find common customers who bought both Electronics and Clothing

clothing_buyers = []

for customer, product, price, category in customer_orders:
    if category == "Clothing":
        clothing_buyers.append(customer)

common_buyers = set(electronic_buyers) & set(clothing_buyers)

print("\nCustomers Who Bought Both Electronics and Clothing:", common_buyers)
