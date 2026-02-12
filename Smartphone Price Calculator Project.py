# Smartphone Price Calculator Project
# Is that ₹50,000 phone actually worth it?

# Hey Innovators! Welcome to Project 3: Smartphone Price Calculator Project! 📊📱

# Chef is building a pricing system that can analyze smartphone specifications and estimate a fair market price using data analysis and mathematical techniques.

# ❓The Big Question: Why Predict Price?
# The dataset lists the Market Price (Selling Price), but we aim to calculate the Fair Price (Hardware Worth).

# Value Check:
# Fair Price > Market Price = Great Deal!
# Fair Price < Market Price = Overpriced!
# Tech Score: Convert raw specs (RAM, Battery) into a single objective "Quality Score".
# Future Simulation: Estimate prices for hypothetical configurations (e.g., 12GB RAM + 512GB Storage).
# Your task is to use NumPy and Pandas to perform feature analysis, scoring, normalization, and price estimation.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic using the NumPy and Pandas Libraries.
# Do NOT change function names or print statements.
# Dataset
# In this Project, you will work with a CSV file named: smartphones.csv

# This dataset contains smartphone specifications along with their market prices.
# Columns:
# ram_capacity → RAM size in GB
# internal_memory → Internal storage in GB
# battery_capacity → Battery capacity in mAh
# primary_camera_rear → Rear camera megapixels
# rating → User rating
# price → Market price of the smartphone (₹)
# Dataset Preview (First 5 rows):
# ram_capacity,internal_memory,battery_capacity,primary_camera_rear,rating,price
# 12.0,256.0,5000.0,50.0,89.0,54999
# 6.0,128.0,5000.0,64.0,81.0,19989
# 4.0,64.0,5000.0,50.0,75.0,16499
# 6.0,128.0,5000.0,50.0,81.0,14999
# 6.0,128.0,5000.0,108.0,82.0,24999
# Tasks
# Data Loading
# Inside load_dataset(filepath):
# Read the CSV file using Pandas.
# Return the DataFrame (code already written).
# Docs: pandas.read_csv()
# Feature Extraction
# Inside split_features_target(df):
# We need to separate the Specs (X) from the Price (y).
# Step 1: Create X by selecting these exact 5 columns (in this order):
# "ram_capacity", "internal_memory", "battery_capacity", "primary_camera_rear", "rating".
# Step 2: Create y by selecting the "price" column.
# Step 3: Convert both X and y into NumPy arrays.
# Why? NumPy matrices are faster for mathematical operations than Pandas DataFrames.
# Docs: pandas.DataFrame.values (Converting to NumPy) | Pandas Indexing and Selecting Data
# Feature Preprocessing
# Inside preprocess_features(X):
# Problem: Battery values (e.g., 5000) are huge compared to RAM (e.g., 8). If we do math on raw numbers, the Battery column will dominate the results.
# Fix:
# Create a copy of X (Code provided).
# Scale down the Battery column (Index 2) by dividing it by 100.
# Example: 5000 becomes 50. 4500 becomes 45.
# Docs: NumPy Indexing and Slicing Arrays
# Market Range Analysis
# Inside detect_price_outliers(prices):
# Chef wants to know the "typical" price range, ignoring the super-cheap and super-expensive extremes.
# Calculate and return two values:
# The 5th Percentile (Low end).
# The 95th Percentile (High end).
# Docs: numpy.percentile Documentation
# The "Tech Score" (Matrix Multiplication)
# Inside calculate_weighted_score(X_scaled):
# We want to assign a single "Quality Score" to every phone based on its specs.
# The Weights: (code provided)
# RAM: 25% (0.25)
# Storage: 20% (0.20)
# Battery: 25% (0.25)
# Camera: 20% (0.20)
# Rating: 10% (0.10)
# Perform a Dot Product between the X_scaled matrix and the weights array.
# Docs: numpy.dot (Matrix Multiplication / Dot Product)
# Normalization (The Sigmoid Function)
# Inside sigmoid_normalization(scores):
# Raw scores are hard to compare. We want to squash them into a 0 to 1 rating (where 1 is perfect).
# Step 1: Center the data. Subtract the mean of the scores from every score (code provided).
# Step 2: Apply the Sigmoid formula:
# Sigmoid
# (
# z
# )
# =
# 1
# 1
# +
# e
# −
# z
# Sigmoid(z)= 
# 1+e 
# −z
 
