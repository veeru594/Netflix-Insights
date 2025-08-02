import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
data = pd.read_csv("output/cleaned_netflix.csv")

# 1. Dataset Overview
print("\nShape of Dataset:", data.shape)
print("\nData Types:\n", data.dtypes)

# 2. Value counts for type (Movie/TV Show)
print("\nContent Type Counts:\n", data['type'].value_counts())
sns.countplot(data=data, x='type')
plt.title("Distribution of Content Types")
plt.show()

# 3. Top 10 genres
if 'listed_in' in data.columns:
    data['listed_in'] = data['listed_in'].fillna('')
    from collections import Counter
    genre_series = data['listed_in'].str.split(', ')
    all_genres = [genre for sublist in genre_series for genre in sublist]
    genre_counts = Counter(all_genres).most_common(10)

    genres, counts = zip(*genre_counts)
    sns.barplot(x=list(counts), y=list(genres))
    plt.title("Top 10 Genres on Netflix")
    plt.xlabel("Count")
    plt.show()

# 4. Content added per year
if 'date_added' in data.columns:
    data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
    data['year_added'] = data['date_added'].dt.year
    sns.countplot(data=data, y='year_added', order=data['year_added'].value_counts().index)
    plt.title("Content Added Per Year")
    plt.show()

# 5. Top countries
if 'country' in data.columns:
    top_countries = data['country'].value_counts().head(10)
    top_countries.plot(kind='barh')
    plt.title("Top 10 Countries Contributing to Netflix")
    plt.xlabel("Number of Titles")
    plt.show()
