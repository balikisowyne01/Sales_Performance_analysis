import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

products = np.array([
    "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet"
])

regions = np.array([
    "West", "East", "North", "South", "West", "East", "North", "South", "West", "East", "North", "South"
])

months = np.array([
    "January", "January", "January", "February", "February", "February", "March", "March", "March", "April", "April", "April"
])

quantity = np.array([
    2, 5, 3, 1, 4, 2, 3, 6, 4, 2, 3, 5
])

unit_price = np.array([
    750, 300, 250, 750, 300, 250, 750, 300, 250, 750, 300, 250
])

unit_cost = np.array([
    600, 220, 180, 600, 220, 180, 600, 220, 180, 600, 220, 180
])


df = pd.DataFrame({
    "Products": products,
    "Regions": regions,
    "Months": months,
    "Quantity": quantity,
    "Unit_Price": unit_price,
    "Unit_Cost": unit_cost
                })
df.to_csv("data/sales_data.csv", index=False)

# Calculate revenue for each transaction

revenue = quantity * unit_price
print("Individual Sales Revenue:")
print(revenue)

# Calculate cost for each transaction

cost = quantity * unit_cost
print("Individual Sales cost:")
print(cost)

# Calculate profit for each transaction

profit = revenue - cost
print("Individual Sales profit:")
print(profit)

# Calculate total revenue , total cost and total profit

total_revenue = np.sum(revenue)
total_cost = np.sum(cost)
total_profit = np.sum(profit)
print(f"\nTotal Revenue: ${total_revenue:.2f}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Total profit: ${total_profit:.2f}\n")


# Get all unique products

unique_products = np.unique(products)
product_revenues = []
for product in unique_products:
# Select transactions belonging to a product
    product_mask = products == product
# Calculate total revenue for the product
    product_total = np.sum(revenue[product_mask])
    product_revenues.append(product_total)

    print(f"{product}: {product_total:,.2f}")

# Identify the best-performing product
best_product_index = np.argmax(product_revenues)
best_product = unique_products[best_product_index]
print(f"Best Selling Product by Revenue: {best_product}\n")


# Get unique months

unique_months = np.unique(months)

monthly_revenues = []

for month in unique_months:

    month_mask = months == month

    month_total = np.sum(revenue[month_mask])

    monthly_revenues.append(month_total)

    print(f"{month}: {month_total:,.2f}")

# Identify the month with highest revenue

best_month_index = np.argmax(monthly_revenues)

best_month = unique_months[best_month_index]

print(f"Best Performing Month: {best_month}\n")
# get unique months

unique_regions = np.unique(regions)

regional_revenues = []

for region in unique_regions:

    region_mask = regions == region

    region_total = np.sum(revenue[region_mask])

    regional_revenues.append(region_total)

    print(f"{region}: {region_total:,.2f}")

# Find the highest-performing region

best_region_index = np.argmax(regional_revenues)

best_region = unique_regions[best_region_index]

print(f"Best Performing Region: {best_region}\n")

average_sales = np.mean(revenue)

highest_sale = np.max(revenue)

lowest_sale = np.min(revenue)

print(f"Average Sales: {average_sales:,.2f}")
print(f"Highest Sale: {highest_sale:,.2f}")
print(f"Lowest Sale: {lowest_sale:,.2f}\n")

# Analyze profit for each product

unique_products = np.unique(products)

product_profits = []

for product in unique_products:
    product_mask = products == product

    # Calculate total profit for each product
    product_total_profit = np.sum(profit[product_mask])

    product_profits.append(product_total_profit)

    print(f"{product} profit: {product_total_profit:,.2f}")

# Identify the most profitable product

best_profit_index = np.argmax(product_profits)

most_profitable_product = unique_products[best_profit_index]

print(f"Most Profitable Product: {most_profitable_product}\n")


# Create a Pandas DataFrame

sales_df = pd.DataFrame({
    "Product": products,
    "Region": regions,
    "Month": months,
    "Quantity": quantity,
    "Unit_Price": unit_price,
    "Unit_Cost": unit_cost,
    "Revenue": revenue,
    "Total_Cost": cost,
    "Profit": profit
})

print(f"{sales_df.to_string()}\n")

product_analysis = sales_df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Total_Profit=("Profit", "sum")
)

print(product_analysis)
# sales_df.to_csv("data/sales_analysis.csv", index=False)

# print("Sales analysis saved successfully!")

# Overall business performance

total_revenue = sales_df["Revenue"].sum()
total_cost = sales_df["Total_Cost"].sum()
total_profit = sales_df["Profit"].sum()
total_quantity = sales_df["Quantity"].sum()

average_revenue = sales_df["Revenue"].mean()

print("\n SALES PERFORMANCE SUMMARY")
print("--------------------------")

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Transaction Revenue: ${average_revenue:,.2f}\n")


Path("visualizations").mkdir(exist_ok=True)

# Revenue by Product
product_revenue = sales_df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
plt.bar(product_revenue.index, product_revenue.values)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("visualizations/revenue_by_product.png", dpi=300)
plt.show()


# Monthly Revenue Trend
month_order = ["January", "February", "March", "April"]

monthly_revenue = (
    sales_df.groupby("Month")["Revenue"]
    .sum()
    .reindex(month_order)
)

plt.figure(figsize=(8, 5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("visualizations/monthly_revenue.png", dpi=300)
plt.show()


# Profit by Product
product_profit = sales_df.groupby("Product")["Profit"].sum()

plt.figure(figsize=(8, 5))
plt.barh(product_profit.index, product_profit.values)
plt.title("Profit by Product")
plt.xlabel("Profit")
plt.tight_layout()
plt.savefig("visualizations/profit_by_product.png", dpi=300)
plt.show()


# Revenue by Region
regional_revenue = sales_df.groupby("Region")["Revenue"].sum()

plt.figure(figsize=(7, 7))
plt.pie(
    regional_revenue.values,
    labels=regional_revenue.index,
    autopct="%1.1f%%"
)
plt.title("Revenue Contribution by Region")
plt.tight_layout()
plt.savefig("visualizations/revenue_by_region.png", dpi=300)
plt.show()
