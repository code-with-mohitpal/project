Exam Marks Statistics Project
Hello developers! Welcome to the Exam Marks Statistics Project! 📊✏️

Chef is building an analytics tool to understand student exam performance using numerical data. Schools often collect exam marks, but raw numbers alone don’t provide meaningful insights.

Chef wants to analyze exam scores to:

Understand overall class performance
Identify high-performing students
Detect failing students
Find the highest and lowest scores
Your task is to use the NumPy Library to transform raw exam marks into useful statistical insights.

What’s Already Provided
You are given a single file: main.py

All required function names are already defined.
The program flow is already set up.
You only need to fill in the missing logic (__________) using the NumPy Library.
Do NOT change function names or print statements.
Dataset
You will work with the following exam marks dataset:

78, 85, 33, 66, 15, 88, 90, 59, 29, 70
Each value represents a student’s exam score

Your Tasks
Load Exam Marks
Inside the function load_data():

Create a NumPy array containing the given exam marks.
We are returning the NumPy array so that it can be reused in other functions.
Docs: np.array() function
Compute Class Statistics
Inside the function compute_statistics():

Compute:
Average marks
Median marks
Standard deviation (rounded to 2 decimal places)
Docs: np.mean() function, np.median() function, np.std() function, round() function
Analyze Student Performance
Inside the function analyze_performance():

Using the exam marks and average marks:
Identify students who scored above average
Count how many students scored above average
Identify students who failed (marks < 35)
Count the number of failed students
Docs: len() function
Find Highest and Lowest Scores
Inside the function find_extremes():

Determine:
Highest exam score
Lowest exam score
Docs: np.argmax() function, np.argmin() function
Expected Output:

import numpy as np

# 1. Load exam marks data
def load_data():
    
    # Create and return a NumPy array containing exam marks.
    # Marks to use: 78, 85, 33, 66, 15, 88, 90, 59, 29, 70
    
    # TODO: Create a NumPy array with the marks listed above
    marks = np.array([78, 85, 33, 66, 15, 88, 90, 59, 29, 70])
    
    print("Exam Marks: ", marks)
    
    # Returning the marks array
    return marks



# 2. Compute and print basic statistics

def compute_statistics(marks):
    
    # Calculate the average (mean) marks
    average = np.mean(marks)
    
    # Calculate the median marks
    median = np.median(marks)
    
    # Calculate the standard deviation
    std_deviation = np.std(marks)

    print("\n--- Class Statistics ---")
    print("Average Marks:", average)
    print("Median Marks:", median)
    print("Standard Deviation:", std_deviation)

    # Returning all three values as a tuple
    return average, median, std_deviation

# 3. Analyze and print performance insights
def analyze_performance(marks, average_marks):
    """
    Analyze performance: Find students above average and those who failed.
    """
    # Filter marks greater than average
    above_average = marks[marks > average_marks]
    
    # Filter marks less than 35 (Fail threshold)
    failed_students = marks[marks < 35]

    print("\n--- Performance Insights ---")
    print("Students scoring above average:", above_average)
    print("Number of students above average:", len(above_average))

    print("\nStudents who failed (marks < 35):", failed_students)
    print("Number of failed students:", len(failed_students))
    
    return above_average, failed_students



# 4. Find and print highest and lowest scorer
def find_extremes(marks):
    """
    Find the highest and lowest scores.
    """
    # Find the maximum score
    highest_score = np.max(marks)
    
    # Find the minimum score
    lowest_score = np.min(marks)

    print("\n--- Extremes ---")
    print("Highest Score:", highest_score)
    print("Lowest Score:", lowest_score)

    return highest_score, lowest_score
