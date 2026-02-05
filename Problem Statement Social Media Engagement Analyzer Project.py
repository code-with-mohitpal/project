# Social Media Engagement Analyzer Project
# Hello developers! Welcome to Project 6: Social Media Engagement Analyzer! 📊📱

# Chef is managing a social media platform and wants to understand how users interact with different posts. Each post receives likes, comments, and shares, but looking at raw numbers makes it difficult to identify engagement patterns.

# Your task is to analyze social media engagement data and create meaningful visualizations that help Chef answer questions like:

# Which posts are getting the most traffic?
# Are people mostly just "liking" or actually "commenting"?
# Do posts with many likes also get many shares?
# Important Notes

# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# Do NOT change function names: The testing system relies on them.
# Dataset
# You do NOT need to load an external file. The data is provided inside load_data() as a dictionary. You will convert this into a DataFrame:

# post_id: Unique ID.
# likes: Count of likes.
# comments: Count of comments.
# shares: Count of shares.
# Your Tasks
# Open main.py and complete the missing logic (marked with TODO and __________).

# Setup & Load Data
# Theme: Set the Seaborn theme to "whitegrid".
# Load: Inside load_data(), convert the provided dictionary into a Pandas DataFrame and return it.
# Docs: sns.set_theme() function, pd.DataFrame()
# Compute Total Engagement
# Inside analyze_engagement(df):
# Create a new column named total_engagement. This should be the sum of the likes, comments, and shares columns.
# Print a summary that displays the first 5 rows, but shows only the post_id and total_engagement columns.
# Stacked Bar Chart: Engagement Composition
# Inside plot_engagement_composition(df):
# Set figure size to 10 inches by 6 inches.
# Plot three layers using plt.bar():
# Likes (Base layer): Color: #3498db (Blue).
# Comments (Middle Layer): Plot the comments data. Configure this bar to start from the top of the Likes bar. Use color #e67e22 (Orange).
# Shares (Top Layer): Plot the shares data. Configure this bar to start from the top of the combined Likes and Comments bars. Use color #2ecc71 (Green).
# Add title (Engagement Composition per Post (Stacked)), labels (xlabel: "Post ID", ylabel: "Count"), and a legend.
# Save as engagement_composition.png.
# Docs: plt.bar() function, plt.savefig() function, plt.figure() function
# Bubble Chart: Metrics Relationship
# Inside plot_metrics_relationship(df):
# Set figure size to 8 inches by 6 inches.
# Create a Scatter Plot (sns.scatterplot()):
# X-axis: likes
# Y-axis: comments
# Size: shares (This creates the bubbles!)
# Add title (Likes vs Comments (Size = Shares)), labels (xlabel: "Likes", ylabel: "Comments") and a legend.
# Save as metrics_relationship.png.
# Docs: sns.scatterplot() function, plt.savefig() function, plt.figure() function
# Box Plot: Distribution (Data Melting)
# Inside plot_engagement_distribution(df):
# Concept: Seaborn prefers "Long Format" data. You must reshape your table so that all counts are in one column and metric names are in another.
# Step 1: Use df.melt() to transform the data:
# id_vars="post_id"
# value_vars=["likes", "comments", "shares"]
# var_name="metric"
# value_name="count"
# Step 2: Create a Box Plot (sns.boxplot()) using this new melted dataframe:
# X-axis: metric
# Y-axis: count
# Palette: "Set2"
# Legend: False
# Set figure size to 8 inches by 6 inches.
# Save as engagement_distribution.png.
# Docs: df.melt() function, sns.boxplot() function, plt.figure() function
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# Social Media Engagement Analyzer Project

# Data loaded successfully!

# Engagement Summary (First 5 rows):
#    post_id  total_engagement
# 0        1               165
# 1        2               460
# 2        3               755
# 3        4               300
# 4        5               565
# Chart saved: engagement_composition.png
# Chart saved: metrics_relationship.png
# Chart saved: engagement_distribution.png
# Generated Files:
# engagement_composition.pngimage
# metrics_relationship.pngimage
# engagement_distribution.pngimage




