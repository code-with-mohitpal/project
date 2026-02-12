# Instagram Viral Trends Analytics Project
# Hey Innovators! Welcome to Project 4: Instagram Viral Trends Analytics Project! 📸✨

# Every day, millions of posts are uploaded on Instagram - but only a few go viral. Some posts get massive reach, while others barely reach their audience - even when they look similar.

# Chef manages multiple Instagram pages and has collected post-level engagement data to understand:

# Which engagement metrics move together?
# Do hashtags really increase reach?
# Why do some posts perform far better (or worse) than expected?
# Raw numbers alone can’t answer these questions. Chef needs your help to analyze Instagram engagement patterns.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named instagram_dataset.csv.

# Columns Description:
# post_id → Unique ID of the post
# account_id → Creator or page ID
# likes → Number of likes on the post
# comments → Total comments received
# shares → Number of times the post was shared
# saves → Number of times users saved the post
# reach → Number of unique accounts that saw the post
# hashtags_count → Number of hashtags used in the post
# Dataset Preview (First 5 rows):
# post_id,account_id,likes,comments,shares,saves,reach,hashtags_count
# 1001,ACC_0001,194,5,7,34,4327,7
# 1002,ACC_0002,449,10,21,68,7451,5
# 1003,ACC_0003,114,2,1,22,1639,8
# 1004,ACC_0004,91,0,7,0,2877,7
# 1005,ACC_0005,154,8,5,21,5350,9
# Your Tasks
# Load Instagram Data
# Inside load_instagram_data(filename):
# Read the CSV file using Pandas.
# Return the DataFrame.
# Docs: pandas.read_csv()
# Plot Engagement Correlation (Heatmap)
# Inside plot_department_counts(df):
# Instagram engagement metrics often influence each other. We want to see if users who "Like" (one metric) a post also tend to "Share" (another metric) it.
# Step 1: Select the numeric columns: likes, comments, shares, saves, reach (code already provided).
# Step 2: Compute the correlation matrix.
# Step 3: Create a Seaborn Heatmap:
# Annotate: Show values inside cells (Explore the annot parameter).
# Color Map: Set the Color theme to "coolwarm" (Explore the cmap parameter).
# Format: Use fmt=".2f" to show 2 decimal places.
# Lines: Set Cell borders to 0.5 for separation (Explore the linewidths parameter).
# Styling:
# Figure Size: Set the figure size to 10 inches by 8 inches.
# Title: "Instagram Engagement Correlation Heatmap"
# Save: Save the plot as engagement_correlation_heatmap.png.
# Adjust the spacing using plt.tight_layout().
# Docs: pandas.DataFrame.corr | seaborn.heatmap | matplotlib.pyplot.figure | matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
# Hashtag Impact Trend (Regression Plot)
# Inside plot_hashtag_vs_reach(df):
# We want to answer: "Do hashtags actually increase reach?", To analyze this, you will create a Regression Plot.
# Create a Regression Plot (sns.regplot):
# X-axis: hashtags_count
# Y-axis: reach
# Scatter Color: Make the dots green.
# Line Color: Make the trend line red.
# Styling:
# Figure Size: Set the figure size to 10 inches by 6 inches.
# Title: "Hashtag Count vs. Reach Trend"
# X-Label: "Number of Hashtags"
# Y-Label: "Post Reach"
# Save: Save as hashtag_reach_trend.png
# Adjust the spacing using plt.tight_layout().
# Docs: seaborn.regplot | matplotlib.pyplot.figure | matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
# Residual Analysis (Viral Detection)
# Inside plot_residual_analysis(df):
# In the previous plot, the "Line" represents the average result. The "Residual" is the difference between the actual result and the average. High positive residuals = Viral Hits.
# Create a Residual Plot (sns.residplot):
# X-axis: hashtags_count
# Y-axis: reach
# Color: Make the points purple.
# Reference Line:
# Add a horizontal line at y=0 (the baseline).
# Color: black
# Style: Dashed (--)
# Styling:
# Figure Size: Set the figure size to 10 inches by 6 inches.
# Title: "Residual Analysis: Viral Outliers (Observed - Expected)"
# X-Label: "Number of Hashtags"
# Y-Label: "Residual Reach (Deviation)"
# Save: Save as viral_residual_analysis.png
# Adjust the spacing using plt.tight_layout().
# Docs: seaborn.residplot | matplotlib.pyplot.axhline | matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# ### Instagram Viral Trends Analytics ###
# Data Loaded Successfully: 29999 posts.
# Columns: ['post_id', 'account_id', 'likes', 'comments', 'shares', 'saves', 'reach', 'hashtags_count']
# Saved: engagement_correlation_heatmap.png
# Saved: hashtag_reach_trend.png
# Saved: viral_residual_analysis.png
# Generated Files:
# engagement_correlation_heatmap.pngimage
# hashtag_reach_trend.pngimage
# viral_residual_analysis.pngimage



