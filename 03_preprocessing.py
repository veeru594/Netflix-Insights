import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("output/cleaned_netflix.csv")

# Fix missing values
data['country'] = data['country'].fillna("Unknown")
data['rating'] = data['rating'].fillna("Not Rated")

# Fix date format
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data['year_added'] = data['date_added'].dt.year

# Handle duration
data['duration'] = data['duration'].fillna("0")
data['duration_int'] = data['duration'].str.extract(r'(\d+)').astype(int)
data['duration_type'] = data['duration'].str.extract(r'([a-zA-Z ]+)')

# Drop duplicates
data.drop_duplicates(inplace=True)

# Skip 'cast' count because column doesn't exist

# Save cleaned output
data.to_csv("output/processed_netflix.csv", index=False)
print("✅ Netflix data preprocessing complete.")