import pandas as pd
import matplotlib
matplotlib.use("Agg")  # headless mode (no GUI)

import matplotlib.pyplot as plt
import seaborn as sns


# 1. Set the Seaborn theme
sns.set_theme(style="whitegrid")


# 1. Load Data
def load_data():
    """
    Create and return a Pandas DataFrame containing social media engagement data.
    """
    data = {
        "post_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "likes": [120, 340, 560, 230, 410, 290, 600, 150],
        "comments": [30, 80, 120, 45, 95, 60, 150, 20],
        "shares": [15, 40, 75, 25, 60, 35, 100, 10]
    }

    # 2. Create DataFrame
    df = pd.DataFrame(data)

    print("Data loaded successfully!")

    # 3. Return DataFrame
    return df


# 2. Compute Engagement
def analyze_engagement(df):
    """
    Calculate total engagement column.
    """
    # 4. Create total_engagement column
    df["total_engagement"] = df["likes"] + df["comments"] + df["shares"]

    print("\nEngagement Summary (First 5 rows):")

    if "total_engagement" in df.columns:
        # 5. Print required columns
        print(df[["post_id", "total_engagement"]].head())

    return df


# 3. Stacked Bar Chart
def plot_engagement_composition(df):
    """
    Visualize Likes, Comments, and Shares using a Stacked Bar Chart.
    """
    # 6. Figure size
    plt.figure(figsize=(10, 6))

    # 7. Likes
    plt.bar(
        df["post_id"],
        df["likes"],
        label="Likes",
        color="#3498db"
    )

    # 8. Comments (stacked)
    plt.bar(
        df["post_id"],
        df["comments"],
        bottom=df["likes"],
        label="Comments",
        color="#e67e22"
    )

    # 9. Bottom for shares
    bottom_heights = df["likes"] + df["comments"]

    # 10. Shares (stacked)
    plt.bar(
        df["post_id"],
        df["shares"],
        bottom=bottom_heights,
        label="Shares",
        color="#2ecc71"
    )

    # 11. Title, labels, legend
    plt.title("Engagement Composition per Post (Stacked)")
    plt.xlabel("Post ID")
    plt.ylabel("Count")
    plt.legend()

    filename = "engagement_composition.png"
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


# 4. Bubble Chart
def plot_metrics_relationship(df):
    """
    Visualize Likes vs Comments, with bubble size representing Shares.
    """
    # 12. Figure size
    plt.figure(figsize=(8, 6))

    # 13. Scatter plot
    sns.scatterplot(
        data=df,
        x="likes",
        y="comments",
        size="shares",
        legend=True
    )

    # 14. Title and labels
    plt.title("Likes vs Comments (Size = Shares)")
    plt.xlabel("Likes")
    plt.ylabel("Comments")

    filename = "metrics_relationship.png"
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


# 5. Box Plot (Melted Data)
def plot_engagement_distribution(df):
    """
    Compare distributions of Likes vs Comments vs Shares.
    """
    # 15. Melt data
    melted_df = df.melt(
        id_vars="post_id",
        value_vars=["likes", "comments", "shares"],
        var_name="metric",
        value_name="count"
    )

    # 16. Figure size
    plt.figure(figsize=(8, 6))

    # 17. Box plot
    sns.boxplot(
        data=melted_df,
        x="metric",
        y="count",
        hue="metric",
        palette="Set2",
        legend=False
    )

    # 18. Title and labels
    plt.title("Distribution of Engagement Metrics")
    plt.xlabel("Metric")
    plt.ylabel("Count")

    filename = "engagement_distribution.png"
    plt.savefig(filename)

    print(f"Chart saved: {filename}")


if __name__ == "__main__":
    print("Social Media Engagement Analyzer Project\n")

    df = load_data()

    if df is not None:
        df = analyze_engagement(df)

        if "total_engagement" in df.columns:
            plot_engagement_composition(df)
            plot_metrics_relationship(df)
            plot_engagement_distribution(df)
        else:
            print("... Please complete the analyze_engagement function.")
    else:
        print("... Please complete the load_data function.")





