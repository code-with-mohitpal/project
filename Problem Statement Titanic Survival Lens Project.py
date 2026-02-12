# Titanic Survival Lens Project
# Visualizing the Titanic Tragedy with Seaborn

# Hello developers! Welcome to Project 4: Titanic Survival Lens Project! 🚢⚓

# The sinking of the RMS Titanic is one of the most tragic maritime disasters in history. More than 1,500 passengers lost their lives, but survival was not completely random.
# Chef has collected passenger data and wants to know:

# Did rich passengers survive more than poor ones?
# Was "Women and Children First" actually followed?
# How did age and ticket price affect survival chances?
# Your Task is to transform raw data into clear and meaningful visual insights.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named titanic_dataset.csv.

# Key Columns:
# Survived → Survival status (0 = No, 1 = Yes)
# Sex → Passenger gender
# Pclass → Passenger class (1st, 2nd, 3rd)
# Embarked → Port of embarkation (C, Q, S)
# Age → Passenger age
# Fare → Ticket price
# SibSp → Number of siblings/spouses aboard
# Parch → Number of parents/children aboard
# Dataset Preview (First 5 rows):
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
# 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
# 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
# 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
# 4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35,1,0,113803,53.1,C123,S
# 5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
# Your Tasks
# Load Titanic Data
# Inside load_titanic_data(filepath):
# Read the CSV file using Pandas.
# Return the DataFrame.
# Docs: pandas.read_csv()
# Feature Engineering
# Inside preprocess_titanic_data(df):
# Prepare the data for visualization:
# Drop Missing Rows: Remove rows where Embarked is missing.
# Fill Missing Values:
# Fill missing Age with the median age.
# Fill missing Fare with the median fare.
# Create New Feature:
# FamilySize = SibSp + Parch + 1
# (This counts the passenger plus all their family members).
# Docs: pandas.DataFrame.dropna | pandas.DataFrame.fillna | pandas.DataFrame.median
# Survival Rate Analysis (FacetGrid)
# Inside plot_demographic_facet(df):
# Comparing survival rates across Gender, Class, and Port.
# Step 1: Create the Grid
# Initialize sns.FacetGrid.
# Split Rows by Sex.
# Split Columns by Pclass.
# Enable the parameter that shows titles on the margins of the grid (Explore the margin_titles parameter).
# Step 2: Map the Plot
# Use g.map_dataframe() to map a Bar Plot (sns.barplot) onto the grid.
# Compare the Survival Status (Y-axis) based on the Port of Embarkation (X-axis).
# Use "skyblue" for the fill color and "black" for the bar borders (Explore the color and edgecolor parameters).
# Disable the confidence interval (error bars) to keep the chart clean (Explore the errorbar parameter).
# Step 3: Reference Line
# Add a horizontal reference line at 0.5 (50% chance).
# Color: "red", Style: "--".
# Save: Save as titanic_facet_bar.png (code provided).
# Docs: seaborn.FacetGrid | seaborn.FacetGrid.map_dataframe | seaborn.barplot | seaborn.FacetGrid.refline
# Survival Clusters (JointGrid)
# Inside plot_fare_age_joint(df):
# See how age and fare interact to affect survival.
# Step 1: Log Transformation
# Ticket fares are highly skewed (some are huge!).
# Create a new feature Log_Fare by applying a natural log transformation (+1) to the Fare column (Explore np.log1p).
# Step 2: Create JointGrid
# Initialize sns.JointGrid.
# Map Age to the X-axis and the new Log_Fare to the Y-axis.
# Step 3: Plot Data
# Center Plot: Use g.plot_joint() to create a Scatter Plot (sns.scatterplot).
# Color the points based on Survival Status (Explore the hue parameter).
# Define a palette where 0 is "red" and 1 is "green".
# Set the point transparency to 0.6 and size to 50 (Explore alpha and s parameters).
# Marginal Plots: Use g.plot_marginals() to add KDE Plots (sns.kdeplot) on the axes.
# Enable the fill under the curve (Explore the fill parameter).
# Set the transparency to 0.3 and use "gray" color.
# Save: Save as titanic_joint_kde.png
# Docs: numpy.log1p | seaborn.JointGrid | seaborn.JointGrid.plot_joint | seaborn.JointGrid.plot_marginals | seaborn.scatterplot | seaborn.kdeplot
# Feature Relationships (PairGrid)
# Inside plot_pair_matrix(df):
# A bird's-eye view of numeric relationships.
# Step 1: Create the Grid
# Define a list of specific numeric features to analyze: Age, Fare, and FamilySize (code provided).
# Initialize a sns.PairGrid.
# Limit the variables in the grid to the list you just defined (Explore the vars parameter).
# Color the charts based on Survival Status (Explore the hue parameter).
# Define a palette where 0 is "red" and 1 is "green".
# Step 2: Map the Visualization
# Use g.map() to apply a Scatter Plot (sns.scatterplot) to every cell in the grid.
# Set the point transparency to 0.6 (Explore alpha parameter).
# Set the point size to 30 (Explore s parameter).
# Step 3: Add Legend
# Add a legend to the grid with the title "Survived" (code provided).
# Save: Save as titanic_pair_grid.png.
# Docs: seaborn.PairGrid | seaborn.PairGrid.map | seaborn.scatterplot | seaborn.PairGrid.add_legend
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# Titanic dataset loaded successfully.
# Data cleaned and features engineered successfully.

