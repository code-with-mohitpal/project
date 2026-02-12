# Iris 3D Mapper Project
# Visualizing Biological Data in 3D Space

# Hey Innovators! Welcome to Project 2: Iris 3D Mapper Project! 🌸🌿

# Biologists often analyze plant measurements to understand how different species vary and cluster in nature. One of the most famous datasets used for this purpose is the Iris Flower Dataset.
# Chef wants to visually explore this biological data to answer big questions:

# Can we visually identify clusters of species in 3D space?
# How do petal and sepal dimensions interact?
# What does the "terrain" of petal width look like?
# Your task is to transform raw biological data into meaningful visual insights using Subplots, 3D Scatter Plots, and Filled Contour Maps.

# Important Notes
# You are given a single file: main.py:

# Do NOT change function names: The testing system relies on them.
# Do NOT use plt.show(): This project runs in a "headless" environment (no screen). You must use plt.savefig("filename.png") to generate output.
# Do NOT close the plot after saving: Do not call plt.close() or similar functions after saving the plot.
# All functions are already defined in main.py. You need to complete the missing logic.
# Dataset
# You will work with a CSV file named iris.csv.

# Columns Description:
# SepalLengthCm → Length of the sepal (cm)
# SepalWidthCm → Width of the sepal (cm)
# PetalLengthCm → Length of the petal (cm)
# PetalWidthCm → Width of the petal (cm)
# Species → "Iris-setosa", "Iris-versicolor", "Iris-virginica"
# Dataset Preview (First 5 rows):
# Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
# 1,5.1,3.5,1.4,0.2,Iris-setosa
# 2,4.9,3.0,1.4,0.2,Iris-setosa
# 3,4.7,3.2,1.3,0.2,Iris-setosa
# 4,4.6,3.1,1.5,0.2,Iris-setosa
# 5,5.0,3.6,1.4,0.2,Iris-setosa
# Your Tasks
# Load Iris Data
# Inside load_iris_data(filepath):
# Read the CSV file using Pandas.
# Return the DataFrame (code provided).
# Docs: pandas.read_csv()
# Feature Distribution (Histograms)
# Inside plot_feature_distributions(df):
# Goal: Compare the spread of all 4 features at a glance.
# Layout: Create a 2 × 2 grid of subplots.
# Figure Size: Set the figure size to 10 inches by 8 inches (code provided).
# Plotting Requirements: Create a histogram for each feature in the specific subplot:
# (0,0) Histogram of SepalLengthCm (Color: skyblue)
# (0,1) Histogram of SepalWidthCm (Color: salmon)
# (1,0) Histogram of PetalLengthCm (Color: lightgreen)
# (1,1) Histogram of PetalWidthCm (Color: gold)
# Common Settings:
# Number of bins = 15 (Explore the bins parameter).
# Color of edge = black (Explore the edgecolor parameter).
# Save: Save as iris_distributions.png (code provided)
# Adjust the spacing using plt.tight_layout().
# Docs: matplotlib.pyplot.subplots | pandas.Series.hist | matplotlib.pyplot.tight_layout | matplotlib.pyplot.savefig
# 3D Species Clustering
# Inside plot_3d_clusters(df):
# Goal: Visualize how the three species cluster in a 3D volume.
# Part A: 3D Scatter Plot
# Initialize a 3D projection subplot.
# Loop through the data grouped by species.
# Inside the loop, create a scatter plot for the current group:
# X-axis: SepalLengthCm
# Y-axis: SepalWidthCm
# Z-axis: PetalLengthCm
# Color Mapping: (code provided)
# Use the provided colors dictionary to find the color for the current species. Use "black" as the default/fallback color if the species is not found (Explore the c parameter and dictionary .get() method).
# Styling:
# Size = 50 (Explore the s parameter).
# Transparency = 0.6 (Explore the alpha parameter).
# Set label as species, this is important for legend (Explore the label parameter).
# Part B: Evolutionary Path (Centroids)
# Calculate the Mean (Average) of the columns grouped by Species.
# The Line: Draw a dashed black line connecting the centroids of the 3 species.
# Use the Mean X, Y, and Z values calculated above.
# Color should be black, Width of line: 3, Line should be dashed (Explore the color, linewidth and linestyle parameters).
# Label: "Cluster Center Path".
# Save: Save as iris_3d_scatter.png (code provided).
# Docs: Matplotlib 3D Scatter Plots | Matplotlib 3D Line Plots | pandas.DataFrame.groupby | Matplotlib Linestyles
# Filled Contour Map
# Inside plot_contour_map(df):
# Goal: Create a topological map where "Petal Width" represents the elevation.
# Axes:
# X: SepalLengthCm
# Y: SepalWidthCm
# Z (Elevation): PetalWidthCm
# The Map:
# Use ax.tricontourf() to create a filled contour.
# Number of levels: 14
# Colormap: 'inferno'
# Add a Colorbar labeled "Petal Width (Elevation)" (Explore the label parameter).
# The Overlay:
# Plot the original data points on top so we can see where the data actually exists.
# Color of points should be black, Size of points: 10, Transparency: 0.3 (Explore the color, s and alpha parameters).
# Label: "Data Points"
# Save: Save as iris_contour_map.png (code provided).
# Docs: matplotlib.pyplot.tricontourf | Matplotlib Colormaps | matplotlib.pyplot.colorbar | matplotlib.pyplot.scatter
# Expected Output:
# When you run the code, your program should print the following messages and generate three image files in the same directory:

# Console Output:
# Iris dataset loaded successfully.

# Generating Histograms...
# Distributions plot saved to iris_distributions.png

# Generating 3D Scatter Plot...
# 3D Scatter plot saved to iris_3d_scatter.png

# Generating Contour Map...
# Contour map saved to iris_contour_map.png
# Generated Files:
# iris_distributions.pngimage
# iris_3d_scatter.pngimage
# iris_contour_map.pngimage



# import pandas as pd
# import matplotlib.pyplot as plt

# import matplotlib
# # Force Matplotlib to work without GUI
# matplotlib.use("Agg")

# # 1. Load Iris Data
# def load_iris_data(filepath):
#     """
#     Load the Iris dataset from CSV.
#     """
#     try:
#         # TODO: Read the CSV file into a DataFrame
#         df = __________
        
#         print("Iris dataset loaded successfully.")
#         return df
#     except Exception as e:
#         print(f"Error loading data: {e}")
#         return pd.DataFrame()


# # 2. Feature Distribution (Histograms)
# def plot_feature_distributions(df):
#     """
#     Create and save a 2x2 grid of histograms to show data distribution.
#     Visualizing feature distributions using histograms.
#     """
#     # TODO: Create a figure with 2 rows and 2 columns
#     fig, axes = __________(__________, __________, figsize=(10, 8))
#     fig.suptitle("Iris Feature Distributions")

#     # TODO: Plot histograms for each feature on a specific axis

#     # TODO: Row 0, Col 0: SepalLengthCm
#     # color: skyblue, number of bins: 15, edgecolor: black
#     __________
#     axes[0, 0].set_title('Sepal Length (Cm)')

#     # TODO: Row 0, Col 1: SepalWidthCm
#     # color: salmon, number of bins: 15, edgecolor: black
#     __________
#     axes[0, 1].set_title('Sepal Width (Cm)')

#     # TODO: Row 1, Col 0: PetalLengthCm
#     # color: lightgreen, number of bins: 15, edgecolor: black
#     __________
#     axes[1, 0].set_title('Petal Length (Cm)')

#     # TODO: Row 1, Col 1: PetalWidthCm
#     # color: gold, number of bins: 15, edgecolor: black
#     __________
#     axes[1, 1].set_title('Petal Width (Cm)')

#     plt.tight_layout()
    
#     # Save the plot
#     output_file = "iris_distributions.png"
#     plt.savefig(output_file)
#     print(f"Distributions plot saved to {output_file}")


# # 3. 3D Scatter + Line Plot
# def plot_3d_clusters(df):
#     """
#     Visualize species in 3D space and connect their averages with a line.
#     """

#     # Size of the figure
#     fig = plt.figure(figsize=(10, 8))

#     # TODO: Create 3D axes using projection = "3d"
#     # Number of rows = 1, Number of columns = 1, index = 1
#     ax = fig.add_subplot(__________, projection=__________)
    
#     # Colors for the species
#     colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
    
#     # Part A: 3D Scatter Plot
#     # TODO: Loop through each species group to plot points
#     for species, group in __________:

#         # TODO: Create the Scatter Plot
#         ax.scatter(
#             # TODO: Map the 3 axes to SepalLength, SepalWidth, PetalLength
#             __________,  # X Axis
#             __________,  # Y Axis
#             __________,  # Z Axis

#             # TODO: Apply the color based on species
#             __________,

#             # TODO: Mark the label for legend as "species"
#             __________,

#             # TODO: Set the size of points to 50 and transparency to 0.6
#             __________,
#             __________
#         )

#     # Part B: 3D Line Plot (Evolutionary Path)
#     # TODO: Calculate the MEAN (average) of numerical columns grouped by Species
#     numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
#     means = __________
    
#     # TODO: Draw a line connecting the centers (means) of the clusters
#     ax.plot(
#         # TODO: Map the 3 axes to the means of SepalLength, SepalWidth, PetalLength
#         __________, # X axis  
#         __________, # Y axis
#         __________, # Z axis

#         # TODO: Set color to black
#         __________, 

#         # TODO: Set line width to 3
#         __________,

#         # TODO: Set line style to dashed 
#         __________,

#         # TODO: Set label for legend as "Cluster Center Path"
#         __________
#     )
    
#     # Labels of the axes
#     ax.set_title("3D Species Clusters & Trends")
#     ax.set_xlabel("Sepal Length (Cm)")
#     ax.set_ylabel("Sepal Width (Cm)")
#     ax.set_zlabel("Petal Length (Cm)")
#     ax.legend()
    
#     # Save the plot
#     output_file = "iris_3d_scatter.png"
#     plt.savefig(output_file, dpi=150)
#     print(f"3D Scatter plot saved to {output_file}")