# 1
# ​
 
# where z = centered_scores / 10
# Docs: numpy.exp (Exponential Function) | numpy.mean
# Fair Price Prediction (The Normal Equation)
# Inside estimate_fair_price(X_scaled, y):
# Now, use Linear Algebra to find the "Fair Price" for any phone specs.
# The Formula (Normal Equation):
# θ
# =
# (
# X
# T
# X
# )
# −
# 1
# X
# T
# y
# θ=(X 
# T
#  X) 
# −1
#  X 
# T
#  y
# Implementation Steps:
# Add Bias: Create a column of 1s and stack it next to X_scaled (so the model has a baseline price), code is already written in main.py file.
# Transpose: Calculate 
# X
# T
# X 
# T
#  .
# Matrix Multiply: Calculate 
# X
# T
# ⋅
# X
# X 
# T
#  ⋅X.
# Invert: Calculate the inverse of that result using np.linalg.pinv() (Pseudo-Inverse is safer than standard Inverse).
# Calculate Theta (
# θ
# θ): Multiply the Inverse by 
# X
# T
# X 
# T
#  , then by 
# y
# y.
# Predict: Finally, multiply your Bias-Matrix by 
# θ
# θ to get the predicted prices.
# Docs: numpy.hstack (Stacking Arrays horizontally) | numpy.transpose (Matrix Transpose) | numpy.linalg.pinv (Pseudo-Inverse)
# Price Simulation (Meshgrid)
# Inside simulate_price_grid(df):
# Chef wants a "Cheat Sheet" showing prices for different RAM and Storage combos.
# Step 1: Calculate the "Price per GB" for RAM and Storage using np.polyfit(column, price, 1). Take the first value (slope).
# Step 2: Create two grids using np.meshgrid() (code provided):
# RAM Options: [4, 6, 8, 12]
# Storage Options: [64, 128, 256, 512]
# Step 3: Calculate the matrix using this formula:
# Price
# =
# 5000
# +
# (
# RAM
# ×
# RAM_Rate
# )
# +
# (
# Storage
# ×
# Storage_Rate
# )
# Price=5000+(RAM×RAM_Rate)+(Storage×Storage_Rate)
# Docs: numpy.polyfit (Least squares polynomial fit) | numpy.meshgrid (Coordinate Matrices from Vectors)
# Expected Output:

# 1. Data Successfully Loaded: 869 smartphones found.
#    Features Processed & Scaled. Shape: (869, 5)

# 3. Typical Market Price Range: ₹8393 - ₹75995

# 4. Weighted Hardware Scores (Raw Sum):
# [85.6 60.5 43.8 57.7 69.4]

# 5. Normalized Spec Ratings (0-1 Scale):
# [0.94 0.54 0.18 0.47 0.74]

# 6. Estimated Fair Prices (Linear Model):
# [55031 27689 15018 29996 21380]

# 7. Theoretical Price Matrix (RAM vs Storage):
# [[ 33250  41426  49603  65956]
#  [ 45146  53323  61500  77853]
#  [ 68940  77116  85293 101646]
#  [116526 124703 132880 149233]]



# import numpy as np
# import pandas as pd

# # 1. Load Dataset
# def load_dataset(filepath):
#     """
#     Load dataset and return the dataframe.
#     """
#     try:
#         # TODO: Load the dataset using Pandas
#         df = __________
#         return df
#     except FileNotFoundError:
#         print(f"Error: {filepath} not found.")
#         return pd.DataFrame()


# # 2. Separate Features and Target
# def split_features_target(df):
#     """
#     Split the table into X (Specs) and y (Price).
#     """

#     feature_cols = [
#         "ram_capacity",   
#         "internal_memory",    
#         "battery_capacity", 
#         "primary_camera_rear",
#         "rating" 
#     ]
    
#     # Check if all columns exist
#     missing = [col for col in feature_cols if col not in df.columns]
#     if missing:
#         raise ValueError(f"Missing columns: {missing}")

#     # TODO: Select the 'feature_cols' from df and convert to .values (NumPy Matrix)
#     X = __________

#     # TODO: Select the "price" column and convert to .values
#     y = __________
    
#     return X, y


# # 2.5 Preprocess Features (Crucial Step)
# def preprocess_features(X):
#     """
#     Scale features so they have similar magnitudes.
#     Specifically, scale down Battery (5000 -> 50) to match RAM/Storage.
#     """
#     X_scaled = X.copy()
    
