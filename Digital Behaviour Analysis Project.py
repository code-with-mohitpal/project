# Digital Behaviour Analysis Project
# Hello developers! Welcome to Project 3: Digital Behaviour Analysis Project! 📊📱

# In today’s digital world, our smartphones quietly track how we spend our time - from screen usage to app activity and phone unlocks.

# Chef has collected daily digital behaviour data to better understand his phone habits.
# But raw numbers alone don’t reveal much insight.

# Chef wants answers like:

# How does his daily screen time change over time?
# Is he crossing his daily usage limit?
# Chef needs your help to transform this data into meaningful visual insights using Matplotlib library.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named digital_behaviour.csv:

# It contains columns such as:
# Date → Day of observation (YYYY-MM-DD)
# ScreenTime → Total screen time in hours
# AppUsage → Time spent actively using apps (in hours)
# Unlocks → Number of times the phone was unlocked
# Dataset Preview (First 5 rows):
# Date,ScreenTime,AppUsage,Unlocks
# 2024-01-01,8.24,6.85,49
# 2024-01-02,6.65,4.64,125
# 2024-01-03,8.62,8.05,70
# 2024-01-04,10.81,9.28,100
# 2024-01-05,6.41,5.09,48
# Tasks
# Load Digital Behaviour Data
# Inside load_data(filename):

# Read the CSV file using Pandas
# Convert the Date column into datetime objects
# Sort the dataset by date (chronological order)
# Return the cleaned DataFrame
# Why sorting is important?
# When creating a line plot, data must be in correct time order. If dates are not sorted, the line graph may jump back and forth, making the trend confusing and hard to read.
# Docs: pandas.read_csv | pandas.to_datetime | pandas.DataFrame.sort_values
# Create a Multi-Plot Layout
# Inside visualize_digital_behavior(df):

# Create 1 row × 2 column subplot layout
# Figure size must be 15 × 5 inches
# Add a main title: "Project 3: Digital Behaviour Analysis"
# Docs: matplotlib.pyplot.subplots | matplotlib.figure.Figure.suptitle
# Plot 1 — Daily Usage Trends (Line Chart)
# On the left subplot (ax1), visualize how usage changes over time:
# Line 1: Plot Screen Time vs Date. Label it "Screen Time".
# Line 2: Plot App Usage vs Date. Label it "App Usage" and make it a dashed line.
# Limit line: Add a horizontal line to show the daily limit.
# Value: 6.0 hours
# Color: red
# Dashed style
# Label: "Daily Limit"
# Styling:
# Title: Daily Usage Trends
# X-label: Date
# Y-label: Hours
# Enable the Legend
# Rotate the date labels on the X-axis by 45 degrees.
# Docs: matplotlib.axes.Axes.plot | matplotlib.axes.Axes.axhline | matplotlib.axes.Axes.set_title | matplotlib.axes.Axes.legend | matplotlib.axes.Axes.tick_params
# Plot 2 — Usage Correlation (Scatter Plot)
# On the right subplot (ax2), see if unlocks affect screen time:
# Create a Scatter Plot:
# X-axis → Unlocks
# Y-axis → Screen Time
# Color mapping → App Usage (Points are colored based on how much the apps were used)
# Colormap → viridis
# Transparency(alpha) → 0.7
# Styling:
# Title: Unlocks vs. Screen Time
# X-label: Unlocks
# Y-label: Screen Time
# Colorbar:
# Since color represents App Usage, you must add a colorbar.
# Requirements:
# Attach the colorbar to the scatter plot
# Label it: "App Usage (Hours)"
# Docs: matplotlib.axes.Axes.scatter | matplotlib.pyplot.colorbar
# Save the Final Visualization
# Adjust the spacing using plt.tight_layout().
# Save the figure as a PNG file named: "digital_behaviour_analysis.png"
# Docs: matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
# Expected Output:
# When you run the code, your program should print the following messages and generate an image file in the same directory:

# Console Output:
# Plot saved as 'digital_behaviour_analysis.png'
# Generated Files:
# digital_behaviour_analysis.pngimage


# import pandas as pd

# import matplotlib
# matplotlib.use("Agg") # Headless mode for saving files

# import matplotlib.pyplot as plt

# # Constants
# FILE_NAME = "digital_behaviour.csv"
# DAILY_LIMIT = 6.0

# def load_data(filename):
#     """
#     Load data and convert Date column.
#     """
#     try:
#         # TODO: Read the CSV file into a DataFrame
#         df = __________

#         # TODO: Convert the 'Date' column to datetime objects
#         df['Date'] = __________
        
