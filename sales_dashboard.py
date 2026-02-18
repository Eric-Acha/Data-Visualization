import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data from an excel file
df = pd.read_excel('Data/sales_performance_raw_data.xlsx')

# Convert the 'order_date' column to datetime format
df["order_date"] = pd.to_datetime(df["order_date"])     

# #Revenue by Region
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)  
plt.figure()
revenue_by_region.plot(kind="bar") 
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show() 

monthly_revenue = (
    df
    .set_index("order_date")
    .resample("M")["revenue"]
    .sum()
)

plt.figure()
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show() 

#Top 10 Products by Revenue

top_products = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

#Revenue by Category

revenue_by_category = df.groupby("category")["revenue"].sum()

plt.figure()
revenue_by_category.plot(kind="bar")
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()



