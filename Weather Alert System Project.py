# Weather Alert System Project
# Hello developers! Welcome to the Weather Alert System Project! 🌧️⚡

# Modern cities rely heavily on digital weather sensors to monitor environmental conditions. However, raw sensor readings often contain errors - negative glitches, extreme spikes, or unusual values that make the data unreliable.

# Chef has been tasked with building a safety dashboard for a smart-city monitoring system. Your task is to clean incoming weather data to extract meaningful insights so the city can respond quickly to hazardous conditions.

# Chef wants to analyze exam scores to:

# Understand overall class performance
# Identify high-performing students
# Detect failing students
# Find the highest and lowest scores
# Your task is to use the NumPy Library to transform raw exam marks into useful statistical insights.

# What’s Already Provided
# You are given a single file: main.py

# All required function names are already defined.
# The program flow is already set up.
# You only need to complete in the missing logic.
# Do NOT change function names or print statements.
# Dataset
# You will work with sensor readings stored in a CSV file named weather_data.csv.

# It contains the following columns:
# Temp: The raw temperature reading in Celsius (°C) recorded by the sensor.
# Dataset Preview (First 5 rows):
# 22 
# 25
# 28
# 30
# -5
# Your Tasks
# Load Sensor Data
# Inside load_weather_data():

# Read the CSV file
# Convert it to a NumPy array.
# Flatten it into a 1D array and then return the flattened array
# Docs: pd.read_csv() documentation | .to_numpy() documentation | .flatten() documentation
# Detect Extreme Heat Alerts
# Inside the function detect_heat_alerts():

# Create a boolean mask where True means the temperature is greater than 40°C.
# This helps identify which sensors are reporting dangerous heatwaves.
# Docs: Boolean Indexing (Masks)
# Fix Broken Sensor Readings
# Inside the function replace_negative_values():

# Sensors sometimes malfunction and report negative numbers (e.g., -5).
# Replace negative values with 0.
# Keep all positive values as they are.
# Docs: np.where() documentation
# Enforce Safe Operating Range
# Inside the function clip_temperature_range():

# The system can only process values between 0°C and 45°C.
# Any value greater than 45 should become 45.
# Any value less than 0 should become 0.
# Docs:np.clip() documentation
# Audit Critical Zones
# Inside the function monitor_critical_zones():

# The city manager wants to check specific high-priority sensors.
# Extract readings at indices 4, 9, and 11.
# Index 4 (Server Room)
# Index 9 (Battery Storage)
# Index 11 (Main Hall)
# Docs: Fancy Indexing (Integer Array Indexing)
# Convert to Fahrenheit
# Inside the function convert_to_fahrenheit():

# Convert the cleaned Celsius readings to Fahrenheit for the dashboard.
# Formula: 
# F
# =
# (
# C
# ×
# 1.8
# )
# +
# 32
# F=(C×1.8)+32
# Use broadcasting to apply this formula to the entire array at once.
# Docs: NumPy Broadcasting Rules
# Expected Output:

# Data Loading:
# Successfully loaded 20 records.
# Raw Data: [22 25 28 30 -5 35 42 48 55 60 18 15 -2  0 10  5 50 41 33 29]

# Heatwave Detection (>40°C):
# Alert Mask: [0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0]
# Result: Found 6 sensors reporting critical heat.

# Sensor Glitch Correction:
# Logic: Replaced negative values with 0.
# Cleaned Data: [22 25 28 30  0 35 42 48 55 60 18 15  0  0 10  5 50 41 33 29]

# Safety Limit Enforcement:
# Logic: Clipped values > 45°C to strictly 45.
# Safe Data: [22 25 28 30  0 35 42 45 45 45 18 15  0  0 10  5 45 41 33 29]

# Critical Zone Audit:
# Zones Checked: Server Room (Idx 4), Battery (Idx 9), Hall (Idx 11)
# Readings: [ 0 45 15]

# Dashboard Display Conversion:
# Data in Fahrenheit: [ 71.6  77.   82.4  86.   32.   95.  107.6 113.  113.  113.   64.4  59.
#   32.   32.   50.   41.  113.  105.8  91.4  84.2]             





import numpy as np
import pandas as pd


# 1. Loading Weather Data
def load_weather_data(filename):
    """
    Load data using Pandas read_csv.
    """
    try:
        # Load the CSV file
        df = pd.read_csv(filename)
        
        # Convert the DataFrame to a 1D NumPy array (flattened)
        return df.to_numpy().flatten()
        
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return np.array([])


# 2. Identify Extreme Heat Alerts
def detect_heat_alerts(temps):
    """ Return True for any sensor reading above 40°C. """
    
    # Generate a boolean mask where temperatures exceed 40
    return temps > 40


# 3. Fix Sensor Errors
def replace_negative_values(temps):
    """
    Replace negative values with 0.
    """
    # Replace values < 0 with 0
    return np.where(temps < 0, 0, temps)


# 4. Enforce Safe Limits
def clip_temperature_range(temps, low=0, high=45):
    """
    Clip values to a max of 45°C.
    """
    # Restrict the array values to the [low, high] interval
    return np.clip(temps, low, high)


# 5. Monitor Critical Infrastructure
def monitor_critical_zones(temps):
    """
    Check specific high-interest zones:
    - Index 4: Had a glitch (-5) -> Should now be 0
    - Index 9: Was extreme (60) -> Should now be 45
    - Index 11: Normal value (15)
    """
    # Extract readings from specific indices
    result = temps[[4, 9, 11]]
    return result


# 6. Convert to Fahrenheit
def convert_to_fahrenheit(temps):
    """ Convert Celsius to Fahrenheit. """
    # Apply the standard conversion formula using broadcasting
    return (temps * 1.8) + 32