#   import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# import matplotlib
# matplotlib.use("Agg")  # Headless mode for saving files

# # Constants
# FILE_NAME = "instagram_dataset.csv"
# # Set a clean visual theme
# sns.set_theme(style="whitegrid")


# # 1. === Loading Instagram Data ===
# def load_instagram_data(filename):
#     """
#     Loading Instagram post dataset.
#     """
#     try:
#         # TODO: Read the CSV file into a dataframe
#         df = __________
        
#         print(f"Data Loaded Successfully: {len(df)} posts.")
#         print(f"Columns: {list(df.columns)}")
        
#         # TODO: Return the dataframe
#         return __________

#     except FileNotFoundError:
#         print(f"Error: {filename} not found.")
#         return pd.DataFrame()



# # 2. === Correlation Heatmap ===
# def plot_engagement_correlation(df):
#     """
#     Visualize correlation between engagement metrics using a Heatmap.
#     """
#     # Numeric engagement columns
#     engagement_cols = [
#         "likes",
#         "comments",
#         "shares",
#         "saves",
#         "reach"
#     ]
    
#     # TODO: Calculate correlation matrix using .corr() on the selected columns
#     corr_matrix = __________

#     # TODO: Set figure size to 10 inches by 8 inches
#     __________

#     # TODO: Create a Heatmap
#     # Arguments:
#     # - Data for this heatmap is the correlation matrix
#     # - Show numbers on the blocks (Explore the annot parameter)
#     # - Set the color map to "coolwarm"
#     # - Format numbers to 2 decimal places (Explore the fmt parameter)
#     # - Set the line widths between cells to 0.5
#     sns.heatmap(
#         __________,
#         __________, 
#         __________, 
#         __________,
#         __________
#     )

#     # TODO: Set the title to "Instagram Engagement Correlation Heatmap"
#     __________
    
#     # TODO: Adjust layout with tight_layout()
#     __________
    
#     # TODO: Save the figure as "engagement_correlation_heatmap.png"
#     __________
    
#     print("Saved: engagement_correlation_heatmap.png")



# # 3. === Hashtag Impact Trend (Regression Plot) ===
# def plot_hashtag_vs_reach(df):
#     """
#     Analyze relationship between hashtags and reach using Regression.
#     """
#     # TODO: Set figure size to 10 inches by 6 inches
#     __________

#     # TODO: Create a Regression Plot (regplot)
#     # Arguments:
#     # - X axis: "hashtags_count"
#     # - Y axis: "reach"
#     # - data: df
#     # - Make scatter points green (Explore the scatter_kws parameter)
#     # - Make the Trend line red (Explore the line_kws parameter)
#     sns.regplot(
#         __________,
#         __________, 
#         __________, 
#         __________,
#         __________
#     )

#     # TODO: Set title to "Hashtag Count vs. Reach Trend"
#     __________
    
#     # TODO: Set x-axis label to "Number of Hashtags" and y-axis label to "Post Reach"
#     __________
#     __________

#     # TODO: Adjust layout using tight_layout() and save as "hashtag_reach_trend.png"
#     __________
#     __________
    
