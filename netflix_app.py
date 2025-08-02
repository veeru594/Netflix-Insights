import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os
import platform

# -------------------------------
# 🔹 Page Configuration
# -------------------------------
st.set_page_config(
    page_title="🎬 Netflix Insights App",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# 🔹 Load and Prepare Data
# -------------------------------
data = pd.read_csv("output/processed_netflix.csv")
data['primary_genre'] = data['listed_in'].apply(lambda x: str(x).split(',')[0].strip())

# -------------------------------
# 🔹 Sidebar Navigation
# -------------------------------
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio(
    "Go to", 
    ["🏠 Home", "🎯 Recommend", "📊 Python Dashboard", "📈 Interactive", "📥 Power BI", "🗃️ Raw Data"],
    key="main_nav"
)

# -------------------------------
# 🏠 HOME SECTION
# -------------------------------
if page == "🏠 Home":
    st.title(" Netflix Insights App")
    st.markdown("> _Dive deep into global Netflix data — filtered, visualized, and interactive!_")
    st.divider()

    col1, col2= st.columns([2, 1])
   
    with col1:
        st.metric("🎬 Total Titles", len(data))
        st.metric("🌍 Countries Covered", data['country'].nunique())
        st.metric("📅 Year Range", f"{data['release_year'].min()} - {data['release_year'].max()}")
    with col2:
         st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=500)

# -------------------------------
# 🎯 GENRE RECOMMENDER
# -------------------------------
elif page == "🎯 Recommend":
    st.header("🎯 Genre-Based Recommendations")

    genre = st.selectbox("Choose a Genre", sorted(data['primary_genre'].dropna().unique()))
    rating = st.selectbox("Choose Rating", sorted(data['rating'].dropna().unique()))

    filtered = data[
        (data['primary_genre'].str.contains(genre, case=False, na=False)) &
        (data['rating'] == rating)
    ]
    st.subheader(f"Top 5 Titles for Genre: {genre} and Rating: {rating}")
    st.dataframe(filtered[['title', 'type', 'release_year', 'rating', 'country']].head(5))

# -------------------------------
# 📊 PYTHON DASHBOARD
# -------------------------------
elif page == "📊 Python Dashboard":
    st.header("📊 Netflix Trends & Stats (Python-Based Visuals)")

    # Top Release Years
    top_years = data['release_year'].value_counts().head(10)
    st.subheader("Top 10 Years With Most Releases")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_years.index, y=top_years.values, ax=ax1, palette='viridis')
    st.pyplot(fig1)

    # Movies vs TV Shows
    st.subheader("Movies vs TV Shows")
    type_counts = data['type'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    st.pyplot(fig2)

    # Ratings
    st.subheader("Top Ratings on Netflix")
    top_ratings = data['rating'].value_counts().head(7)
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_ratings.index, y=top_ratings.values, ax=ax3, palette='coolwarm')
    st.pyplot(fig3)

    # Heatmap
    st.subheader("Release Year vs Country Heatmap (Top 5)")
    top_countries = data['country'].value_counts().head(5).index
    heatmap_data = data[data['country'].isin(top_countries)]
    heatmap_table = pd.crosstab(heatmap_data['release_year'], heatmap_data['country'])
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    sns.heatmap(heatmap_table, annot=True, fmt='d', cmap="YlGnBu", ax=ax4)
    st.pyplot(fig4)

# -------------------------------
# 📈 INTERACTIVE CHART
# -------------------------------
elif page == "📈 Interactive":
    st.header("📈 Netflix Releases Over Time (Interactive)")
    fig = px.histogram(data, x='release_year', color='type', title='Netflix Releases Over Years')
    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# 📥 POWER BI SECTION
# -------------------------------
# -------------------------------
# 📥 POWER BI SECTION
# -------------------------------
elif page == "📥 Power BI":
    st.header("📥 Power BI Dashboard")
    st.markdown("""
    Here's a preview of the **Power BI dashboard** created using the Netflix dataset.
    """)

    # Display Power BI dashboard image
    st.image("visuals/image.png", caption="Power BI Dashboard Preview",  use_container_width=True)


    st.markdown("""
    > 📊 This dashboard includes:
    - Total Titles
    - TV vs Movie Split
    - Top Genres
    - Country-wise Breakdown
    - Ratings Distribution

    If you'd like to open and explore the **interactive .pbix file**, use the button below:
    """)

    if st.button("▶️ Launch Power BI Dashboard (.pbix file)"):
        pbix_path = r"C:\Users\veera\Desktop\Netflix_project\Netflix dashboard.pbix"
        if os.path.exists(pbix_path):
            try:
                if platform.system() == "Windows":
                    os.startfile(pbix_path)
                else:
                    st.error("Auto-launch only supported on Windows.")
            except Exception as e:
                st.error(f"Error opening file: {e}")
        else:
            st.error("PBIX file not found. Please check the path.")

# -------------------------------
# 🗃️ RAW DATA
# -------------------------------
elif page == "🗃️ Raw Data":
    st.header("🗃️ View Netflix Raw Dataset")
    st.dataframe(data.head(100))
