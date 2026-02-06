# YouTube Content Strategy Analyzer Project
# Hello developers! Welcome to Project 3: YouTube Content Strategy Analyzer! 🎯📊

# Chef loves watching YouTube! He has collected data from his favourite YouTube channels to understand what makes a video successful. The dataset contains metrics like views, likes, and comments for various trending videos.

# Chef wants you to build a Visual Dashboard to answer questions like:

# Which videos are watched the most?
# Do more views actually translate into more likes?
# Which videos create the most discussion?
# Your task is to turn this raw data into beautiful, insightful charts!

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with the file youtube.csv. It contains columns such as:

# title (Video Name)
# channel_title (Channel Name)
# views (Total Views)
# likes (Total Likes)
# comment_count (Total Comments)
# Your Tasks
# Load the YouTube Dataset
# Inside load_data():

# Read the CSV file using Pandas.
# Docs: pd.read_csv()
# Visualize Views vs. Likes (Scatter Plot)
# Inside plot_scatter(df):
# This chart will show if popular videos (high views) also get appreciated (high likes). We will also use bubble size to show comments!

# Setup: Set figure size to 10 inches by 6 inches.
# Plotting: Create a scatter plot where:
# X-axis: views
# Y-axis: likes
# Size (s): comment_count * 0.3 (Scaling down for readability)
# Color: "purple"
# Transparency (alpha): 0.5
# Edge Color: "black"
# Styling:
# Title: "Views vs Likes (Size = Comment Count)"
# Labels: X-label="Views", Y-label="Likes"
# Grid: Enable grid with alpha 0.5.
# Limits: Stretch axes to 110% of max values ((max value of columns) * 1.1) to let the data breathe.
# Save: Save the chart as scatter_plot.png.
# Docs: plt.scatter() | plt.grid() | plt.xlim() | plt.savefig() | plt.title() function | plt.xlabel() function | plt.ylabel() function
# Compare Likes vs. Comments (Side-by-Side Bar Chart)
# Inside bar_chart_side_by_side(df):
# This chart compares two different metrics for the same video side-by-side.
# Setup: Set figure size to 12 inches by 6 inches (wider for video titles).
# Logic: We need to manually shift the bars so they don't overlap:
# Likes: Shift Left (x - width/2), Color: "skyblue".
# Comments: Shift Right (x + width/2), Color: "orange".
# Styling:
# Title: "Engagement Analysis: Likes vs Comments"
# Labels: X-label="Video Title", Y-label="Count"
# Rotation: Rotate x-axis labels vertically so they don't overlap.
# Legend: Add a legend to explain the colors.
# Grid: Enable grid only on the Y-axis with alpha 0.7.
# Final Touch: We have written plt.tight_layout() to ensure long titles aren't cut off (Code already provided).
# Save: Save the chart as bar_chart.png.
# Docs: plt.bar() | plt.xticks() | plt.legend() | plt.tight_layout() | plt.title() function | plt.xlabel() function | plt.ylabel() function
# Expected Output:
# When you run the code, your program should print the following messages and generate two image files in the same directory:

# Console Output:
# YouTube Content Strategy Analyzer...

# Dataset Preview:
#                title   channel_title    views  likes  dislikes  comment_count
# 0   The New SpotMini  BostonDynamics    75752   9419        52           1230
# 1   VLOG Delhi Metro   TravelIndiaYT   204889   6031       225            510
# 2  U2 - The Blackout          U2VEVO    60506   5389       106            455
# 3  NF - Let You Down          NFVEVO  1774018  40417      5002           1686
# 4   Live in the now!       poofables    95085   7909      1652            593
# Chart saved: scatter_plot.png
# Chart saved: bar_chart.png
# Generated Files:
# scatter_plot.pngimage
# bar_chart.pngimage












import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files
import matplotlib.pyplot as plt


# 1. Load Dataset
def load_data():
    """
    Load and return the YouTube dataset.
    """
    path = "youtube.csv"
    df = pd.read_csv(path)
    
    print("Dataset Preview:")
    print(df.head())
    return df


# 2. Scatter Plot: Views vs Likes
def plot_scatter(df):
    """
    Create a scatter plot comparing Views vs Likes.
    Marker size proportional to comment count + slight transparency.
    """
    # Set figure size
    plt.figure(figsize=(10, 6))

    # Create scatter plot
    plt.scatter(
        df["views"],
        df["likes"],
        s=df["comment_count"] * 0.3,
        color="purple",
        alpha=0.5,
        edgecolors="black"
    )

    # Add title and labels
    plt.title("Views vs Likes (Size = Comment Count)")
    plt.xlabel("Views")
    plt.ylabel("Likes")

    # Enable grid
    plt.grid(alpha=0.5)

    # Set axis limits
    plt.xlim(0, df["views"].max() * 1.1)
    plt.ylim(0, df["likes"].max() * 1.1)

    # Save plot
    plt.savefig("scatter_plot.png")

    print("Chart saved: scatter_plot.png")


# 3. Side-by-Side Bar Chart
def bar_chart_side_by_side(df):
    """
    Compare Likes and Comments per video using side-by-side bars.
    """
    titles = df["title"]
    likes = df["likes"]
    comments = df["comment_count"]

    x = np.arange(len(titles))
    width = 0.35

    # Set figure size
    plt.figure(figsize=(12, 6))

    # Likes bars (left)
    plt.bar(x - width/2, likes, width, label="Likes", color="skyblue")

    # Comments bars (right)
    plt.bar(x + width/2, comments, width, label="Comments", color="orange")

    # Add title and labels
    plt.title("Engagement Analysis: Likes vs Comments")
    plt.xlabel("Video Title")
    plt.ylabel("Count")

    # X-axis ticks
    plt.xticks(x, titles, rotation=90)

    # Legend
    plt.legend()

    # Grid (Y-axis only)
    plt.grid(axis="y", alpha=0.7)

    # Layout adjustment
    plt.tight_layout()

    # Save plot
    plt.savefig("bar_chart.png")

    print("Chart saved: bar_chart.png")


if __name__ == "__main__":
    print("YouTube Content Strategy Analyzer...\n")

    # Load Data
    df = load_data()

    if df is not None:
        plot_scatter(df)
        bar_chart_side_by_side(df)




