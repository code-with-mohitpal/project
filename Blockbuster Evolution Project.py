# Blockbuster Evolution Project
# Hey Learners! Welcome to Project 1: Blockbuster Evolution Project! 🍿🎬

# Movies are more than just entertainment - they are a massive global business. Every year, thousands of films are released, competing for audience attention and box-office success.
# Chef is a huge movie enthusiast and has collected historical box-office data of movies released over the last 40 years. He wants to answer big questions:

# Which studios dominate the market?
# How has the industry grown financially over decades?
# What are the short-term revenue trends?
# Chef needs your help to analyze this dataset. Your task is to use the Pandas library to clean, analyze, and extract meaningful insights.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic using the Pandas Library.
# Do NOT change function names or print statements.
# Dataset
# In this Project, you will work with a CSV file: movies.csv

# This dataset contains 40 years of movie data.
# Columns:
# name → Movie title
# released → Full release date string (e.g., "June 13, 1980")
# Note: Needs parsing into a proper Date object.
# gross → Total Box-Office Revenue ($)
# If missing (NaN), revenue data is unavailable.
# company → Production Company / Studio Name
# rating → MPAA Rating (e.g., R, PG, PG-13)
# genre → Movie Genre (e.g., Action, Drama)
# country → Country of origin
# Dataset Preview (First 5 rows):
# name,rating,genre,released,country,gross,company
# The Shining,R,Drama,"June 13, 1980",United Kingdom,46998772.0,Warner Bros.
# The Blue Lagoon,R,Adventure,"July 2, 1980",United States,58853106.0,Columbia Pictures
# Star Wars: Episode V - The Empire Strikes Back,PG,Action,"June 20, 1980",United States,538375067.0,Lucasfilm
# Airplane!,PG,Comedy,"July 2, 1980",United States,83453539.0,Paramount Pictures
# Caddyshack,R,Comedy,"July 25, 1980",United States,39846344.0,Orion Pictures
# Tasks
# Load Dataset
# Inside load_flight_data(filename):
# Load the CSV file into a Pandas DataFrame.
# Docs: pandas.read_csv()
# Clean the Data
# Inside clean_data(df):
# Step 1: Convert the released column to datetime objects.
# Step 2: Remove rows where gross revenue is NaN (Missing).
# Docs: dropna | pandas.to_datetime()
# Optimize Memory
# Inside optimize_memory(df):
# Text columns like rating ("PG", "R") and genre ("Action", "Comedy") repeat thousands of times. Storing them as simple text strings wastes RAM.
# Task: Convert the following columns to the category data type:
# "rating", "genre", "country", "company"
# Docs: Pandas Categorical Data
# Rank Production Studios
# Inside rank_studios(df):
# Who are the giants of the industry?
# Step 1: Group movies by company and sum their gross revenue.
# Note: Use observed=True in your groupby to handle the categorical data cleanly.
# Step 2: Rank the studios based on total revenue.
# The highest earner gets Rank 1.
# Use method='min' (if two studios tie for 1st place, they both get Rank 1).
# Step 3: Combine the data into a new DataFrame.
# Columns should be: "Total_Gross" and "Rank".
# Sort the result by Rank (Ascending order).
# Docs: groupby | rank
# Industry Growth (Expanding Sum)
# Inside calculate_industry_growth(df):
# Chef wants to see the "All-Time Cumulative Revenue" of the film industry grow over the years.
# Step 1: Sort the data by released date. (Time-series data must be sorted).
# Step 2: Calculate the Expanding Sum of the gross column.
# Store this in a new column called "cumulative_industry_gross".
# Example:
# Movie A: 
# 10
# (
# T
# o
# t
# a
# l
# :
# 10(Total:10)
# Movie B: 
# 20
# (
# T
# o
# t
# a
# l
# :
# 20(Total:30)
# Movie C: 
# 15
# (
# T
# o
# t
# a
# l
# :
# 15(Total:45)
# Step 3: Return a DataFrame with only these columns:
# "released", "name", "gross", "cumulative_industry_gross"
# Docs: DataFrame.expanding().sum()
# Trend Analysis (Rolling Average)
# Inside analyze_recent_trends(df):
# Box office numbers are volatile. One massive hit is followed by three flops. We need to smooth the line.
# Step 1: Sort by released date.
# Step 2: Calculate the 3-Movie Rolling Average for gross.
# Store this in a new column called "rolling_avg_3_movies".
# Step 3: Fill the first two NaN values with 0.
# Step 4: Return a DataFrame with only these columns:
# "released", "name", "gross", "rolling_avg_3_movies"
# Docs: rolling()
# Expected Output:

# ### Blockbuster Evolution Project ###

# 1. Data Loaded Successfully.

# 2. Top 5 Companies by Total Gross:
#                         Total Gross  Rank
# company                                  
# Universal Pictures     1.643803e+10   1.0
# Paramount Pictures     1.480054e+10   2.0
# Warner Bros.           1.389824e+10   3.0
# Twentieth Century Fox  1.233287e+10   4.0
# Columbia Pictures      9.153184e+09   5.0

# 3. Industry Growth (First 5 Entries):
#      released                        name       gross  cumulative_industry_gross
# 81 1980-01-18                     Windows   2128395.0                  2128395.0
# 74 1980-01-18  Just Tell Me What You Want   2086905.0                  4215300.0
# 65 1980-02-01                       Fatso   7653061.0                 11868361.0
# 29 1980-02-01             American Gigolo  22743674.0                 34612035.0
# 18 1980-02-08                     The Fog  21448782.0                 56060817.0

# 4. Recent Trends (First 10 Entries):
#      released                          name       gross  rolling_avg_3_movies
# 81 1980-01-18                       Windows   2128395.0          0.000000e+00
# 74 1980-01-18    Just Tell Me What You Want   2086905.0          0.000000e+00
# 65 1980-02-01                         Fatso   7653061.0          3.956120e+06
# 29 1980-02-01               American Gigolo  22743674.0          1.082788e+07
# 18 1980-02-08                       The Fog  21448782.0          1.728184e+07
# 69 1980-02-08                 Hero at Large  15934737.0          2.004240e+07
# 20 1980-02-15                      Cruising  19814523.0          1.906601e+07
# 39 1980-03-07         Coal Miner's Daughter  67182787.0          3.431068e+07
# 83 1980-03-19  The King and the Mockingbird    167451.0          2.905492e+07
# 26 1980-03-21               Little Darlings  34326249.0          3.389216e+07





# import pandas as pd

# # 1. Load Dataset
# def load_dataset(filepath):
#     """
#     Load the CSV file and handle file not found errors.
#     """
#     try:
#         # TODO: Read the CSV file into a DataFrame
#         df = __________
#         return df
#     except FileNotFoundError:
#         print(f"Error: {filepath} not found.")
#         return pd.DataFrame()


# # 2. Clean Data (Date Parsing & Removing Empty Rows)
# def clean_data(df):
#     """
#     Parse the complex date format and remove rows with missing gross revenue.
#     """
#     # Step 1: Copying the dataframe to avoid modifying the original
#     df_clean = df.copy()
    
#     # TODO: Convert the 'released' column to datetime objects
#     df_clean['released'] = __________

#     # TODO: Remove rows where 'gross' is NaN (Empty) to prevent calculation errors later
#     df_clean = __________
    
#     # Step 4: Returning cleaned dataframe
#     return df_clean


# # 3. Optimize Memory
# def optimize_memory(df):
#     """
#     Convert string columns with repeated values to 'category' type to save RAM.
#     """
#     # Copying the dataframe
#     df_optimized = df.copy()
    
#     # List of columns that are good candidates for categorical conversion
#     categorical_cols = ['rating', 'genre', 'country']
    
#     for col in categorical_cols:
#         # Check if column exists before converting
#         if col in df_optimized.columns:
#             # TODO: Convert the column to 'category' type
#             df_optimized[col] = __________
            
#     # Returning optimized dataframe
#     return df_optimized


# # 4. Studio Ranking (Grouped Ranking)
# def rank_studios(df):
#     """
#     Rank production companies by their total gross revenue.
#     """
#     # TODO: Group by 'company' and sum the 'gross' revenue
#     # Put observed=True in groupby to handle categorical data properly
#     studio_gross = __________
    
#     # TODO: Rank the studios based on total gross (Highest gross = Rank 1)
#     # Assign the same rank to studios with the same gross revenue
#     ranks = __________
    
#     # TODO: Combine into a clean table
#     # Columns: 'Total_Gross', 'Rank'

#     ranking_table = __________
    
#     return ranking_table


