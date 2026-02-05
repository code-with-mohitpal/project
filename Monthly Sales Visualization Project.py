# Monthly Sales Visualization Project
# Hello developers! Welcome to Project 3: Monthly Sales Visualization! 📈📊

# Chef has just opened a new restaurant chain and wants to track how the business is performing throughout the year 🍝
# He has the raw sales numbers for every month, but a list of numbers is hard to read. He needs you to build a visualization tool that converts this data into clear charts and graphs.

# Your task is to use Matplotlib Library to generate:

# A Line Chart to show the growth trend.
# A Bar Chart to compare months side-by-side.
# Important Notes

# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# Do NOT change function names: The testing system relies on them.
# Dataset
# You will need to manually enter this data inside the load_sales_data() function:

# Months: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
# Sales ($): 12000, 15000, 17000, 16000, 18000, 20000, 22000, 21000, 19000, 23000, 25000, 27000
# Your Tasks
# Open main.py and complete the logic inside the functions.

# Load Monthly Sales Data
# Inside load_sales_data():
# Create a list of strings for the 12 months.
# Create a list of integers for the 12 sales values.
# Return both lists so they can be used by the plotting functions.
# Visualize Sales Trend (Line Chart)
# Inside plot_sales_trend(months, sales):
# Set the figure size to (10, 6).
# Plot a Line Chart with:
# Color: Blue ('b')
# Marker: Circle ('o')
# Line Style: Solid ('-')
# Line Width: 2
# Label: "Monthly Sales" (Required for the legend).
# Add the title: "Monthly Sales Trend (2025)"
# Add labels: X-axis = "Month", Y-axis = "Sales Amount ($)"
# Enable the Grid and show the Legend.
# Save the plot as sales_trend.png.
# Docs: plt.figure() function, plt.plot() function, plt.title() function, plt.xlabel() Documentation, plt.ylabel() function, plt.grid() function, plt.legend() function, plt.savefig() function
# Compare Monthly Sales (Bar Chart)
# Inside plot_sales_bar_chart(months, sales):
# Set the figure size to (10, 6).
# Plot a Bar Chart with:
# Color: Orange
# Label: "Monthly Sales" (Required for the legend).
# Add the title: "Monthly Sales Comparison"
# Add labels: X-axis = "Month", Y-axis = "Sales Amount ($)"
# Enable the Grid and show the Legend.
# Save the plot as sales_bar_chart.png.
# Docs: plt.figure() function, plt.bar() function, plt.title() function, plt.xlabel() Documentation, plt.ylabel() function, plt.grid() function, plt.legend() function, plt.savefig() function
# Expected Output:
# When you run the code, your program should print the following messages and generate two image files in the same directory:

# Console Output:
# Monthly Sales Visualization Project

# Chart saved: sales_trend.png
# Chart saved: sales_bar_chart.png
# Generated Files:
# sales_trend.pngimage
# sales_bar_chart.pngimage



import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt


# 1. Load Data
def load_sales_data():
    """
    Returns lists of months and sales figures.
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    sales = [12000, 15000, 17000, 16000, 18000, 20000,
             22000, 21000, 19000, 23000, 25000, 27000]

    return months, sales


# 2. Line Plot (Trend)
def plot_sales_trend(months, sales):
    """
    Create a line chart and save it to a file.
    """
    plt.figure(figsize=(10, 6))

    plt.plot(
        months,
        sales,
        color="b",
        marker="o",
        linestyle="-",
        linewidth=2,
        label="Monthly Sales"
    )

    plt.title("Monthly Sales Trend (2025)")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")

    plt.grid(True)
    plt.legend()

    plt.savefig("sales_trend.png")

    print("Chart saved: sales_trend.png")


# 3. Bar Chart (Comparison)
def plot_sales_bar_chart(months, sales):
    """
    Create a bar chart and save it to a file.
    """
    plt.figure(figsize=(10, 6))

    plt.bar(
        months,
        sales,
        color="orange",
        label="Monthly Sales"
    )

    plt.title("Monthly Sales Comparison")
    plt.xlabel("Month")
    plt.ylabel("Sales Amount ($)")

    plt.grid(True)
    plt.legend()

    plt.savefig("sales_bar_chart.png")

    print("Chart saved: sales_bar_chart.png")


if __name__ == "__main__":
    print("Monthly Sales Visualization Project\n")

    months, sales = load_sales_data()

    plot_sales_trend(months, sales)
    plot_sales_bar_chart(months, sales)
