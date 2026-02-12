# Virat Kohli IPL Stats Analyzer Project
# Hello developers! Welcome to the Virat Kohli IPL Stats Analyzer Project! ⚾🏏

# Virat Kohli is one of the greatest batsmen in modern cricket. Over the years, he has delivered countless match-winning performances in the Indian Premier League (IPL).

# image
# Chef is a huge cricket fan and has collected match-by-match IPL performance data of Virat Kohli - including runs scored, opponents faced, venues played, dismissal status, and match dates.

# Chef needs your help to analyze this data and uncover meaningful insights. Your task is to use the Pandas library to perform data analysis.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic using the Pandas Library.
# Do NOT change function names or print statements.
# Dataset
# In this Project, you will work with two CSV files:

# ipl_matches.csv This file contains Virat Kohli’s IPL match-wise performance.
# Columns:
# match_date → Date of the match (YYYY-MM-DD)
# runs → Runs scored in the match
# opponent → Opponent team short code (CSK, MI, KKR, etc.)
# venue → Stadium name
# dismissal → How Virat got out (Caught, Bowled, Not Out, etc.)
# Dataset Preview (First 5 rows):
# match_no,runs,match_date,opponent,venue,dismissal
# 1,23,2011-04-09,MI,Chinnaswamy Stadium,Caught
# 2,12,2011-04-12,PBKS,Chinnaswamy Stadium,Bowled
# 3,71,2011-04-14,DC,Rajiv Gandhi Intl Stadium,Not Out
# 4,35,2011-04-19,RR,Sawai Mansingh Stadium,Run Out
# 5,12,2011-04-22,CSK,MA Chidambaram Stadium,Caught
# opponents.csv This file maps short team codes to full team names.
# Columns:
# opponent → Team short code
# fullName → Full team name
# Dataset Preview (First 5 rows):
# opponent,fullName
# MI,Mumbai Indians
# PBKS,Punjab Kings
# DC,Delhi Capitals
# RR,Rajasthan Royals
# CSK,Chennai Super Kings
# Your Tasks
# Load Match Data
# Inside load_data(filename):
# Load the CSV file using Pandas.
# Convert the match_date column into datetime objects.
# Hint: Use this format="%Y-%m-%d".
# Docs: pd.read_csv() | pd.to_datetime()
# Load Opponent Mapping
# Inside load_opponent_data(filename):
# Load the opponent mapping CSV.
# Return it as a DataFrame.
# Docs: pd.read_csv()
# Merge Match & Opponent Data
# Inside merge_match_opponent(match_df, opponent_df):
# Merge the match data (left) with opponent data (right).
# Use a left join on the "opponent" column.
# Why? We want to keep all match records, even if an opponent's full name is missing.
# Docs: pd.merge()
# Total Career Runs
# Inside total_runs(df):
# Calculate total runs Virat has scored in his entire IPL career.
# Docs: Series.sum()
# The Average
# Inside average_runs(df):
# Calculate on average how many runs Virat Kohli scores per match.
# Requirement: Round your answer to 2 decimal places.
# Docs: Series.mean() | round()
# The Favorite Rival
# Inside runs_by_opponent(df):
# Find out against which teams Virat scores the most runs.
# Goal: Calculate the total runs scored against each unique opponent (using their Full Name).
# Requirement: The output must be ranked from Highest runs to Lowest runs.
# Docs: groupby() | sum() | sort_values()
# The Half-Centuries
# Inside count_fifties(df):
# Calculate how many times Virat Kohli has scored a Fifty.
# Definition: A "Fifty" is a score of 50 or more, but less than 100. (A score of 100 is a Century, not a Fifty).
# Docs: Boolean Indexing
# The Centuries
# Inside count_centuries(df):
# Calculate how many times Virat Kohli has scored a Century.
# Definition: A score of 100 or more.
# Docs: Boolean Indexing
# The Career Growth Chart
# Inside career_run_progression(df):
# Now Chef's Question is, "I want to see how Virat Kohli's total runs increased match by match over time."
# Goal:
# Ensure the matches are in the correct chronological order (Time order).
# Calculate a Running Total (Cumulative Sum) of his runs.
# Store this running total in a new column called "career_runs".
# Return a DataFrame with only: match_date, runs, and career_runs.
# Docs: sort_values() | cumsum()
# Consistency Check
# Inside consistency_matches(df):
# Now calculate how often Virat Kohli gives a solid start.
# Goal: Count how many matches he has scored 30 or more runs in.
# Docs: Boolean Indexing
# The Finisher
# Inside not_out_innings(df):
# Calculate how many times Virat Kohli remained unbeaten.
# Goal: Find the number of innings where his dismissal status was "Not Out".
# Docs: Boolean Indexing
# The Fortress
# Inside best_venue(df):
# Find out which stadium is Virat Kohli's lucky charm.
# Goal: Find out which specific venue has the highest total runs scored by Virat. Return the name of that one venue.
# Docs: groupby() | sum() | sort_values()
# Expected Output:

# ### Virat Kohli Career Analysis ###

# Total Career Runs: 7804
# Average Runs Per Match: 36.3

# Runs Against Each Opponent (Top 3):
# fullName
# Kolkata Knight Riders    1071
# Mumbai Indians            949
# Rajasthan Royals          926
# Name: runs, dtype: int64

# Number of 50s: 60
# Number of Centuries: 8

# Career Run Progression (First 5 matches):
#   match_date  runs  career_runs
# 0 2011-04-09    23           23
# 1 2011-04-12    12           35
# 2 2011-04-14    71          106
# 3 2011-04-19    35          141
# 4 2011-04-22    12          153

# Number of Consistent Matches (30+ runs):
# 115
# Number of Not Out Innings:
# 40

# Best Venue: Chinnaswamy Stadium with 3227 runs

# port pandas as pd


# # 1. Load Virat Match Data
# def load_data(filename):
#     """
#     Load Virat Kohli match-wise performance data and parse dates.
#     """
#     try:
#         # TODO: Load the CSV file using Pandas
#         df = __________

#         # TODO: Convert 'match_date' column to datetime objects
#         # Use this format="%Y-%m-%d"
#         __________
        
#         return df
#     except FileNotFoundError:
#         print(f"Error: {filename} not found.")
#         return pd.DataFrame()
#     except Exception:
#         print(f"Error loading data.")
#         return pd.DataFrame()


# # 2. Load Opponent Mapping Data
# def load_opponent_data(filename):
#     try:
#         # TODO: Load the CSV file using Pandas
#         df = __________

#         return df
#     except FileNotFoundError:
#         print(f"Error: {filename} not found.")
#         return pd.DataFrame()


# # 3. Merge Match + Opponent Data
# def merge_match_opponent(match_df, opponent_df):
#     """
#     Merge match data with opponent full names.
#     """

#     if "opponent" not in match_df.columns or "opponent" not in opponent_df.columns:
#         print("Error: 'opponent' column missing in one of the datasets.")
#         return match_df

#     # TODO: Merge the two dataframes on the "opponent" column using a left join
#     merged_df = __________
    
#     return merged_df


# # 4. Analysis Functions
# def total_runs(df):
#     """
#     Calculate total runs scored by Virat Kohli.
#     """
#     runs_column = df["runs"]
    
#     # TODO: Calculate total runs scored by Virat Kohli
#     total = __________
    
#     return total


# def average_runs(df):
#     """
#     Calculate the average runs per match scored by Virat Kohli.
#     """
#     runs_column = df["runs"]
    
#     # TODO: Calculate the average runs per match
#     average = __________
    
#     # TODO: Round the average to 2 decimal places
#     average_rounded = __________
    
#     return average_rounded


# def runs_by_opponent(df):
#     """
#     Calculate total runs scored against each opponent.
#     """
#     # TODO: Group the data by "opponent" full name
#     grouped_data = __________

#     # TODO: Sum the runs for each opponent
#     total_runs = __________
    
#     # TODO: Sort the total runs in descending order
#     sorted_runs = __________
    
#     return sorted_runs


# def count_fifties(df):
#     """
#     Count the number of matches where Virat Kohli scored fifty or more runs (but less than 100 runs).
#     """
#     # TODO: Find the number of matches with 50-99 runs
#     total_fifties = __________

#     return total_fifties


# def count_centuries(df):
#     """
#     Count the number of matches where Virat Kohli scored a century or more runs.
#     """
#     # TODO: Find the number of matches with 100 or more runs
#     total_centuries = __________

#     return total_centuries


# def career_run_progression(df):
#     """
#     Calculate cumulative career runs over time.
#     """
#     # TODO: Sort the dataframe by "match_date"
#     df_sorted = __________

#     # TODO: Calculate cumulative sum of "runs"
#     # Hint: Use .cumsum() to calculate the cumulative sum of runs
#     cumulative_runs = __________

#     # TODO: Create a new column for career total runs with name "career_runs"
#     __________

#     # TODO: Select only the required columns for output
#     result = __________

#     return result


# def consistency_matches(df):
#     """
#     Count the number of matches where Virat Kohli scored at least 30 runs.
#     """
#     # TODO: Filter matches where runs are >= 30
#     total_consistent_matches = __________

#     return total_consistent_matches


# def not_out_innings(df):
#     """
#     Count the number of innings where Virat Kohli remained Not Out.
#     """
#     # TODO: Find the number of innings where Virat Kohli remained Not Out
#     total_not_out = __________

#     return total_not_out


# def best_venue(df):
#     """
#     Find the venue where Virat Kohli has scored the most runs.
#     """
#     # TODO: Find the venue where Virat Kohli has scored the most runs
#     best_venue = __________

