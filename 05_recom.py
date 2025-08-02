import pandas as pd

# Step 1: Load the preprocessed Netflix dataset
file_path = "output/processed_netflix.csv"
data = pd.read_csv(file_path)

# Step 2: Display basic info for reference
print("✅ Dataset Loaded Successfully")
print(data[['title', 'type', 'listed_in']].head())

# Step 3: Extract primary genre
# 'listed_in' contains comma-separated genres; we'll take the first one
data['primary_genre'] = data['listed_in'].apply(lambda x: str(x).split(',')[0].strip())

# Step 4: User Genre Selection (you can change this value)
user_genre = "Dramas"  # Change to any genre like 'Action', 'Comedies', 'Horror' etc.
print(f"\n🎯 Recommendations for Genre: {user_genre}\n")

# Step 5: Filter and recommend top 5 titles based on genre
recommended = data[data['primary_genre'].str.contains(user_genre, case=False, na=False)]
recommended = recommended[['title', 'type', 'release_year', 'primary_genre']].head(5)

# Step 6: Display Recommendations
if not recommended.empty:
    print("📽️ Top Recommendations:")
    print(recommended.to_string(index=False))
else:
    print("❌ No recommendations found for this genre. Try another!")
