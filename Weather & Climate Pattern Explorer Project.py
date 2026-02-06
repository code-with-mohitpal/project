# Weather & Climate Pattern Explorer Project
# Hello developers! Welcome to Project 4: Weather & Climate Pattern Explorer! 🌤️🌧️

# Chef loves travelling across different cities, but he never knows what weather to expect! He has collected temperature and humidity data from multiple cities over 10 days.

# However, looking at a raw spreadsheet is confusing. Chef needs your help to turn this data into meaningful climate insights.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with weather.csv. This dataset contains weather observations recorded over 10 days from 3 distinct Indian cities (Delhi, Mumbai, Bangalore).

# It contains the following columns:

# city: Name of the city (Delhi, Mumbai, Bangalore).
# day: Day number (1 to 10).
# temperature: Average daily temperature in Celsius.
# humidity: Average daily humidity percentage.
# Your Tasks
# Load Weather Data
# Inside load_weather_data():

# Read the dataset (weather.csv) using Pandas library.
# Print the first 5 rows to ensure it is loaded correctly.
# Docs: pd.read_csv() | df.head()
# Plot Temperature vs. Humidity (Scatter Plot)
# Inside plot_temperature_vs_humidity(df):
# We want to see if there is a correlation between heat and humidity.

# Function: We want you to use the figure-level function for this, like sns.relplot() (Relational Plot).
# Mappings:
# x: temperature
# y: humidity
# Color the points based on the city (Explore the hue parameter).
# This plot should be of scatter kind.
# Styling:
# Title: As we used the figure-level function, we have to add a "Super Title" (Temperature vs Humidity) using g.fig.suptitle() function.
# Position: Use y=1.02 to push the title slightly up.
# Save: Save as temp_vs_humid_scatter.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: sns.relplot() | plt.savefig() | Figure.suptitle()
# Plot Temperature Distribution (KDE Curve)
# Inside plot_temperature_kde(df):
# A KDE (Kernel Density Estimate) is like a smooth histogram. It shows us the "shape" of the temperature data.

# Function: We want you to use the axes-level function for this, like sns.kdeplot().
# Mappings:
# x: temperature
# Draw a separate curve for each city (Explore the hue parameter).
# Shade the area under the curve (Explore the fill parameter).
# Styling:
# Set figure size to 10 inches by 6 inches.
# Add Title: "Temperature Distribution (KDE)".
# Add Grid: Add a grid with transparency set to 0.3 (Explore the alpha parameter).
# Save the plot as temperature_kde.png.
# Docs: sns.kdeplot() | plt.figure() | plt.title() | plt.grid()
# Faceted Plot by City
# Inside plot_faceted_distribution(df):
# Sometimes, plotting everything on one chart is messy. Faceting splits the data into separate charts.
# Function: We want you to use the figure-level function for this, like sns.displot() (Distribution Plot).
# Mappings:
# x: temperature
# Faceting: Create a separate chart for each city (Explore the col parameter).
# Set the kind of plot to "kde".
# Shade the area under the curve (Explore the fill parameter).
# Styling:
# Title: As we used the figure-level function, we have to add a "Super Title" (Faceted Temperature Distributions) using g.fig.suptitle() function.
# Position: Use y=1.03 to push the title slightly up.
# Save: Save as temperature_facets.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: sns.displot() | Figure.suptitle() | plt.savefig()
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# Weather & Climate Pattern Explorer...

# Dataset Preview:
#     city  day  temperature  humidity
# 0  Delhi    1           32        48
# 1  Delhi    2           34        52
# 2  Delhi    3           33        45
# 3  Delhi    4           35        50
# 4  Delhi    5           36        54
# Chart saved: temp_vs_humid_scatter.png
# Chart saved: temperature_kde.png
# Chart saved: temperature_facets.png
# Generated Files:
# temp_vs_humid_scatter.pngimage
# temperature_kde.pngimage
# temperature_facets.pngimage







import pandas as pd
import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt


# 1. Load Dataset
def load_weather_data():
    """
    Load and return the weather dataset.
    """
    df = pd.read_csv("weather.csv")
    
    print("Dataset Preview:")
    print(df.head())

    return df


# 2. Scatter Plot: Temperature vs Humidity
def plot_temperature_vs_humidity(df):
    """
    Compare temperature vs humidity using a relational plot.
    """
    g = sns.relplot(
        data=df,
        x="temperature",
        y="humidity",
        hue="city",
        kind="scatter"
    )

    # Super Title
    g.fig.suptitle("Temperature vs Humidity", y=1.02)

    # Save plot
    plt.savefig("temp_vs_humid_scatter.png", bbox_inches="tight")

    print("Chart saved: temp_vs_humid_scatter.png")


# 3. Distribution Chart: KDE Curve
def plot_temperature_kde(df):
    """
    Plot smooth temperature distributions.
    """
    plt.figure(figsize=(10, 6))

    sns.kdeplot(
        data=df,
        x="temperature",
        hue="city",
        fill=True
    )

    plt.title("Temperature Distribution (KDE)")
    plt.grid(alpha=0.3)

    plt.savefig("temperature_kde.png")

    print("Chart saved: temperature_kde.png")


# 4. Faceted Distribution Plot (Side-by-Side)
def plot_faceted_distribution(df):
    """
    Create separate charts for each city side-by-side.
    """
    g = sns.displot(
        data=df,
        x="temperature",
        col="city",
        kind="kde",
        fill=True
    )

    g.fig.suptitle("Faceted Temperature Distributions", y=1.03)

    plt.savefig("temperature_facets.png", bbox_inches="tight")

    print("Chart saved: temperature_facets.png")


if __name__ == "__main__":
    print("Weather & Climate Pattern Explorer...\n")

    # 1. Load Data
    df = load_weather_data()

    if df is not None:
        # 2. Scatter Plot
        plot_temperature_vs_humidity(df)

        # 3. KDE Plot
        plot_temperature_kde(df)

        # 4. Faceted Plot
        plot_faceted_distribution(df)