# # 4. Plot Filled Contour Map
# def plot_contour_map(df):
#     """
#     Create a filled contour map to represent elevation using Petal Width.
#     """
#     fig, ax = plt.subplots(figsize=(10, 6))
    
#     # TODO: Define X, Y, Z for the map
#     # Map Sepal Length to X axis and Sepal Width to Y axis
#     x = __________
#     y = __________

#     # TODO: Use Petal Width as the "elevation" (Z axis)
#     z = __________

#     # TODO: Create the Filled Contour Map
#     # Number of levels = 14, colormap = 'inferno'
#     contour = __________
    
#     # Adding a color bar
#     cbar = plt.colorbar(contour)
#     cbar.set_label('Petal Width (Elevation)')

#     # TODO: Overlay the original points so we can see the data density
#     # Color of points: black, size: 10, transparency: 0.3, label: 'Data Points'
#     ax.scatter(_____, _____, c=_____, s=_____, alpha=_____, label=_____)
    
#     ax.set_title("Topological Map of Petal Width")
#     ax.set_xlabel("Sepal Length (Cm)")
#     ax.set_ylabel("Sepal Width (Cm)")
#     ax.legend()
    
#     # Save the plot
#     output_file = "iris_contour_map.png"
#     plt.savefig(output_file)
#     print(f"Contour map saved to {output_file}")


# if __name__ == "__main__":
    
#     # Load Data
#     df = load_iris_data("iris.csv")
    
#     if not df.empty:
#         # 1. Visualization: Histograms
#         print("\nGenerating Histograms...")
#         plot_feature_distributions(df)
        
#         # 2. Visualization: 3D Scatter
#         print("\nGenerating 3D Scatter Plot...")
#         plot_3d_clusters(df)
        
#         # 3. Visualization: Contour Map
#         print("\nGenerating Contour Map...")
#         plot_contour_map(df)



import pandas as pd
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")


def load_iris_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Iris dataset loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()


def plot_feature_distributions(df):

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle("Iris Feature Distributions")

    df['SepalLengthCm'].hist(bins=15, color='skyblue', edgecolor='black', ax=axes[0, 0])
    axes[0, 0].set_title('Sepal Length (Cm)')

    df['SepalWidthCm'].hist(bins=15, color='salmon', edgecolor='black', ax=axes[0, 1])
    axes[0, 1].set_title('Sepal Width (Cm)')

    df['PetalLengthCm'].hist(bins=15, color='lightgreen', edgecolor='black', ax=axes[1, 0])
    axes[1, 0].set_title('Petal Length (Cm)')

    df['PetalWidthCm'].hist(bins=15, color='gold', edgecolor='black', ax=axes[1, 1])
    axes[1, 1].set_title('Petal Width (Cm)')

    plt.tight_layout()
    output_file = "iris_distributions.png"
    plt.savefig(output_file)
    print(f"Distributions plot saved to {output_file}")


def plot_3d_clusters(df):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(1, 1, 1, projection="3d")

    colors = {
        'Iris-setosa': 'red',
        'Iris-versicolor': 'green',
        'Iris-virginica': 'blue'
    }

    for species, group in df.groupby("Species"):

        ax.scatter(
            group['SepalLengthCm'],
            group['SepalWidthCm'],
            group['PetalLengthCm'],
            c=colors.get(species, "black"),
            label=species,
            s=50,
            alpha=0.6
        )

    numeric_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    means = df.groupby("Species")[numeric_cols].mean()

    ax.plot(
        means['SepalLengthCm'],
        means['SepalWidthCm'],
        means['PetalLengthCm'],
        color="black",
        linewidth=3,
        linestyle="--",
        label="Cluster Center Path"
    )

    ax.set_title("3D Species Clusters & Trends")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.set_zlabel("Petal Length (Cm)")
    ax.legend()

    output_file = "iris_3d_scatter.png"
    plt.savefig(output_file, dpi=150)
    print(f"3D Scatter plot saved to {output_file}")


def plot_contour_map(df):

    fig, ax = plt.subplots(figsize=(10, 6))

    x = df['SepalLengthCm']
    y = df['SepalWidthCm']
    z = df['PetalWidthCm']

    contour = ax.tricontourf(x, y, z, levels=14, cmap='inferno')

    cbar = plt.colorbar(contour)
    cbar.set_label('Petal Width (Elevation)')

    ax.scatter(x, y, c='black', s=10, alpha=0.3, label='Data Points')

    ax.set_title("Topological Map of Petal Width")
    ax.set_xlabel("Sepal Length (Cm)")
    ax.set_ylabel("Sepal Width (Cm)")
    ax.legend()

    output_file = "iris_contour_map.png"
    plt.savefig(output_file)
    print(f"Contour map saved to {output_file}")


if __name__ == "__main__":

    df = load_iris_data("iris.csv")

    if not df.empty:
        print("\nGenerating Histograms...")
        plot_feature_distributions(df)

        print("\nGenerating 3D Scatter Plot...")
        plot_3d_clusters(df)

        print("\nGenerating Contour Map...")
        plot_contour_map(df)