#         # TODO: Sort the DataFrame by 'Date' and return the sorted DataFrame
#         return __________
        
#     except FileNotFoundError:
#         print("Error: File not found.")
#         return pd.DataFrame()
    

# def visualize_digital_behavior(df):
#     """
#     Create a side-by-side plot layout.
#     """

#     # 1. Setup Subplots in 1 Row and 2 Columns
#     # TODO: Create a subplot with 1 row and 2 columns
#     # Set the figure size to 15 inches by 5 inches
#     fig, axes = plt.subplots(__________, __________, __________)

#     # Assigning axes to variables for easier use
#     ax1 = axes[0] # Axis for Plot 1
#     ax2 = axes[1] # Axis for Plot 2

#     # TODO: Add a main title for the entire figure
#     # Main Title: "Project 3: Digital Behaviour Analysis"
#     __________

#     # === PLOT 1: Daily Trends (Line Plot) ===
#     # TODO: Plot 'Date' on X-axis and 'ScreenTime' on Y-axis
#     # Add label 'Screen Time'
#     __________

#     # Now plot another line for 'AppUsage' 
#     # TODO: Plot 'Date' on X-axis and 'AppUsage' on Y-axis
#     # Make this line dashed and add label 'App Usage'
#     __________

#     # TODO: Add a horizontal line for the daily limit
#     # Use y=DAILY_LIMIT, color='red' and make this line dashed
#     # Label it 'Daily Limit'
#     __________

#     # Labels
#     # TODO: Add a title to ax1 "Daily Usage Trends"
#     __________

#     # TODO: Add X axis label 'Date' and Y axis label 'Hours'
#     __________
#     __________

#     # TODO: Add a legend to axis ax1
#     __________
    
#     # TODO: Rotate date labels by 45 degrees for better readability
#     __________

#     # === PLOT 2: Correlations (Scatter with Color Map) ===
#     # TODO: Create a scatter plot on axis ax2
#     # x = 'Unlocks', y = 'ScreenTime'
#     # This maps color to App Usage
#     # Set colormap to 'viridis'
#     # Set transparency to 0.7 (Explore alpha parameter)
#     scatter = ax2.scatter(
#         __________,
#         __________, 
#         __________, 
#         __________,
#         __________
#     )

#     # Labels
#     # TODO: Add title to ax2 "Unlocks vs. Screen Time"
#     __________

#     # TODO: Add X axis label 'Unlocks' and Y axis label 'Screen Time'
#     __________
#     __________

#     # TODO: Add a Colorbar to explain the colors
#     # Pass the 'scatter' object and the axis 'ax2'
#     # Set the label to 'App Usage (Hours)'
#     __________

#     # TODO: Adjust layout using tight_layout function and save the figure as a PNG file (digital_behaviour_analysis.png)
#     __________
#     __________

#     print("Plot saved as 'digital_behaviour_analysis.png'")

# if __name__ == "__main__":
#     df = load_data(FILE_NAME)






import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

FILE_NAME = "digital_behaviour.csv"
DAILY_LIMIT = 6.0


def load_data(filename):
    try:
        df = pd.read_csv(filename)
        df['Date'] = pd.to_datetime(df['Date'])
        return df.sort_values("Date")
    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()


def visualize_digital_behavior(df):

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    ax1 = axes[0]
    ax2 = axes[1]

    fig.suptitle("Project 3: Digital Behaviour Analysis")

    ax1.plot(df['Date'], df['ScreenTime'], label="Screen Time")
    ax1.plot(df['Date'], df['AppUsage'], linestyle="--", label="App Usage")
    ax1.axhline(y=DAILY_LIMIT, color="red", linestyle="--", label="Daily Limit")

    ax1.set_title("Daily Usage Trends")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Hours")
    ax1.legend()
    ax1.tick_params(axis='x', rotation=45)

    scatter = ax2.scatter(
        df['Unlocks'],
        df['ScreenTime'],
        c=df['AppUsage'],
        cmap='viridis',
        alpha=0.7
    )

    ax2.set_title("Unlocks vs. Screen Time")
    ax2.set_xlabel("Unlocks")
    ax2.set_ylabel("Screen Time")

    plt.colorbar(scatter, ax=ax2, label="App Usage (Hours)")

    plt.tight_layout()
    plt.savefig("digital_behaviour_analysis.png")

    print("Plot saved as 'digital_behaviour_analysis.png'")


if __name__ == "__main__":
    df = load_data(FILE_NAME)
    
    if not df.empty:
        visualize_digital_behavior(df)
    
#     if not df.empty:
#         visualize_digital_behavior(df)