#     return best_venue


# if __name__ == "__main__":
#     print("### Virat Kohli Career Analysis ###")

#     # Load Data
#     virat_df = load_data("ipl_matches.csv")
#     opponent_df = load_opponent_data("opponents.csv")

#     if not virat_df.empty:
#         # Merge if opponent data exists
#         if not opponent_df.empty:
#             df = merge_match_opponent(virat_df, opponent_df)
#         else:
#             df = virat_df
#             print("Warning: Opponent data missing, proceeding with match data only.")

#         # 1. Total runs
#         print(f"\nTotal Career Runs: {total_runs(df)}")

#         # 2. Average runs
#         print(f"Average Runs Per Match: {average_runs(df)}")

#         # 3. Runs against each opponent
#         print("\nRuns Against Each Opponent (Top 3):")
#         print(runs_by_opponent(df).head(3))

#         # 4. Fifty counts
#         print(f"\nNumber of 50s: {count_fifties(df)}")

#         # 5. Century counts
#         print(f"Number of Centuries: {count_centuries(df)}")

#         # 6. Career progression
#         print("\nCareer Run Progression (First 5 matches):")
#         print(career_run_progression(df).head())

#         # 7. Consistency (30+ runs)
#         print(f"\nNumber of Consistent Matches (30+ runs):")
#         print(f"{consistency_matches(df)}")

#         # 8. Not Out Innings
#         print(f"Number of Not Out Innings:")
#         print(f"{not_out_innings(df)}")

#         # 9. Best Venue
#         best = best_venue(df)
#         print(f"\nBest Venue: {best.index[0]} with {best.values[0]} runs")





import pandas as pd


def load_data(filename):
    try:
        df = pd.read_csv(filename)
        df["match_date"] = pd.to_datetime(df["match_date"], format="%Y-%m-%d")
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
    except Exception:
        print(f"Error loading data.")
        return pd.DataFrame()


def load_opponent_data(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


def merge_match_opponent(match_df, opponent_df):
    if "opponent" not in match_df.columns or "opponent" not in opponent_df.columns:
        print("Error: 'opponent' column missing in one of the datasets.")
        return match_df

    merged_df = pd.merge(match_df, opponent_df, on="opponent", how="left")
    return merged_df


def total_runs(df):
    runs_column = df["runs"]
    total = runs_column.sum()
    return total


def average_runs(df):
    runs_column = df["runs"]
    average = runs_column.mean()
    average_rounded = round(average, 2)
    return average_rounded


def runs_by_opponent(df):
    grouped_data = df.groupby("fullName")["runs"]
    total_runs = grouped_data.sum()
    sorted_runs = total_runs.sort_values(ascending=False)
    return sorted_runs


def count_fifties(df):
    total_fifties = df[(df["runs"] >= 50) & (df["runs"] < 100)].shape[0]
    return total_fifties


def count_centuries(df):
    total_centuries = df[df["runs"] >= 100].shape[0]
    return total_centuries


def career_run_progression(df):
    df_sorted = df.sort_values("match_date")
    cumulative_runs = df_sorted["runs"].cumsum()
    df_sorted["career_runs"] = cumulative_runs
    result = df_sorted[["match_date", "runs", "career_runs"]]
    return result


def consistency_matches(df):
    total_consistent_matches = df[df["runs"] >= 30].shape[0]
    return total_consistent_matches


def not_out_innings(df):
    total_not_out = df[df["dismissal"] == "Not Out"].shape[0]
    return total_not_out


def best_venue(df):
    best_venue = df.groupby("venue")["runs"].sum().sort_values(ascending=False).head(1)
    return best_venue


if __name__ == "__main__":
    print("### Virat Kohli Career Analysis ###")

    virat_df = load_data("ipl_matches.csv")
    opponent_df = load_opponent_data("opponents.csv")

    if not virat_df.empty:
        if not opponent_df.empty:
            df = merge_match_opponent(virat_df, opponent_df)
        else:
            df = virat_df
            print("Warning: Opponent data missing, proceeding with match data only.")

        print(f"\nTotal Career Runs: {total_runs(df)}")
        print(f"Average Runs Per Match: {average_runs(df)}")

        print("\nRuns Against Each Opponent (Top 3):")
        print(runs_by_opponent(df).head(3))

        print(f"\nNumber of 50s: {count_fifties(df)}")
        print(f"Number of Centuries: {count_centuries(df)}")

        print("\nCareer Run Progression (First 5 matches):")
        print(career_run_progression(df).head())

        print(f"\nNumber of Consistent Matches (30+ runs):")
        print(f"{consistency_matches(df)}")

        print(f"Number of Not Out Innings:")
        print(f"{not_out_innings(df)}")

        best = best_venue(df)
        print(f"\nBest Venue: {best.index[0]} with {best.values[0]} runs")
