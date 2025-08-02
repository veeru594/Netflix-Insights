import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the preprocessed dataset
data = pd.read_csv("output/processed_netflix.csv")

# Fix styling
# plt.style.use("seaborn-darkgrid")  


# ================================
# 1️⃣ Bar Chart: Top 10 Years With Most Releases
# ================================
top_years = data['release_year'].value_counts().head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_years.index, y=top_years.values, palette='viridis')
plt.title("Top 10 Years With Most Netflix Releases")
plt.xlabel("Year")
plt.ylabel("Number of Titles Released")
plt.tight_layout()
plt.show()

# ================================
# 2️⃣ Pie Chart: Movie vs TV Show
# ================================
type_counts = data['type'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=["#ff9999", "#66b3ff"])
plt.title("Content Type Distribution (Movie vs TV Show)")
plt.tight_layout()
plt.show()

# ================================
# 3️⃣ Bar Chart: Most Common Ratings
# ================================
top_ratings = data['rating'].value_counts().head(7)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_ratings.index, y=top_ratings.values, palette='coolwarm')
plt.title("Top Content Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ================================
# 4️⃣ Heatmap: Year vs Country for Top Producers
# ================================
top_countries = data['country'].value_counts().head(5).index
heatmap_data = data[data['country'].isin(top_countries)]
heatmap_table = pd.crosstab(heatmap_data['release_year'], heatmap_data['country'])
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_table, cmap='YlGnBu', annot=True, fmt='d')
plt.title("Heatmap: Release Year vs Country (Top 5)")
plt.tight_layout()
plt.show()

# ================================
# 5️⃣ Interactive Plot: Releases Over Time by Type
# ================================
fig = px.histogram(data, x='release_year', color='type', title='Netflix Releases Over Years')
fig.show()
