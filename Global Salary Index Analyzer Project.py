# Global Salary Index Analyzer Project
# Hello developers! Welcome to Project 6: Global Salary Index Analyzer! 💼📊

# Chef is curious to understand how salaries vary around the world. He collected employee data from multiple countries - including experience, job roles, and salary figures. But staring at spreadsheets is confusing! 😵

# Chef needs your help to visualize the data and uncover meaningful global salary trends using Seaborn and Matplotlib.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with global_salaries.csv. This dataset helps us compare remote vs onsite work across skills, experience, and geography.

# It contains the following columns:

# country: Country where the employee works
# job_role: Type of role (Developer, Data Scientist, etc.)
# experience_years: Work experience in years
# salary_remote: Average remote salary (USD)
# salary_onsite: Average onsite salary (USD)
# remote_ratio: Percentage of work done remotely (0-100)
# Your Tasks
# Compare Remote vs Onsite Salaries (Bar Chart)
# Inside plot_salary_comparison(df):
# We want to compare two values (remote vs onsite) for each country side-by-side. To do this with Seaborn, we first need to reshape our data.
# Reshape: Convert the DataFrame into "long format" using df.melt() and assign it to df_long.
# id_vars: The column to keep fixed (hint: we are comparing countries).
# value_vars: The two columns containing the numerical data we want to stack.
# var_name: Name the new category column "salary_type".
# value_name: Name the new value column "amount".
# Plot: Create a side-by-side bar chart using sns.barplot().
# Mappings:
# x: country
# y: amount
# Color the bars based on the salary type (Explore the hue parameter).
# Styling:
# Set figure size to 12 inches by 6 inches.
# Use the color palette: ["#e74c3c", "#2c3e50"].
# Disable the error bars.
# Add Title: "Average Salary Comparison: Remote vs Onsite".
# Add X-label "Country" and Y-label "Avg Salary (USD)".
# Add a grid to the Y-axis with transparency set to 0.3 (Explore the alpha parameter).
# Save the plot as salary_comparison.png.
# Use bbox_inches='tight' to avoid cutting off labels.
# Docs: df.melt() | sns.barplot() | plt.savefig() | plt.figure() | plt.title() | plt.grid()
# Analyze Experience vs Remote Salary (Scatter Plot)
# Inside plot_salary_vs_experience(df):
# Let's see if experience pays off! We also want to visualize how much "remote work" each data point represents.
# Plot: Create a scatter plot using plt.scatter() and assign it to scatter.
# Mappings:
# x: experience_years
# y: salary_remote
# Bubble Size should represent remote_ratio (scale it by multiplying by 5 for visibility).
# Styling:
# Set figure size to 10 inches by 6 inches.
# Set point transparency to 0.7 (Explore the alpha parameter).
# Add a black outline to the bubbles (Explore the edgecolors parameter).
# Add Title: "Experience vs Remote Salary (Size = Remote Ratio)".
# Add X-label "Years of Experience" and Y-label "Remote Salary (USD)".
# Add a grid with transparency set to 0.3 (Explore the alpha parameter).
# Save the plot as "salary_experience_scatter.png".
# Use bbox_inches='tight' to avoid cutting off labels.
# Docs: plt.scatter() | plt.savefig() | plt.figure() | plt.title() | plt.grid()
# Salary Distribution by Role (KDE Plot)
# Inside plot_salary_kde(df):
# Let's use a KDE (Kernel Density Estimate) to visualize the "shape" of salary distributions. Are they spread out or clustered?
# Plot: Create a density plot using sns.kdeplot().
# Mappings:
# x: salary_onsite
# Draw a separate curve for each job role (Explore the hue parameter).
# Shade the area under the curves (Explore the fill parameter).
# Styling:
# Set figure size to 10 inches by 6 inches.
# Set transparency to 0.4 (Explore the alpha parameter).
# Add Title: "Salary Distribution by Job Role (KDE)".
# Add X-label "Onsite Salary (USD)".
# Add a grid with transparency set to 0.3 (Explore the alpha parameter).
# Save the plot as salary_kde.png.
# Use bbox_inches='tight' to avoid cutting off labels.
# Docs: sns.kdeplot() | plt.savefig() | plt.figure() | plt.title() | plt.grid()
# Role-Based Faceted Salary Trends (Relational Plot)
# Inside plot_faceted_relplot(df):
# Instead of one messy chart, let's create a separate chart for each job role automatically!
# Plot: Use Seaborn's figure-level function sns.relplot() and assign the result to variable g.
# Mappings:
# x: experience_years
# y: salary_onsite
# Color the points based on the country (Explore the hue parameter).
# Create a separate chart for each job role (Explore the col parameter).
# This plot should be of scatter kind (Explore the kind parameter).
# Styling:
# Add a Super Title to the entire figure: "Global Salary Trends by Role & Experience".
# Push the title up slightly (Explore the y parameter in suptitle, try 1.03).
# Save the plot as faceted_salary_roles.png.
# Use bbox_inches='tight' to avoid cutting off labels.
# Docs: sns.relplot() | Figure.suptitle() | plt.savefig()
# Expected Output:
# When you run the code, your program should print the following messages and generate 4 image files in the same directory:

