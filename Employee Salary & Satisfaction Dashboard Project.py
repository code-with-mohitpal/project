# Employee Salary & Satisfaction Dashboard Project
# Hello developers! Welcome to Project 4: Employee Salary & Satisfaction Dashboard Project! 💼📊

# Chef has now moved into the corporate world!
# He has collected HR data for employees working in different departments of his company. But raw spreadsheets don’t tell the full story - Chef needs VISUAL answers to key questions like:

# Which departments have the most employees?
# Which teams pay more or less?
# Are employees happy with their work?
# Do salary and satisfaction differ by gender or department?
# Help Chef build a visual dashboard using Seaborn and Matplotlib to uncover workforce trends.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named employees.csv.

# It contains columns such as:
# Name (Employee name)
# Gender (Male / Female)
# Department (IT, HR, Finance, Sales etc.)
# Experience_Level (Junior, Mid, Senior)
# Salary (Annual pay in USD)
# Satisfaction (Happiness score from 0.0 to 10.0)
# Dataset Preview (First 5 rows):
# Aarav,Male,Engineering,Junior,55000,7.8
# Isha,Female,Engineering,Senior,95000,8.6
# Kabir,Male,Engineering,Mid,75000,8.1
# Tanvi,Female,Engineering,Junior,58000,7.2
# Arjun,Male,Marketing,Mid,62000,7.4
# Your Tasks
# Load the Employee Dataset
# Inside load_employee_data(filename):

# Read the dataset (employees.csv) using Pandas library.
# Return it as a DataFrame.
# Docs: pandas.read_csv()
# Plot Department Headcounts (Count Plot)
# Inside plot_department_counts(df):
# Show which department has the most employees.

# Plot: Create a Count Plot.
# Map the Department to the X-axis.
# Compare groups: Separate the counts by Gender so we can see the balance in each team (Explore the hue parameter).
# Colors: Use the "viridis" color palette.
# Styling:
# Figure size: Set the figure size to 10 inches by 6 inches.
# Title: "Employee Count by Department".
# Labels: Set X to "Department" and Y to "Number of Employees".
# Legend Title: "Gender".
# Rotation: Rotate x-axis labels by 45 degrees so they don't overlap.
# Save: Save the plot as department_headcount.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: seaborn.countplot() | plt.savefig() | matplotlib.pyplot.figure() | matplotlib.pyplot.xticks() | plt.title()
# Plot Salary Distribution (Box Plot)
# Inside plot_salary_box(df):
# Compare salary ranges across departments.
# Plot: Create a Box Plot.
# Map Department to the X-axis and Salary to the Y-axis.
# We don't need a legend for this specific plot, so make sure to turn it off.
# Styling:
# Figure size: Set the figure size to 10 inches by 6 inches.
# Title: "Salary Distribution by Department".
# Labels: Set X to "Department" and Y to "Annual Salary ($)".
# Rotation: Rotate x-axis labels by 45 degrees.
# Save: Save the plot as salary_boxplot.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: seaborn.boxplot() | plt.figure() | plt.title()
# Plot Satisfaction Distribution (Violin Plot)
# Inside plot_satisfaction_violin(df):
# Show how happiness levels vary across gender and department.
# Plot: Create a Violin Plot.
# Map Department to X and Satisfaction to Y.
# Compare groups: Separate the violins by Gender.
# Merge: Instead of side-by-side violins, merge the male/female halves into a single shape (Look for the split parameter).
# Detail: Draw quartile lines inside the violins (Look for the inner parameter).
# Colors: Use the "muted" palette.
# Styling:
# Figure size: Set the figure size to 10 inches by 6 inches.
# Title: "Employee Satisfaction Density (Male vs Female)".
# Labels: Set X to "Department" and Y to "Satisfaction Score (0-10)".
# Legend Title: "Gender".
# Rotation: Rotate x-axis labels by 45 degrees.
# Save: Save as satisfaction_violin.png.
# Use bbox_inches parameter to avoid cutting off title (set to 'tight')
# Docs: seaborn.violinplot() | matplotlib.pyplot.savefig()
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# Data loaded successfully.
# Total Employees: 75

# Generating Department Count Chart...
# Saved: department_headcount.png

# Generating Salary Box Plot...
# Saved: salary_boxplot.png

# Generating Satisfaction Violin Plot...
# Saved: satisfaction_violin.png
# Generated Files:
# department_headcount.pngimage
# salary_boxplot.pngimage
# satisfaction_violin.pngimage





import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")   # Headless mode for saving files
import matplotlib.pyplot as plt


# 1. Load Employee Data
def load_employee_data(filename):
    """
    Load CSV dataset into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a dataframe
        df = pd.read_csv(filename)

        print("Data loaded successfully.")

        # Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Plot Department Headcounts
def plot_department_counts(df):
    """
    Create a countplot showing how many employees work in each department.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))
    
    # Create countplot
    sns.countplot(
        x="Department", 
        hue="Gender", 
        data=df, 
        palette="viridis"
    )
    
    # Title
    plt.title("Employee Count by Department")

    # Axis labels
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")

    # Legend title
    plt.legend(title="Gender")
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    
    output = "department_headcount.png"
    # Save figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


# 3. Plot Salary Distribution
def plot_salary_box(df):
    """
    Compare salary ranges across departments using boxplots.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))
    
    # Create boxplot
    sns.boxplot(
        x="Department", 
        y="Salary", 
        data=df, 
        legend=False
    )
    
    # Title
    plt.title("Salary Distribution by Department")

    # Axis labels
    plt.xlabel("Department")
    plt.ylabel("Annual Salary ($)")
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    
    output = "salary_boxplot.png"

    # Save figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


# 4. Plot Employee Satisfaction
def plot_satisfaction_violin(df):
    """
    Show satisfaction score distribution using violin plots.
    """

    # Set figure size
    plt.figure(figsize=(10, 6))
    
    # Create violinplot
    sns.violinplot(
        x="Department",
        y="Satisfaction",
        hue="Gender",
        data=df,
        split=True,
        inner="quartile",
        palette="muted"
    )
    
    # Title
    plt.title("Employee Satisfaction Density (Male vs Female)")

    # Axis labels
    plt.xlabel("Department")
    plt.ylabel("Satisfaction Score (0-10)")

    # Legend title
    plt.legend(title="Gender")
    
    # Rotate x-axis labels
    plt.xticks(rotation=45)
    
    output = "satisfaction_violin.png"

    # Save figure
    plt.savefig(output, bbox_inches="tight")

    print(f"Saved: {output}")


if __name__ == "__main__":
    file = "employees.csv"
    df = load_employee_data(file)

    if not df.empty:
        print(f"Total Employees: {len(df)}")

        # Who works here?
        print("\nGenerating Department Count Chart...")
        plot_department_counts(df)

        # How much do they make?
        print("\nGenerating Salary Box Plot...")
        plot_salary_box(df)

        # Are they happy?
        print("\nGenerating Satisfaction Violin Plot...")
        plot_satisfaction_violin(df)
