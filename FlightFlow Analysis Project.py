# FlightFlow Analysis Project
# Hey Learners! Welcome to Project 2: FlightFlow Analysis Project! 📊✈️

# Air travel plays a major role in today’s fast-moving world, but delays can turn even a short journey into a frustrating experience.
# Chef is planning multiple domestic and international trips. To avoid unnecessary delays, he has collected real-world flight data containing information such as:

# Flight dates
# Airlines
# Departure delays
# Chef needs your help to analyze this dataset. Your task is to use the Pandas library to clean, analyze, and extract meaningful insights from flight delay data.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic using the Pandas Library.
# Do NOT change function names or print statements.
# Dataset
# In this Project, you will work with a CSV file named: flights.csv

# This dataset contains flight departure information.
# Columns:
# FlightDate → Date of the flight (YYYY-MM-DD)
# Airline → Name of the airline
# Origin → Departure airport or city code
# Destination → Arrival airport or city code
# DepartureDelay → Delay in minutes
# If missing (NaN), it means the flight was on time.
# Cancelled → Indicates whether the flight was cancelled.
# 0 = Not cancelled
# 1 = Cancelled
# Dataset Preview (First 5 rows):
# FlightDate,Airline,Origin,Destination,DepartureDelay,Cancelled
# 2024-04-02,Akasa Air,DOH,SIN,103,1
# 2024-01-04,Singapore Airlines,JFK,DOH,20,0
# 2024-05-24,Akasa Air,SIN,LHR,57,1  
# 2024-02-03,IndiGo,LHR,MUM,31,1
# 2024-04-07,Singapore Airlines,LHR,BLR,15,0
# Your Tasks
# Load Flight Data
# Inside load_flight_data(filename):
# Load the CSV file using Pandas.
# Convert the FlightDate column into datetime format.
# Use the format: "YYYY-MM-DD".
# Docs: pandas.read_csv() | pandas.to_datetime()
# Clean Delay Data
# Inside clean_delay_data(df):
# If DepartureDelay is missing (NaN), treat it as 0 minutes.
# This means the flight departed on time.
# Goal: Fill missing values (NaN) in the DepartureDelay column with 0.
# Docs: fillna()
# Extract Day Features
# Inside extract_day_features(df):
# Extract the day name from the flight date. Example:
# 2024-01-01 → Monday
# 2024-01-02 → Tuesday
# Store it in a new column called Day_Name.
# Docs: pandas.Series.dt.day_name()
# Airline Reliability Analysis
# Inside airline_reliability_stats(df):
# For each airline, calculate:
# Avg_Delay → The mean of the departure delay.
# Total_Flights → The count of how many flights they operated.
# Requirements:
# Group by Airline.
# Round average delay to 2 decimal places.
# Docs: groupby() | agg() | round()
# Rank Airlines by Reliability
# Inside rank_airlines(stats_df):
# Rank airlines from:
# Most reliable (lowest average delay)
# Least reliable (highest average delay)
# Goal: Sort your reliability stats so that the Most Reliable airline (Lowest Average Delay) appears at the top.
# Docs: sort_values()
# Identify Worst Days to Fly
# Inside identify_delayed_days(df):
# Calculate average delay for each day of the week.
# Sort days from highest delay to lowest.
# Round values to 2 decimal places.
# Docs: groupby() | mean() | sort_values()
# Expected Output:

# ### FlightFlow Analysis ###
# Data Loaded & Cleaned: 250 flights processed.

# Most Reliable Airlines (Lowest Avg Delay):
#                Avg_Delay  Total_Flights
# Airline                                
# Qatar Airways      38.88             24
# Emirates           44.04             25
# IndiGo             48.28             25

# Least Reliable Airlines (Highest Avg Delay):
#                  Avg_Delay  Total_Flights
# Airline                                  
# Akasa Air            58.12             24
# Lufthansa            62.95             19
# British Airways      71.11             28