# Generating FacetGrid...
# FacetGrid plot saved.

# Generating JointGrid...
# JointGrid plot saved.

# Generating PairGrid...
# PairGrid plot saved.
# Generated Files:
# titanic_facet_bar.pngimage
# titanic_joint_kde.pngimage
# titanic_pair_grid.pngimage


# mport pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# import matplotlib
# # Force Matplotlib to work without GUI
# matplotlib.use("Agg")


# # Set seaborn theme
# sns.set_theme(style="whitegrid", palette="muted")


# # 1. Load Titanic Dataset
# def load_titanic_data(filepath):
#     """
#     Load Titanic dataset from CSV file.
#     """
#     try:
#         # TODO: Read the CSV file into a dataframe
#         df = __________
#         print("Titanic dataset loaded successfully.")
#         return df

#     except Exception as e:
#         print(f"Error loading data: {e}")
#         return pd.DataFrame()


# # 2. Clean Data & Feature Engineering
# def preprocess_titanic_data(df):
#     """
#     Clean missing values and create new features
#     for analysis and visualization.
#     """

#     # Copying dataframe to avoid modifying original
#     df_clean = df.copy()

#     # Required columns
#     required_cols = [
#         "Survived", "Sex", "Pclass", "Embarked",
#         "Age", "Fare", "SibSp", "Parch"
#     ]

#     missing = [col for col in required_cols if col not in df_clean.columns]
#     if missing:
#         raise ValueError(f"Missing columns: {missing}")

#     # TODO: Remove rows with missing embarkation
#     df_clean = __________

#     # TODO: Fill missing Age using the median value of Age column
#     df_clean["Age"] = __________

#     # TODO: Fill missing Fare using the median value of Fare column
#     df_clean["Fare"] = __________

#     # Feature Engineering: Family Size
#     # TODO: Calculate FamilySize = SibSp + Parch + 1
#     df_clean["FamilySize"] = __________

#     print("Data cleaned and features engineered successfully.")
#     return df_clean


# # 3. FacetGrid — Survival Rate Analysis
# def plot_demographic_facet(df):

#     # FacetGrid for survival rate by Sex, Pclass and Embarked
#     # TODO: Initialize FacetGrid
#     # - data: The dataframe
#     # - Split the grid rows based on Gender
#     # - Split the grid columns based on Passenger Class
#     # - Enable margin titles
#     g = sns.FacetGrid(
#         __________,
#         __________,
#         __________,
#         __________
#     )