# # 5. Industry Growth (Expanding Sums)
# def calculate_industry_growth(df):
#     """
#     Calculate the cumulative gross revenue over time.
#     """
#     # TODO: Sort the dataframe by 'released' date (Essential for time-series calculations)
#     df_sorted = __________
    
#     # TODO: Calculate Expanding Sum for 'gross' to get cumulative industry gross
#     df_sorted['cumulative_industry_gross'] = __________
    
#     # TODO: Return relevant columns
#     return __________


# # 6. Trend Analysis (Rolling Windows)
# def analyze_recent_trends(df):
#     """
#     Calculate the '3-Movie Rolling Average' of Gross Revenue.
#     """
#     # Sort by date first to ensure the rolling window moves through time correctly
#     df_sorted = __________
    
#     # TODO: Calculate the Rolling Average
#     # 1. Select 'gross' column
#     # 2. Create a rolling window of 3
#     # 3. Calculate the mean
#     # 4. Fill NaN values with 0 (zero) for the first two entries
#     df_sorted['rolling_avg_3_movies'] = __________
    
#     # TODO: Return relevant columns
#     return __________


# if __name__ == "__main__":
#     print("### Blockbuster Evolution Project ###")
    
#     # 1. Load
#     df_raw = load_dataset("movies.csv")
    
#     if not df_raw.empty:
#         # 2. Clean
#         df_clean = clean_data(df_raw)
        
#         # 3. Optimize
#         df = optimize_memory(df_clean)
    
#         # Check if we still have data after cleaning (e.g. dropping NaNs)
#         if not df.empty:
#             print(f"\n1. Data Loaded Successfully.")
            
#             # 2. Rankings
#             print("\n2. Top 5 Companies by Total Gross:")
#             print(rank_studios(df).head())
            
#             # 3. Cumulative Growth
#             print("\n3. Industry Growth (First 5 Entries):")
#             print(calculate_industry_growth(df).head())
            
#             # 4. Rolling Trends
#             print("\n4. Recent Trends (First 10 Entries):")
#             print(analyze_recent_trends(df).head(10))
#         else:
#             print("Error: Dataframe is empty after cleaning.")
#     else:
#         print("Error: 'movies.csv' not found.")



import pandas as pd

def load_dataset(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return pd.DataFrame()


def clean_data(df):
    df_clean = df.copy()
    
    df_clean['released'] = pd.to_datetime(df_clean['released'])
    df_clean = df_clean.dropna(subset=['gross'])
    
    return df_clean


def optimize_memory(df):
    df_optimized = df.copy()
    
    categorical_cols = ['rating', 'genre', 'country', 'company']
    
    for col in categorical_cols:
        if col in df_optimized.columns:
            df_optimized[col] = df_optimized[col].astype('category')
            
    return df_optimized


def rank_studios(df):
    studio_gross = df.groupby('company', observed=True)['gross'].sum()
    
    ranks = studio_gross.rank(method='min', ascending=False)
    
    ranking_table = pd.DataFrame({
        'Total_Gross': studio_gross,
        'Rank': ranks
    }).sort_values('Rank')
    
    return ranking_table


def calculate_industry_growth(df):
    df_sorted = df.sort_values('released')
    
    df_sorted['cumulative_industry_gross'] = df_sorted['gross'].expanding().sum()
    
    return df_sorted[['released', 'name', 'gross', 'cumulative_industry_gross']]


def analyze_recent_trends(df):
    df_sorted = df.sort_values('released')
    
    df_sorted['rolling_avg_3_movies'] = (
        df_sorted['gross']
        .rolling(window=3)
        .mean()
        .fillna(0)
    )
    
    return df_sorted[['released', 'name', 'gross', 'rolling_avg_3_movies']]


if __name__ == "__main__":
    print("### Blockbuster Evolution Project ###")
    
    df_raw = load_dataset("movies.csv")
    
    if not df_raw.empty:
        df_clean = clean_data(df_raw)
        df = optimize_memory(df_clean)
    
        if not df.empty:
            print(f"\n1. Data Loaded Successfully.")
            
            print("\n2. Top 5 Companies by Total Gross:")
            print(rank_studios(df).head())
            
            print("\n3. Industry Growth (First 5 Entries):")
            print(calculate_industry_growth(df).head())
            
            print("\n4. Recent Trends (First 10 Entries):")
            print(analyze_recent_trends(df).head(10))
        else:
            print("Error: Dataframe is empty after cleaning.")
    else:
        print("Error: 'movies.csv' not found.")