#     print("Saved: hashtag_reach_trend.png")



# # 4. === Residual Analysis (Unexpected Viral Behavior) ===
# def plot_residual_analysis(df):
#     """
#     Use a Residual Plot to see 'outlier' performance.
#     Points far from 0 line = Posts performing much better/worse than expected.
#     """
#     # TODO: Set figure size to 10 inches by 6 inches
#     __________

#     # TODO: Create a Residual Plot (residplot)
#     # Arguments:
#     # - X axis: "hashtags_count"
#     # - Y axis: "reach"
#     # - data: df
#     # - Make the points purple
#     sns.residplot(
#         __________,
#         __________,
#         __________,
#         __________
#     )

#     # TODO: Add a reference line at 0 (y=0) (Expected Performance)
#     # # Color: Black, Linestyle: Dashed ("--")
#     __________

#     # TODO: Set title to "Residual Analysis: Viral Outliers (Observed - Expected)"
#     __________
    
#     # TODO: Set x-axis label to "Number of Hashtags"
#     __________
    
#     # TODO: Set y-axis label to "Residual Reach (Deviation)"
#     __________

#     # TODO: Adjust layout using tight_layout() and save as "viral_residual_analysis.png"
#     __________
#     __________
    
#     print("Saved: viral_residual_analysis.png")



# if __name__ == "__main__":
#     print("### Instagram Viral Trends Analytics ###")

#     df = load_instagram_data(FILE_NAME)

#     if not df.empty:
#         # 1. Correlation Analysis (Heatmap)
#         plot_engagement_correlation(df)

#         # 2. Hashtag Trend Analysis (Regression)
#         plot_hashtag_vs_reach(df)

#         # 3. Residual Analysis (Residplot)
#         plot_residual_analysis(df)

#     else:
#         print("Analysis stopped.")




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib
matplotlib.use("Agg")

FILE_NAME = "instagram_dataset.csv"
sns.set_theme(style="whitegrid")


def load_instagram_data(filename):
    try:
        df = pd.read_csv(filename)
        
        print(f"Data Loaded Successfully: {len(df)} posts.")
        print(f"Columns: {list(df.columns)}")
        
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


def plot_engagement_correlation(df):

    engagement_cols = [
        "likes",
        "comments",
        "shares",
        "saves",
        "reach"
    ]
    
    corr_matrix = df[engagement_cols].corr()

    plt.figure(figsize=(10, 8))

    sns.heatmap(
        corr_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Instagram Engagement Correlation Heatmap")
    
    plt.tight_layout()
    
    plt.savefig("engagement_correlation_heatmap.png")
    
    print("Saved: engagement_correlation_heatmap.png")


def plot_hashtag_vs_reach(df):

    plt.figure(figsize=(10, 6))

    sns.regplot(
        x="hashtags_count",
        y="reach",
        data=df,
        scatter_kws={"color": "green"},
        line_kws={"color": "red"}
    )

    plt.title("Hashtag Count vs. Reach Trend")
    
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Post Reach")

    plt.tight_layout()
    plt.savefig("hashtag_reach_trend.png")
    
    print("Saved: hashtag_reach_trend.png")


def plot_residual_analysis(df):

    plt.figure(figsize=(10, 6))

    sns.residplot(
        x="hashtags_count",
        y="reach",
        data=df,
        color="purple"
    )

    plt.axhline(y=0, color="black", linestyle="--")

    plt.title("Residual Analysis: Viral Outliers (Observed - Expected)")
    
    plt.xlabel("Number of Hashtags")
    plt.ylabel("Residual Reach (Deviation)")

    plt.tight_layout()
    plt.savefig("viral_residual_analysis.png")
    
    print("Saved: viral_residual_analysis.png")


if __name__ == "__main__":
    print("### Instagram Viral Trends Analytics ###")

    df = load_instagram_data(FILE_NAME)

    if not df.empty:
        plot_engagement_correlation(df)
        plot_hashtag_vs_reach(df)
        plot_residual_analysis(df)
    else:
        print("Analysis stopped.")