#     # Bar plot of survival rate by Embarked within each facet 
#     # TODO: Map a plotting function to the grid
#     # - Plotting Function: sns.barplot
#     # - Map "Port of Embarkation" to the X-axis
#     # - Map "Survival Status" to the Y-axis
#     # - Set color to "skyblue"
#     # - Set edgecolor to "black"
#     # - Disable error bars
#     g.map_dataframe(
#         __________,
#         __________,
#         __________,
#         __________,
#         __________,
#         __________
#     )

#     # TODO: Add a reference line at 0.5 survival rate
#     # Color the line red and use dashed style
#     g.refline(
#         ___________,
#         ___________,
#         ___________
#     )

#     # X and Y labels
#     g.set_axis_labels("Port of Embarkation", "Survival Rate (0-1)")

#     # Adjust titles and layout
#     g.figure.subplots_adjust(top=0.90)

#     # Overall title of the FacetGrid
#     g.figure.suptitle("Survival Rate by Gender, Class & Embarkation")

#     # Saving the plot
#     plt.savefig("titanic_facet_bar.png")
#     print("FacetGrid plot saved.")


# # 4. JointGrid — Age vs Fare
# def plot_fare_age_joint(df):

#     # Transform Fare for better visualization
#     plot_df = df.copy()

#     # TODO: Log-transform the 'Fare' column using np.log1p() to reduce skewness
#     plot_df["Log_Fare"] = __________

#     # JointGrid for Age vs Log(Fare)
#     # TODO: Initialize JointGrid
#     # - data: The transformed dataframe
#     # - Map "Age" to the X-axis
#     # - Map the new "Log_Fare" to the Y-axis
#     g = sns.JointGrid(
#         __________,
#         __________,
#         __________
#     )

#     # Scatter plot with survival hue
#     # TODO: Plot the joint chart (center) using sns.scatterplot
#     # - Color the points based on "Survival Status" (hue)
#     # - data: The transformed dataframe
#     # - Use the palette: {0: "red", 1: "green"}
#     # - Transparency (alpha): 0.6
#     # - Point size (s): 50
#     g.plot_joint(
#         __________,
#         __________,
#         __________,
#         __________,
#         __________,
#         __________
#     )

#     # Marginal KDE plots for Age and Log(Fare)
#     # TODO: Plot the marginal charts (sides) using sns.kdeplot
#     # - Enable fill under the curve
#     # - Set transparency (alpha) to 0.3
#     # - Set color to "gray"
#     g.plot_marginals(
#         __________,
#         __________,
#         __________,
#         __________
#     )

#     # X and Y labels
#     g.set_axis_labels("Age", "Fare (Log Scale)")

#     # Adjust titles and layout
#     g.figure.subplots_adjust(top=0.90)

#     # Overall title of the JointGrid
#     g.figure.suptitle("Survival Clusters: Age vs Log(Fare)")

#     # Saving the plot
#     plt.savefig("titanic_joint_kde.png")
#     print("JointGrid plot saved.")


# # 5. PairGrid — Numeric Relationships
# def plot_pair_matrix(df):

#     # PairGrid for selected numeric features
#     features = ["Age", "Fare", "FamilySize"]

#     # Create PairGrid with survival hue
#     # TODO: Initialize PairGrid
#     # - data: The dataframe
#     # - Limit variables to the 'features' list defined above
#     # - Color the charts based on "Survival Status"
#     # - Use palette: {0: "red", 1: "green"}
#     g = sns.PairGrid(
#         __________,
#         __________,
#         __________,
#         __________
#     )
    
#     # Scatter plots in the grid
#     # TODO: Map sns.scatterplot to the grid
#     # - Set transparency (alpha) to 0.6
#     # - Set point size (s) to 30
#     g.map(
#         __________, 
#         __________, 
#         __________
#     )

#     # Legend 
#     g.add_legend(title="Survived")

#     # Adjust titles and layout
#     g.figure.subplots_adjust(top=0.90)

#     # Overall title of the PairGrid
#     g.figure.suptitle("Passenger Feature Relationships")

