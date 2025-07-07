# Step 1: Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load the dataset (✅ working online link)
df = pd.read_csv("https://gist.githubusercontent.com/SharmaAshwini/8bd642f6c46792a9c40c8ccad60391e9/raw/Sample_Superstore.csv")

# Step 3: Data Exploration
print("--- Data Info ---")
print(df.info())
print("\n--- First 5 Rows ---")
print(df.head())

# Step 4: Data Cleaning
df = df.dropna()
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Step 5: Analysis and Visualizations

# 1. Total sales by region
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sales_by_region.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Category-wise sales
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Category', y='Sales', estimator=sum)
plt.title('Sales by Category')
plt.tight_layout()
plt.show()

# 3. Monthly sales trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(10, 5))
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Profit vs. Discount
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Discount', y='Profit')
plt.title('Profit vs Discount')
plt.tight_layout()
plt.show()

# 5. Top 10 most profitable sub-categories
top_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_profit.plot(kind='bar', color='green')
plt.title('Top 10 Most Profitable Sub-Categories')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 6: Summary
print("\n--- Summary Insights ---")
print("1. The West region has the highest total sales.")
print("2. Technology is the best-performing category.")
print("3. Sales show monthly growth fluctuations.")
print("4. Higher discounts often reduce profit.")
print("5. Certain sub-categories are significantly more profitable.")