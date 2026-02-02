Netflix Library Explorer Project
Hello developers! Welcome to the Netflix Library Explorer Project! 📺📊

Chef is building a data exploration tool to analyze Netflix’s content catalog using tabular data. Netflix stores thousands of movies and TV shows, but raw CSV data alone doesn’t provide meaningful insights.

Chef wants to explore the Netflix library to:

Understand the size and structure of the catalog
Discover recently released content
Identify popular content ratings
Your task is to use the Pandas library to transform raw Netflix data into simple, readable insights.

What’s Already Provided
You are given a single file: main.py

All required function names are already defined.
The program flow is already written.
You only need to fill in the missing logic (__________) using the Pandas Library.
Do NOT change function names or print statements.
Dataset
You will work with a Netflix dataset stored in a CSV file:

File name: netflix.csv
The dataset contains information such as:
Title
Content type (Movie / TV Show)
Release year
Rating
Country
Your Tasks
Load Netflix Dataset
Inside the function load_data()
Load the Netflix CSV file using Pandas
Print the first 5 rows showing:
title
type
release_year
Return the Pandas DataFrame so it can be used in other functions
Docs: pd.read_csv(), DataFrame.head()
Explore Dataset Structure
Inside the function explore_dataset(df)
Print:
Shape of the dataset (rows × columns)
List of column names as a Python list
Docs: DataFrame.shape, DataFrame.columns
Analyze Content Distribution
Inside the function count_content_types(df)
Count how many Movies and TV Shows are present
Print the distribution
Docs: Series.value_counts()
Filter Recent Content
Inside the function filter_recent_content(df)
Filter content released after the year 2015
Print the first 5 rows showing:
title
type
release_year
Return the filtered DataFrame
Docs: DataFrame.head()
Find Popular Ratings
Inside the function top_ratings(df)
Identify and print the top 5 most common content ratings
Docs: Series.value_counts(), DataFrame.head()
View Latest Netflix Content
Inside the function sort_by_release_year(df)
Sort content by release_year in descending order
Print the first 5 rows showing:
title
type
release_year
Docs: DataFrame.sort_values(), DataFrame.head()
Expected Output:

Netflix Library Explorer Project

Dataset loaded successfully!

Sample Data (first 5 rows):
                   title     type  release_year
0   Dick Johnson Is Dead    Movie          2020
1          Blood & Water  TV Show          2021
2              Ganglands  TV Show          2021
3  Jailbirds New Orleans  TV Show          2021
4           Kota Factory  TV Show          2021

Dataset Overview:
Shape of the dataset: (8804, 5)
Column Names: ['title', 'type', 'release_year', 'rating', 'country']

Content Type Distribution:
type
Movie      6129
TV Show    2675
Name: count, dtype: int64

Content Released After 2015:
                   title     type  release_year
0   Dick Johnson Is Dead    Movie          2020
1          Blood & Water  TV Show          2021
2              Ganglands  TV Show          2021
3  Jailbirds New Orleans  TV Show          2021
4           Kota Factory  TV Show          2021

Top 5 Content Ratings:
rating
TV-MA    3205
TV-14    2159
TV-PG     863
R         799
PG-13     490
Name: count, dtype: int64

Latest Content on Netflix:
                               title     type  release_year
35    The Father Who Moves Mountains    Movie          2021
8      The Great British Baking Show  TV Show          2021
6   My Little Pony: A New Generation    Movie          2021
5                      Midnight Mass  TV Show          2021
4                       Kota Factory  TV Show          2021






import pandas as pd


# 1. Load Netflix dataset
def load_data():
    """
    Load the Netflix dataset from the CSV file:
    - File path: "./netflix.csv"

    Print:
    - First 5 rows showing: title, type, release_year

    Return:
        Pandas DataFrame
    """

    df = pd.read_csv("./netflix.csv")
    print("Dataset loaded successfully!")

    print("\nSample Data (first 5 rows):")
    print(df[["title", "type", "release_year"]].head())

    return df


# 2. Display basic dataset information
def explore_dataset(df):
    """
    Print:
    - Shape of the dataset
    - Column names of the dataset
    """

    print("\nDataset Overview:")
    print("Shape of the dataset:", df.shape)
    print("Column Names:", list(df.columns))


# 3. Count Movies vs TV Shows
def count_content_types(df):
    """
    Count and print how many Movies and TV Shows are present.
    """

    print("\nContent Type Distribution:")
    content_counts = df["type"].value_counts()
    print(content_counts)


# 4. Filter content released after 2015
def filter_recent_content(df):
    """
    Filter content released after 2015
    """

    recent_content = df[df["release_year"] > 2015]

    print("\nContent Released After 2015:")
    print(recent_content[["title", "type", "release_year"]].head())

    return recent_content


# 5. Top 5 most common ratings
def top_ratings(df):
    """
    Print the top 5 most common content ratings.
    """

    print("\nTop 5 Content Ratings:")
    ratings = df["rating"].value_counts().head(5)
    print(ratings)


# 6. Sort content by release year (latest first)
def sort_by_release_year(df):
    """
    Sort the content by release year in descending order
    and print first 5 rows showing: title, type, release_year
    """

    sorted_df = df.sort_values(by="release_year", ascending=False)

    print("\nLatest Content on Netflix:")
    print(sorted_df[["title", "type", "release_year"]].head())


if __name__ == "__main__":
    print("Netflix Library Explorer Project\n")

    df = load_data()
    explore_dataset(df)
    count_content_types(df)
    recent_df = filter_recent_content(df)
    top_ratings(df)
    sort_by_release_year(df)