#     # TODO: Scale Battery (Column Index 2) by dividing by 100.
#     # We do this once here so ALL functions use the same data range.
#     X_scaled[:, 2] = __________
    
#     return X_scaled


# # 3. Detect Price Outliers
# def detect_price_outliers(prices):
#     """
#     Find the price range that covers 90% of phones (5th to 95th percentile).
#     """
#     # TODO: Calculate the 5th percentile
#     low = __________
    
#     # TODO: Calculate the 95th percentile
#     high = __________
    
#     return low, high


# # 4. Weighted Smartphone Scoring
# def calculate_weighted_score(X_scaled):
#     """
#     Calculate a 'Tech Score' for each phone using scaled data.
#     """
#     # Weights: RAM(25%), Storage(20%), Battery(25%), Camera(20%), Rating(10%)
#     weights = np.array([0.25, 0.20, 0.25, 0.20, 0.10])
    
#     # TODO: Calculate the weighted score using Matrix Multiplication (Dot Product)
#     # Hint: Use np.dot()
#     return __________


# # 5. Sigmoid Normalization
# def sigmoid_normalization(scores):
#     """
#     Convert raw scores to a 0-1 rating using the Sigmoid function.
#     """
#     # Center the scores around 0 so sigmoid works best
#     centered_scores = scores - np.mean(scores)
    
#     # TODO: Apply the Sigmoid Formula
#     # Formula: 1 / (1 + e^(-z)) where z = centered_scores / 10
#     return __________


# # 6. Fair Price Estimation (Normal Equation)
# def estimate_fair_price(X_scaled, y):
#     """
#     Predict fair prices using the Normal Equation (Linear Algebra).
#     Formula: theta = (X'X)^-1 X'y
#     """
#     # Add a column of 1s (Bias term) to X
#     ones = np.ones((X_scaled.shape[0], 1))
#     X_bias = np.hstack((ones, X_scaled))

#     # TODO: Calculate X Transpose (X')
#     X_T = __________

#     # TODO: Calculate (X'X) -> Matrix Multiplication
#     # Hint: Use np.dot()
#     xt_x = __________

#     # TODO: Calculate Inverse of (X'X)
#     # Hint: Use np.linalg.pinv()
#     xt_x_inv = __________

#     # TODO: Calculate Theta -> (X'X)^-1 * (X'y)
#     theta = __________

#     # TODO: Calculate Predicted Prices -> X_bias * theta
#     predicted_prices = __________

#     return theta, predicted_prices


# # 7. Price Simulation using Meshgrid
# def simulate_price_grid(df):
#     """
#     Simulate a price grid for different RAM/Storage combos.
#     Uses np.polyfit to find the 'Market Rate' per GB automatically.
#     """
#     # Calculate 'Price per GB' directly from data (Slope of the line)
#     ram_price_per_gb = np.polyfit(df['ram_capacity'], df['price'], 1)[0]
#     storage_price_per_gb = np.polyfit(df['internal_memory'], df['price'], 1)[0]

#     # Create the grid
#     ram_options = np.array([4, 6, 8, 12])
#     storage_options = np.array([64, 128, 256, 512])
    
#     # TODO: Generate a Meshgrid for RAM and Storage
#     # Hint: Use np.meshgrid()
#     RAM_GRID, STORAGE_GRID = __________

#     # Formula: Base Price + (RAM * RAM_Rate) + (Storage * Storage_Rate)
#     base_price = 5000
    
#     # TODO: Calculate the simulated price matrix using the grid variables
#     simulated_price = __________

#     return RAM_GRID, STORAGE_GRID, simulated_price


# if __name__ == "__main__":

#     try:
#         # 1. Load Data
#         df = load_dataset("smartphones.csv")
        
#         if not df.empty:
#             print(f"1. Data Successfully Loaded: {df.shape[0]} smartphones found.")

#             # 2. Split Features (Now uses Explicit Columns)
#             X_raw, y = split_features_target(df)
            
#             # Now both 'Score' and 'Price' functions use the same compatible data
#             X = preprocess_features(X_raw)
#             print(f"   Features Processed & Scaled. Shape: {X.shape}")

#             # 3. Outliers
#             low, high = detect_price_outliers(y)
#             print(f"\n3. Typical Market Price Range: ₹{int(low)} - ₹{int(high)}")