# Console Output:
# Global Salary Index Analyzer Project...

# Plotting Salary Comparison...
# Melted DataFrame Preview:
#          country    salary_type  amount
# 0  United States  salary_remote   95000
# 1  United States  salary_remote  125000
# 2  United States  salary_remote  135000
# 3  United States  salary_remote  165000
# 4  United States  salary_remote  155000
# Chart saved: salary_comparison.png
# Plotting Salary vs Experience...
# Chart saved: salary_experience_scatter.png
# Plotting Salary Density (KDE)...
# Chart saved: salary_kde.png
# Plotting Faceted Role Trends...
# Chart saved: faceted_salary_roles.png
# Generated Files:
# salary_comparison.pngimage
# salary_experience_scatter.pngimage
# salary_kde.pngimage
# faceted_salary_roles.pngimage




import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files


# 1. Bar Chart - Compare Avg Salary by Country (Side-by-Side Bars)
def plot_salary_comparison(df):
    """
    Create a side-by-side bar chart comparing onsite vs remote salaries.
    Using MELT to reshape data for plotting.
    """
    print("Plotting Salary Comparison...")

    # Melt dataframe to long format
    df_long = df.melt(
        id_vars="country",
        value_vars=["salary_remote", "salary_onsite"],
        var_name="salary_type",
        value_name="amount"
    )

    print("Melted DataFrame Preview:")
    print(df_long.head())

    # Set figure size
    plt.figure(figsize=(12, 6))

    # Bar plot
    sns.barplot(
        data=df_long,
        x="country",
        y="amount",
        hue="salary_type",
        palette=["#e74c3c", "#2c3e50"],
        errorbar=None
    )

    # Titles and labels
    plt.title("Average Salary Comparison: Remote vs Onsite")
    plt.xlabel("Country")
    plt.ylabel("Avg Salary (USD)")

    # Grid (Y-axis only)
    plt.grid(axis="y", alpha=0.3)

    # Save plot
    plt.savefig("salary_comparison.png", bbox_inches="tight")

    print("Chart saved: salary_comparison.png")
    return df_long


# 2. Scatter Plot - Multi-variable
def plot_salary_vs_experience(df):
    """
    Scatter plot with semantic mapping.
    """
    print("Plotting Salary vs Experience...")

    # Set figure size
    fig = plt.figure(figsize=(10, 6))

    # Scatter plot
    plt.scatter(
        df["experience_years"],
        df["salary_remote"],
        s=df["remote_ratio"] * 5,
        alpha=0.7,
        edgecolors="black"
    )

    plt.title("Experience vs Remote Salary (Size = Remote Ratio)")
    plt.xlabel("Years of Experience")
    plt.ylabel("Remote Salary (USD)")
    plt.grid(alpha=0.3)

    plt.savefig("salary_experience_scatter.png", bbox_inches="tight")

    print("Chart saved: salary_experience_scatter.png")
    return fig


# 3. KDE Plot - Distribution Analysis
def plot_salary_kde(df):
    """
    Plot KDE density estimate showing salary distribution across roles.
    """
    print("Plotting Salary Density (KDE)...")

    # Set figure size
    fig = plt.figure(figsize=(10, 6))

    sns.kdeplot(
        data=df,
        x="salary_onsite",
        hue="job_role",
        fill=True,
        alpha=0.4
    )

    plt.title("Salary Distribution by Job Role (KDE)")
    plt.xlabel("Onsite Salary (USD)")
    plt.grid(alpha=0.3)

    plt.savefig("salary_kde.png", bbox_inches="tight")

    print("Chart saved: salary_kde.png")
    return fig


# 4. Faceted Plot - Role Trends
def plot_faceted_relplot(df):
    """
    Multiple scatter plot using figure-level relplot.
    Faceted by Job Role.
    """
    print("Plotting Faceted Role Trends...")

    g = sns.relplot(
        data=df,
        x="experience_years",
        y="salary_onsite",
        hue="country",
        col="job_role",
        kind="scatter"
    )

    g.fig.suptitle(
        "Global Salary Trends by Role & Experience",
        y=1.03
    )

    plt.savefig("faceted_salary_roles.png", bbox_inches="tight")

    print("Chart saved: faceted_salary_roles.png")
    return g


if __name__ == "__main__":
    print("Global Salary Index Analyzer Project...\n")

    path = "global_salaries.csv"
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: {path} not found.")
        df = None

    if df is not None:
        plot_salary_comparison(df)
        plot_salary_vs_experience(df)
        plot_salary_kde(df)
        plot_faceted_relplot(df)



