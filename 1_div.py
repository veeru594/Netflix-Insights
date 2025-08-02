import pandas as pd
import numpy as np
import os

# Step 1: Load dataset
file_path = 'Data/netflix1.csv'
data = pd.read_csv(file_path)


# Step 2: View basic information
print("\n--- Dataset Info ---")
print(data.info())

print("\n--- First 5 Rows ---")
print(data.head())

# Step 3: Check for null values
print("\n--- Missing Values ---")
print(data.isnull().sum())

# Step 4: Clean column names
# Remove whitespaces and convert to lowercase
data.columns = [col.strip().lower().replace(' ', '_') for col in data.columns]

# Step 5: Handle date column if present
if 'date_added' in data.columns:
    data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')

# Step 6: Drop rows with all null values
data.dropna(how='all', inplace=True)

# Step 7: Summary stats
print("\n--- Summary Statistics ---")
print(data.describe(include='all'))

# Step 8: Save cleaned version
os.makedirs("output", exist_ok=True)
data.to_csv("output/cleaned_netflix.csv", index=False)
print("\n✅ Cleaned data saved to output/cleaned_netflix.csv")
