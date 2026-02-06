# Customer Purchase Insights Project
# Hello developers! Welcome to Project 5: Customer Purchase Insights! 🛍📊

# Chef runs a growing retail shop that sells electronics items! However, his sales records are messy. 😵‍💫

# Some entries are incomplete, some contain missing values, and he has no quick way to understand:

# Which customers spend the most?
# Which product sells the fastest?
# How much revenue is actually being generated?
# Your task is to transform these raw transaction logs into meaningful business insights!💡

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic.
# Do NOT change function names or print statements.
# Dataset
# You will work with retail_store_sales.csv. It contains transaction records.

# It contains the following columns:

# Transaction_ID: Unique ID for the order
# Customer_ID: Unique ID for the customer
# Item: Name of the product purchased
# Price_Per_Unit: Cost of one unit ($)
# Quantity: Number of units purchased
# Your Tasks
# Load the Dataset
# Inside load_sales_data():

# Read the dataset (retail_store_sales.csv).
# Print a preview of the first 5 records to check if it loaded correctly.
# Docs: pd.read_csv() | df.head()
# Clean the Data
# Inside clean_data(df): Real-world data is rarely perfect. We need to handle missing values.

# Drop Invalid Rows:
# Remove rows where Customer_ID is missing.
# Crucial: Use .copy() after dropping to avoid the "SettingWithCopyWarning".
# Impute Missing Values: Fill missing Quantity and Price_Per_Unit with their median values (this is more robust than using the average).
# Print the count of dropped rows.
# Docs: df.dropna() | df.fillna()
# Feature Engineering
# Inside add_total_price(df):
# We need to calculate the total value of each order.
# Create a new column Total_Amount by multiplying Price_Per_Unit and Quantity.
# NumPy Matrix Analysis
# Inside perform_numpy_analysis(df):
# Convert: Select the numerical columns (Price, Quantity, Total) and convert them to a NumPy array.
# Aggregate: Calculate the Max and Mean along the columns.
# Print: Display these four values:
# Max Price (up to 2 decimal places)
# Max Quantity
# Max Total Order Value (up to 2 decimal places)
# Average Order Value (up to 2 decimal places)
# Docs: df.to_numpy() | np.max() | np.mean()
# Business Insights
# Inside analyze_statistics(df):
# Calculate:
# Total Revenue: Sum of Total_Amount (up to 2 decimal places).
# Average Order Value: Average of Total_Amount (up to 2 decimal places).
# Top Customer: Find which Customer_ID has the highest total spending.
# Top Item: Find which Item has the highest total Quantity sold.
# Return these results as a dictionary.
# Docs: df.groupby() | df.idxmax() | df.sum() | df.mean()
# Expected Output:

# Customer Purchase Insights...

# Dataset Preview:
#    Transaction_ID Customer_ID                 Item  Price_Per_Unit  Quantity
# 0            1001        C001       Wireless Mouse            25.0       2.0
# 1            1002        C002  Mechanical Keyboard            85.0       1.0
# 2            1003         NaN            USB Cable            12.0       5.0
# 3            1004        C003              Monitor             NaN       2.0
# 4            1005        C001           HDMI Cable            15.0       NaN
# Cleaning Data:
# Rows dropped (Missing ID): 5
# Missing values in Price/Quantity filled with Median.

# Added 'Total_Amount' column.

# NumPy Matrix Analysis:
# Matrix Shape: (20, 3)
# Max Price: $300.00
# Max Quantity in one order: 10
# Max Total Order Value: $300.00
# Avg Order Value: $90.50

# Customer Insights:
# Total Store Revenue: $1810.00
# Average Order Value: $90.50
# Top Spending Customer: C003
# Most Popular Item: USB Cable




import pandas as pd
import numpy as np


# 1. Load Dataset
def load_sales_data():
    """
    Load and return the raw sales dataset.
    """
    path = "retail_store_sales.csv"
    try:
        df = pd.read_csv(path)
        print("Dataset Preview:")

        # Print the first 5 rows of the dataframe
        print(df.head())

        return df
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        return None


# 2. Clean Data (Handle Missing Values)
def clean_data(df):
    """
    Clean missing values and remove invalid rows.
    """
    print("Cleaning Data:")
    
    # Calculate initial rows 
    initial_rows = len(df)

    # Drop rows where Customer_ID is missing
    df = df.dropna(subset=["Customer_ID"]).copy()
    
    # Fill missing Quantity with median
    df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
    
    # Fill missing Price_Per_Unit with median
    df["Price_Per_Unit"] = df["Price_Per_Unit"].fillna(df["Price_Per_Unit"].median())

    # Calculate total rows dropped
    dropped_count = initial_rows - len(df)

    print(f"Rows dropped (Missing ID): {dropped_count}")
    print("Missing values in Price/Quantity filled with Median.\n")
    
    return df


# 3. Feature Engineering
def add_total_price(df):
    """
    Add new column: Total Purchase Amount = Price x Quantity
    """
    df["Total_Amount"] = df["Price_Per_Unit"] * df["Quantity"]
    
    print("Added 'Total_Amount' column.\n")
    return df


# 4. NumPy Matrix Operations
def perform_numpy_analysis(df):
    """
    Convert numeric data to NumPy matrix and perform axis-based aggregations.
    """
    print("NumPy Matrix Analysis:")

    num_cols = df[["Price_Per_Unit", "Quantity", "Total_Amount"]]
    
    # Convert dataframe to NumPy array
    matrix = num_cols.to_numpy()

    # Print shape
    print(f"Matrix Shape: {matrix.shape}")

    # Column-wise max and mean
    max_values = np.max(matrix, axis=0)
    mean_values = np.mean(matrix, axis=0)

    print(f"Max Price: ${max_values[0]:.2f}")
    print(f"Max Quantity in one order: {int(max_values[1])}")
    print(f"Max Total Order Value: ${max_values[2]:.2f}")
    print(f"Avg Order Value: ${mean_values[2]:.2f}\n")
    
    return matrix


# 5. Customer Insights 
def analyze_statistics(df):
    """
    Generate purchase insights using GroupBy.
    """
    print("Customer Insights:")

    # Total revenue
    total_revenue = df["Total_Amount"].sum()

    # Average order value
    avg_spent = df["Total_Amount"].mean()
    
    # Top spending customer
    best_customer = (
        df.groupby("Customer_ID")["Total_Amount"]
        .sum()
        .idxmax()
    )
    
    # Most popular item
    top_item = (
        df.groupby("Item")["Quantity"]
        .sum()
        .idxmax()
    )

    print(f"Total Store Revenue: ${total_revenue:.2f}")
    print(f"Average Order Value: ${avg_spent:.2f}")
    print(f"Top Spending Customer: {best_customer}")
    print(f"Most Popular Item: {top_item}\n")

    return {
        "total_revenue": total_revenue,
        "avg_spent": avg_spent,
        "best_customer": best_customer,
        "top_item": top_item
    }


if __name__ == "__main__":
    print("Customer Purchase Insights...\n")

    # 1. Load
    df = load_sales_data()

    if df is not None:
        # 2. Clean
        df = clean_data(df)

        # 3. Feature Engineering
        df = add_total_price(df)

        # 4. NumPy Analysis
        perform_numpy_analysis(df)

        # 5. Business Insights
        analyze_statistics(df)