# Worst Days to Fly (Highest Avg Delay):
# Day_Name
# Friday      65.28
# Tuesday     57.11
# Saturday    56.27
# Name: DepartureDelay, dtype: float64                                                                               import pandas as pd

# FILE_NAME = "flights.csv"

# # 1. Data Loading and Data Parsing
# def load_flight_data(filename):
#     """
#     Load flight dataset and parse dates from 'FlightDate'.
#     """
#     try:
#         # TODO: Load the CSV file into a Pandas DataFrame
#         df = __________

#         # Validation: Check if required column exists
#         if "FlightDate" not in df.columns:
#             print("Error: 'FlightDate' column is missing in the CSV.")
#             return pd.DataFrame()

#         # TODO: Parse the "FlightDate" column into datetime format
#         # Make sure to specify the correct date format (YYYY-MM-DD)
#         df["FlightDate"] = __________
        
#         return df
        
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#         return pd.DataFrame()
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return pd.DataFrame()


# # 2. Data Cleaning
# def clean_delay_data(df):
#     """
#     Assumption: If delay is NaN (empty), it means the flight was On Time (0 delay).
#     """

#     # TODO: Fill missing values (NaN) in the 'DepartureDelay' column with 0
#     if "DepartureDelay" in df.columns:
#         df["DepartureDelay"] = __________
    
#     return df


# # 3. Feature Extraction
# def extract_day_features(df):
#     """
#     Extract the 'Day Name' (Monday, Tuesday...) from the Date column.
#     """

#     # TODO: Get the name of the day (e.g., "Monday") from the "FlightDate" column
#     # Hint: Use Pandas date accessors to find the day name
#     df["Day_Name"] = __________
    
#     return df


# # 4. Statistical Analysis
# def airline_reliability_stats(df):
#     """
#     Calculate the Average Departure Delay and Total Flights for each airline.
#     """
#     # TODO: Group data by "Airline" and calculate two statistics for "DepartureDelay":
#     # 1. The Average (mean) delay
#     # 2. The Total count of flights
#     stats = __________
    

#     # Renaming columns for clarity
#     if not stats.empty:
#         stats = stats.rename(columns={"mean": "Avg_Delay", "count": "Total_Flights"})
        
#         # Round the average delay to 2 decimal places
#         stats["Avg_Delay"] = __________
    
#     return stats


# # 5. Ranking & Sorting
# def rank_airlines(stats_df):
#     """
#     Rank airlines from Most Reliable (Lowest Delay) to Least Reliable.
#     """
#     # TODO: Sort the airlines so that the one with the LOWEST "Avg_Delay" comes first
#     sorted_stats = __________
    
#     return sorted_stats


# # 6. Pattern Identification
# def identify_delayed_days(df):
#     """
#     Find which day of the week has the worst delays on average.
#     """
#     # TODO: Find the average "DepartureDelay" for each "Day_Name"
#     day_stats = __________
    
#     # TODO: Sort the results so the day with the HIGHEST delay comes first
#     # Round the result to 2 decimal places
#     sorted_days = __________
    
#     return sorted_days


# if __name__ == "__main__":
#     print("### FlightFlow Analysis ###")

#     # 1. Load Data
#     raw_df = load_flight_data(FILE_NAME)

#     if not raw_df.empty:
#         # 2. Clean Data
#         clean_df = clean_delay_data(raw_df)
#         print(f"Data Loaded & Cleaned: {clean_df.shape[0]} flights processed.")

#         # 3. Feature Extraction
#         enhanced_df = extract_day_features(clean_df)
        
#         # 4. Reliability Analysis
#         stats = airline_reliability_stats(enhanced_df)
#         ranked = rank_airlines(stats)
        
#         print("\nMost Reliable Airlines (Lowest Avg Delay):")
#         print(ranked.head(3))
        
#         print("\nLeast Reliable Airlines (Highest Avg Delay):")
#         print(ranked.tail(3))

