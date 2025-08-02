import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned Netflix dataset
data = pd.read_csv("output/processed_netflix.csv")

# Confirm it loaded correctly
print("✅ Dataset Loaded:")
print(data.head())


sns.countplot(data=data, x='year_added', hue='type')
plt.xticks(rotation=45)
plt.title("Movies vs TV Shows Added Each Year")
plt.show()

sns.boxplot(x='type', y='duration_int', data=data)
plt.title("Duration Comparison: Movies vs TV Shows")
plt.show()


top_countries = data['country'].value_counts().head(10)
sns.barplot(y=top_countries.index, x=top_countries.values)
plt.title("Top 10 Content-Producing Countries")
plt.xlabel("Number of Titles")
plt.show()



sns.countplot(y='rating', data=data, order=data['rating'].value_counts().index)
plt.title("Distribution of Ratings")
plt.show()



# If 'listed_in' is included
from collections import Counter
import seaborn as sns

data['listed_in'] = data['listed_in'].fillna('')
data['genre_clean'] = data['listed_in'].str.split(',').apply(lambda x: x[0])  # Take primary genre

genre_type = pd.crosstab(data['genre_clean'], data['type'])
sns.heatmap(genre_type, annot=True, fmt='d', cmap="YlGnBu")
plt.title("Genre vs Content Type")
plt.show()

