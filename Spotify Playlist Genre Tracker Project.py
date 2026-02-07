# Spotify Playlist Genre Tracker Project
# Hello developers! Welcome to the Spotify Playlist Genre Tracker Project! 🎶🎤

# Chef loves music, especially discovering trends across his growing Spotify playlist. He has collected dozens of Bollywood, Pop, Rock, Hip-Hop, and R&B tracks.

# But simply looking at long lists of songs doesn’t reveal much insight. Chef needs your help to analyze his playlist and answer questions like:

# Which genre dominates his playlist?
# Which artists contribute the most songs?
# How popular is each genre on average?
# Your task is to use the Pandas Library to clean and summarize Spotify playlist data and uncover meaningful listening patterns.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete the missing logic.
# Do NOT change function names or print statements.
# Dataset
# You will work with a CSV file named spotify_playlist.csv.

# It contains the following columns:
# Track: Name of the song (e.g., "Blinding Lights", "Kesariya").
# Artist: Name of the singer or band (e.g., "The Weeknd", "Arijit Singh").
# Genre: The musical category (Pop, Bollywood, Rock, Hip-Hop, R&B).
# Duration: Length of the song in seconds.
# Popularity: A score from 0 to 100 indicating how trending the song is.
# Dataset Preview (First 5 rows):
# Kesariya,Arijit Singh,Bollywood,232,85
# Kesariya,Arijit Singh,Bollywood,232,85
# Tum Hi Ho,Arijit Singh,Bollywood,249,92
# Tere Vaaste,Varun Jain,Bollywood,207,78
# Jhoome Jo Pathaan,Arijit Singh,Bollywood,240,88
# Note: The dataset contains duplicates and different popularity scores from 0-100.
# Your Tasks
# Load Playlist Data
# Inside the function load_playlist():

# Read the CSV file into a Pandas DataFrame.
# Return the DataFrame for use in later functions.
# Docs: pandas.read_csv() documentation
# Compute Class Statistics
# Inside the function remove_duplicates():

# The system glitched and added some songs multiple times!
# Drop duplicate rows based on the Track + Artist combination.
# Keep only the first occurrence.
# Docs: pandas.drop_duplicates() documentation
# Count Songs by Genre
# Inside the function count_genre_frequency():

# Determine the frequency of each genre in the playlist.
# We want to know exactly how many songs belong to "Pop", "Rock", "Bollywood", etc.
# Docs: pandas.value_counts() documentation
# Analyze Artist Activity by Genre
# Inside the function group_by_genre_and_artist():

# Break down the dataset by Genre and Artist.
# For every artist within a genre, count the number of tracks they have contributed.
# Docs: pandas.groupby() documentation
# Compute Genre-Level Performance Statistics
# Inside the function compute_genre_stats():

# Create a high-level summary table for each Genre.
# You need to calculate two different metrics at once:
# Total Songs: The count of tracks in that genre.
# Avg Popularity: The average popularity score of that genre.
# Hint: You might need to use a dictionary to specify different operations for different columns.
# Rename the resulting columns to Total_Songs and Avg_Popularity.
# Round values to 2 decimals (Code already written).
# Docs: pandas.agg() documentation | pandas.round() documentation
# Rank Most Active Artists
# Inside the function sort_top_artists():

# Take the grouped artist data from Task 4 and rearrange it.
# The artists with the highest number of tracks should appear at the very top of the list.
# Docs: pandas.sort_values() documentation
# Expected Output:

# Songs Loaded: 52
# After Cleaning Duplicates: 50

# Songs Per Genre:
# Genre
# Bollywood      14
# Pop            13
# Rock            7
# Hip-Hop         7
# R&B             6
# Alternative     3
# Name: count, dtype: int64

# Artist Track Counts (Grouped):
# Genre        Artist         
# Alternative  Billie Eilish      3
# Bollywood    Ali Sethi          1
#              Arijit Singh       9
#              Atif Aslam         1
#              Benny Dayal        1
#              Rahul Sipligunj    1
#              Varun Jain         1
# Hip-Hop      DaBaby             1
#              Drake              3
#              Roddy Ricch        1
# Name: Track, dtype: int64

# Genre Performance Stats:
#              Total_Songs  Avg_Popularity
# Genre                                   
# Alternative            3           88.00
# Bollywood             14           84.36
# Hip-Hop                7           83.00
# Pop                   13           90.15
# R&B                    6           74.83
# Rock                   7           87.86

# Top 5 Most Active Artists:
# Genre        Artist         
# Bollywood    Arijit Singh       9
# Alternative  Billie Eilish      3
# Hip-Hop      Drake              3
# Pop          The Weeknd         3
# Rock         Imagine Dragons    3
# Name: Track, dtype: int64



import pandas as pd


# 1. Load Playlist Data
def load_playlist(filename):
    """
    Load CSV playlist data into a pandas DataFrame.
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Remove Duplicate Tracks
def remove_duplicates(df):
    """
    Remove duplicate songs based on Title + Artist combination.
    """
    # Keep only unique entries based on 'Track' and 'Artist'
    cleaned_df = df.drop_duplicates(subset=["Track", "Artist"])
    return cleaned_df


# 3. Count Genre Popularity
def count_genre_frequency(df):
    """
    Count total songs in each genre.
    """
    # Frequency of each genre
    return df["Genre"].value_counts()


# 4. Analyze Artist Performance by Genre
def group_by_genre_and_artist(df):
    """
    Group by Genre + Artist and count tracks per artist.
    """
    # Group by Genre and Artist, then count Track
    grouped = df.groupby(["Genre", "Artist"])["Track"].count()
    return grouped


# 5. Multi-Aggregation Summary
def compute_genre_stats(df):
    """
    Calculate:
      - Total Songs per genre (count)
      - Average Popularity (mean)
    """
    # Aggregate count of tracks and mean popularity per genre
    stats = df.groupby("Genre").agg({
        "Track": "count",
        "Popularity": "mean"
    })
    
    if not stats.empty:
        # Rename columns
        stats.columns = ["Total_Songs", "Avg_Popularity"]
        return stats.round(2)
    return stats


# 6. Sort Results for Insights
def sort_top_artists(grouped_series):
    """
    Sort grouped Series (Genre + Artist track counts) in descending order.
    """
    # Sort artists by number of tracks (descending)
    return grouped_series.sort_values(ascending=False)