#         # 5. Pattern Analysis
#         worst_days = identify_delayed_days(enhanced_df)

#         print("\nWorst Days to Fly (Highest Avg Delay):")
#         print(worst_days.head(3))
    
#     else:
#         print("Analysis could not proceed due to data loading errors.")





import pandas as pd

FILE_NAME = "flights.csv"

# 1. Data Loading and Data Parsing
def load_flight_data(filename):
    """
    Load flight dataset and parse dates from 'FlightDate'.
    """
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(filename)

        # Validation: Check if required column exists
        if "FlightDate" not in df.columns:
            print("Error: 'FlightDate' column is missing in the CSV.")
            return pd.DataFrame()

        # Parse the "FlightDate" column into datetime format
        df["FlightDate"] = pd.to_datetime(df["FlightDate"], format="%Y-%m-%d")
        
        return df
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()


# 2. Data Cleaning
def clean_delay_data(df):
    """
    Assumption: If delay is NaN (empty), it means the flight was On Time (0 delay).
    """

    # Fill missing values (NaN) in the 'DepartureDelay' column with 0
    if "DepartureDelay" in df.columns:
        df["DepartureDelay"] = df["DepartureDelay"].fillna(0)
    
    return df


# 3. Feature Extraction
def extract_day_features(df):
    """
    Extract the 'Day Name' (Monday, Tuesday...) from the Date column.
    """

    # Get the name of the day from the "FlightDate" column
    df["Day_Name"] = df["FlightDate"].dt.day_name()
    
    return df


# 4. Statistical Analysis
def airline_reliability_stats(df):
    """
    Calculate the Average Departure Delay and Total Flights for each airline.
    """
    # Group data by "Airline" and calculate mean and count
    stats = df.groupby("Airline")["DepartureDelay"].agg(["mean", "count"])
    

    # Renaming columns for clarity
    if not stats.empty:
        stats = stats.rename(columns={"mean": "Avg_Delay", "count": "Total_Flights"})
        
        # Round the average delay to 2 decimal places
        stats["Avg_Delay"] = stats["Avg_Delay"].round(2)
    
    return stats


# 5. Ranking & Sorting
def rank_airlines(stats_df):
    """
    Rank airlines from Most Reliable (Lowest Delay) to Least Reliable.
    """
    # Sort airlines by lowest Avg_Delay first
    sorted_stats = stats_df.sort_values(by="Avg_Delay", ascending=True)
    
    return sorted_stats


# 6. Pattern Identification
def identify_delayed_days(df):
    """
    Find which day of the week has the worst delays on average.
    """
    # Average delay per day
    day_stats = df.groupby("Day_Name")["DepartureDelay"].mean()
    
    # Sort by highest delay first and round to 2 decimals
    sorted_days = day_stats.sort_values(ascending=False).round(2)
    
    return sorted_days


if __name__ == "__main__":
    print("### FlightFlow Analysis ###")

    # 1. Load Data
    raw_df = load_flight_data(FILE_NAME)

    if not raw_df.empty:
        # 2. Clean Data
        clean_df = clean_delay_data(raw_df)
        print(f"Data Loaded & Cleaned: {clean_df.shape[0]} flights processed.")

        # 3. Feature Extraction
        enhanced_df = extract_day_features(clean_df)
        
        # 4. Reliability Analysis
        stats = airline_reliability_stats(enhanced_df)
        ranked = rank_airlines(stats)
        
        print("\nMost Reliable Airlines (Lowest Avg Delay):")
        print(ranked.head(3))
        
        print("\nLeast Reliable Airlines (Highest Avg Delay):")
        print(ranked.tail(3))

        # 5. Pattern Analysis
        worst_days = identify_delayed_days(enhanced_df)

        print("\nWorst Days to Fly (Highest Avg Delay):")
        print(worst_days.head(3))
    
    else:
        print("Analysis could not proceed due to data loading errors.")

                                     