#     # Saving the plot
#     plt.savefig("titanic_pair_grid.png")
#     print("PairGrid plot saved.")


# if __name__ == "__main__":

#     df_raw = load_titanic_data("titanic_dataset.csv")

#     if not df_raw.empty:
#         df = preprocess_titanic_data(df_raw)

#         print("\nGenerating FacetGrid...")
#         plot_demographic_facet(df)

#         print("\nGenerating JointGrid...")
#         plot_fare_age_joint(df)

#         print("\nGenerating PairGrid...")
#         plot_pair_matrix(df)





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
matplotlib.use("Agg")

sns.set_theme(style="whitegrid", palette="muted")


def load_titanic_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Titanic dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def preprocess_titanic_data(df):

    df_clean = df.copy()

    required_cols = [
        "Survived", "Sex", "Pclass", "Embarked",
        "Age", "Fare", "SibSp", "Parch"
    ]

    missing = [col for col in required_cols if col not in df_clean.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df_clean = df_clean.dropna(subset=["Embarked"])

    df_clean["Age"] = df_clean["Age"].fillna(df_clean["Age"].median())
    df_clean["Fare"] = df_clean["Fare"].fillna(df_clean["Fare"].median())

    df_clean["FamilySize"] = df_clean["SibSp"] + df_clean["Parch"] + 1

    print("Data cleaned and features engineered successfully.")
    return df_clean


def plot_demographic_facet(df):

    g = sns.FacetGrid(
        df,
        row="Sex",
        col="Pclass",
        margin_titles=True
    )

    g.map_dataframe(
        sns.barplot,
        x="Embarked",
        y="Survived",
        color="skyblue",
        edgecolor="black",
        errorbar=None
    )

    g.refline(
        y=0.5,
        color="red",
        linestyle="--"
    )

    g.set_axis_labels("Port of Embarkation", "Survival Rate (0-1)")
    g.figure.subplots_adjust(top=0.90)
    g.figure.suptitle("Survival Rate by Gender, Class & Embarkation")

    plt.savefig("titanic_facet_bar.png")
    print("FacetGrid plot saved.")


def plot_fare_age_joint(df):

    plot_df = df.copy()
    plot_df["Log_Fare"] = np.log1p(plot_df["Fare"])

    g = sns.JointGrid(
        data=plot_df,
        x="Age",
        y="Log_Fare"
    )

    g.plot_joint(
        sns.scatterplot,
        data=plot_df,
        hue="Survived",
        palette={0: "red", 1: "green"},
        alpha=0.6,
        s=50
    )

    g.plot_marginals(
        sns.kdeplot,
        fill=True,
        alpha=0.3,
        color="gray"
    )

    g.set_axis_labels("Age", "Fare (Log Scale)")
    g.figure.subplots_adjust(top=0.90)
    g.figure.suptitle("Survival Clusters: Age vs Log(Fare)")

    plt.savefig("titanic_joint_kde.png")
    print("JointGrid plot saved.")


def plot_pair_matrix(df):

    features = ["Age", "Fare", "FamilySize"]

    g = sns.PairGrid(
        df,
        vars=features,
        hue="Survived",
        palette={0: "red", 1: "green"}
    )

    g.map(
        sns.scatterplot,
        alpha=0.6,
        s=30
    )

    g.add_legend(title="Survived")

    g.figure.subplots_adjust(top=0.90)
    g.figure.suptitle("Passenger Feature Relationships")

    plt.savefig("titanic_pair_grid.png")
    print("PairGrid plot saved.")


if __name__ == "__main__":

    df_raw = load_titanic_data("titanic_dataset.csv")

    if not df_raw.empty:
        df = preprocess_titanic_data(df_raw)

        print("\nGenerating FacetGrid...")
        plot_demographic_facet(df)

        print("\nGenerating JointGrid...")
        plot_fare_age_joint(df)

        print("\nGenerating PairGrid...")
        plot_pair_matrix(df)