#             # 4. Weighted Score (Uses Scaled X)
#             scores = calculate_weighted_score(X)
#             print(f"\n4. Weighted Hardware Scores (Raw Sum):\n{scores[:5]}")

#             # 5. Normalization
#             ratings = sigmoid_normalization(scores)
#             print(f"\n5. Normalized Spec Ratings (0-1 Scale):\n{np.round(ratings[:5], 2)}")

#             # 6. Fair Price Prediction (Uses Scaled X + Pseudo Inverse)
#             theta, predicted = estimate_fair_price(X, y)
#             print(f"\n6. Estimated Fair Prices (Linear Model):\n{predicted[:5].astype(int)}")

#             # 7. Simulation
#             print("\n7. Theoretical Price Matrix (RAM vs Storage):")
#             RAM, STORAGE, prices = simulate_price_grid(df)
#             print(prices.astype(int))
            
#     except Exception as e:
#         print(f"\n[!] Error during execution: {e}")




import numpy as np
import pandas as pd


def load_dataset(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return pd.DataFrame()


def split_features_target(df):

    feature_cols = [
        "ram_capacity",
        "internal_memory",
        "battery_capacity",
        "primary_camera_rear",
        "rating"
    ]

    missing = [col for col in feature_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    X = df[feature_cols].values
    y = df["price"].values

    return X, y


def preprocess_features(X):
    X_scaled = X.copy()
    X_scaled[:, 2] = X_scaled[:, 2] / 100
    return X_scaled


def detect_price_outliers(prices):
    low = np.percentile(prices, 5)
    high = np.percentile(prices, 95)
    return low, high


def calculate_weighted_score(X_scaled):
    weights = np.array([0.25, 0.20, 0.25, 0.20, 0.10])
    return np.dot(X_scaled, weights)


def sigmoid_normalization(scores):
    centered_scores = scores - np.mean(scores)
    z = centered_scores / 10
    return 1 / (1 + np.exp(-z))


def estimate_fair_price(X_scaled, y):

    ones = np.ones((X_scaled.shape[0], 1))
    X_bias = np.hstack((ones, X_scaled))

    X_T = X_bias.T
    xt_x = np.dot(X_T, X_bias)
    xt_x_inv = np.linalg.pinv(xt_x)

    theta = np.dot(np.dot(xt_x_inv, X_T), y)
    predicted_prices = np.dot(X_bias, theta)

    return theta, predicted_prices


def simulate_price_grid(df):

    ram_price_per_gb = np.polyfit(df['ram_capacity'], df['price'], 1)[0]
    storage_price_per_gb = np.polyfit(df['internal_memory'], df['price'], 1)[0]

    ram_options = np.array([4, 6, 8, 12])
    storage_options = np.array([64, 128, 256, 512])

    RAM_GRID, STORAGE_GRID = np.meshgrid(ram_options, storage_options)

    base_price = 5000

    simulated_price = (
        base_price
        + (RAM_GRID * ram_price_per_gb)
        + (STORAGE_GRID * storage_price_per_gb)
    )

    return RAM_GRID, STORAGE_GRID, simulated_price


if __name__ == "__main__":

    try:
        df = load_dataset("smartphones.csv")

        if not df.empty:
            print(f"1. Data Successfully Loaded: {df.shape[0]} smartphones found.")

            X_raw, y = split_features_target(df)
            X = preprocess_features(X_raw)
            print(f"   Features Processed & Scaled. Shape: {X.shape}")

            low, high = detect_price_outliers(y)
            print(f"\n3. Typical Market Price Range: ₹{int(low)} - ₹{int(high)}")

            scores = calculate_weighted_score(X)
            print(f"\n4. Weighted Hardware Scores (Raw Sum):\n{scores[:5]}")

            ratings = sigmoid_normalization(scores)
            print(f"\n5. Normalized Spec Ratings (0-1 Scale):\n{np.round(ratings[:5], 2)}")

            theta, predicted = estimate_fair_price(X, y)
            print(f"\n6. Estimated Fair Prices (Linear Model):\n{predicted[:5].astype(int)}")

            print("\n7. Theoretical Price Matrix (RAM vs Storage):")
            RAM, STORAGE, prices = simulate_price_grid(df)
            print(prices.astype(int))

    except Exception as e:
        print(f"\n[!] Error during execution: {e}")
        
