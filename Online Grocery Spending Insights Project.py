# Online Grocery Spending Insights Project
# Hello developers! Welcome to Project 3: Online Grocery Spending Insights Project! 🍎🥦

# Chef has been ordering groceries online for months and wants to understand where his money is going.
# Just like many shoppers, Chef buys items from multiple categories—Fruits, Dairy, Snacks, Vegetables, and more.

# But raw order receipts don’t tell him:

# Which category takes most of his grocery budget?
# Are his orders usually cheap or expensive?
# CHEF NEEDS YOU to turn his purchase data into visual insights!

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named grocery_orders.csv.

# It contains columns such as:
# OrderID (Unique order identifier)
# Category (Item type like Dairy, Fruits, Snacks)
# Item (Specific product name)
# Quantity (Number of units purchased)
# UnitPrice (Cost of a single unit)
# Total_Price (Final cost: Quantity × UnitPrice)
# Dataset Preview (First 5 rows):
# 101,Dairy,Milk (1L),2,1.5,3.0
# 102,Bakery,Sourdough Bread,1,3.5,3.5
# 103,Fruits,Apples (1kg),1,4.0,4.0
# 104,Vegetables,Broccoli,2,2.5,5.0
# 105,Beverages,Orange Juice,1,5.0,5.0
# Your Tasks
# Load the Grocery Orders
# Inside load_grocery_data(filename):

# Read the CSV file using Pandas.
# Return it as a DataFrame.
# Docs: pd.read_csv()
# Calculate Spending per Category
# Inside calculate_category_spending(df):

# Group rows by Category.
# Sum the Total_Price spent in each category.
# Result: This should produce a Series where the index is the Category name and the value is the total money spent.
# Docs: pandas.groupby() | groupby.sum()
# Visualize Category Share (Pie Chart)
# Inside plot_category_pie(category_totals):
# Produce a pie chart showing which category consumes the most budget.
# Figure size: Set figure size to 7 inches by 7 inches.
# Labels: Use the category names (index).
# Percentages: Display the percentage value on the slices formatted to 1 decimal place (e.g., 12.5%).
# Hint: Use the format string.
# Explode: Slightly separate the slices to create a "gap" between them.
# Hint: Create a list of 0.05 repeated for every category.
# Title: "Grocery Spending by Category".
# Save: Save as category_spending_pie_chart.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: matplotlib.pyplot.pie() | plt.title() function | matplotlib.pyplot.figure() | matplotlib.pyplot.savefig()
# Visualize Order Cost Distribution (Histogram)
# Inside plot_order_histogram(df):
# Show how expensive Chef’s typical orders are using a Histogram.
# Figure size: Set figure size to 8 inches by 5 inches.
# Data: Plot the Total_Price column.
# Bins: Number of bins should be 10.
# Colors: Bar color: "skyblue", Edge color: "black", Alpha(Transparency): 0.7.
# Labels:
# Title: "How Much Do Customers Spend? (Order Value Distribution)"
# X-label: "Total Bill Amount ($)"
# Y-label: "Number of Orders"
# Grid: Enable grid lines on the Y-axis only with alpha 0.5.
# Save: Save the plot as order_value_histogram.png.
# Docs: matplotlib.pyplot.hist() | matplotlib.pyplot.title() | matplotlib.pyplot.xlabel() | matplotlib.pyplot.ylabel() | matplotlib.pyplot.grid()
# Expected Output:
# When you run the code, your program should print the following messages and generate two image files in the same directory:

# Console Output:
# Data loaded successfully.
# Total Transactions: 55

# Spending Breakdown by Category:
# Category
# Bakery        44.1
# Beverages     59.0
# Dairy         52.0
# Fruits        55.8
# Snacks        53.4
# Vegetables    22.7
# Name: Total_Price, dtype: float64

# Generating Pie Chart...
# Pie chart saved to category_spending_pie_chart.png

# Generating Histogram...
# Histogram saved to order_value_histogram.png
# Generated Files:
# category_spending_pie_chart.pngimage
# order_value_histogram.pngimage





import pandas as pd

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

import matplotlib.pyplot as plt


# 1. Load Grocery Order Data
def load_grocery_data(filename):
    """
    Load CSV order data into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        print("Data loaded successfully.")

        # Return the DataFrame
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Calculate Category Spending Totals
def calculate_category_spending(df):
    """
    Sum total spending for each item category.
    """
    # Group by 'Category' and sum the 'Total_Price' column
    category_totals = df.groupby("Category")["Total_Price"].sum()

    # Return the resulting Series
    return category_totals


# 3. Plot Pie Chart for Category Spending Share
def plot_category_pie(category_totals):
    """
    Create and save a pie chart of category spending distribution.
    Shows which category (e.g., Dairy, Fruits) consumes the most budget.
    """

    # Set figure size to 7 inches by 7 inches
    plt.figure(figsize=(7, 7))
    
    # Create a pie chart
    plt.pie(
        # Use the values from category_totals
        category_totals.values,

        # Use the index (category names) as labels
        labels=category_totals.index,

        # Show percentage upto 1 decimal place
        autopct="%.1f%%",  

        # Slightly separate all slices
        explode=[0.05] * len(category_totals)
    )

    # Set the plot title
    plt.title("Grocery Spending by Category")
    
    # Save the plot
    output_file = "category_spending_pie_chart.png"
    plt.savefig(output_file, bbox_inches="tight")
    
    print(f"Pie chart saved to {output_file}")


# 4. Plot Histogram of Order Value
def plot_order_histogram(df):
    """
    Create and save a histogram of individual order values.
    Shows the distribution of order costs (Are most orders cheap or expensive?).
    """

    # Set figure size to 8 inches by 5 inches
    plt.figure(figsize=(8, 5))
    
    # Create a histogram for the 'Total_Price' column
    plt.hist(
        df["Total_Price"],

        # Number of bins
        bins=10,            

        # Bar color
        color="skyblue",    

        # Border color
        edgecolor="black",  

        # Transparency
        alpha=0.7           
    )
    
    # Add Title and Labels
    plt.title("How Much Do Customers Spend? (Order Value Distribution)")
    plt.xlabel("Total Bill Amount ($)")
    plt.ylabel("Number of Orders")

    # Add gridlines only to the y-axis
    plt.grid(axis="y", alpha=0.5)
    
    # Save the plot
    output_file = "order_value_histogram.png"
    plt.savefig(output_file)

    print(f"Histogram saved to {output_file}")


if __name__ == "__main__":

    # Load data
    filename = 'grocery_orders.csv'
    df = load_grocery_data(filename)

    if not df.empty:
        print(f"Total Transactions: {len(df)}")

        # 1. Analysis: Category Spending
        category_totals = calculate_category_spending(df)
        print("\nSpending Breakdown by Category:")
        print(category_totals)

        # 2. Visualization: Pie Chart
        print("\nGenerating Pie Chart...")
        plot_category_pie(category_totals)

        # 3. Visualization: Histogram
        print("\nGenerating Histogram...")
        plot_order_histogram(df)
