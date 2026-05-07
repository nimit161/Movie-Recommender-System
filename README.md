# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using Machine Learning, NLP, and Streamlit.  
This project recommends movies similar to a selected movie using metadata such as genres, cast, crew, keywords, and movie overviews.

---

# 🚀 Live Demo

🔗 Deployed App:  
https://movie-recommender-system-j5gisbxv89f4acbsmrje3q.streamlit.app/

---

# 📌 Project Overview

This project uses the TMDB 5000 Movie Dataset to perform:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Content-Based Recommendation System
- Web App Deployment using Streamlit Cloud

The recommendation engine suggests movies similar to the selected movie based on content similarity using Natural Language Processing (NLP) techniques.

---

# 🧠 Features

✅ Movie Recommendation System  
✅ Fetches Real Movie Posters from TMDB API  
✅ Interactive Streamlit Web Interface  
✅ Content-Based Filtering  
✅ Cosine Similarity Algorithm  
✅ NLP-based Recommendation Logic  
✅ Cloud Deployment using Streamlit Community Cloud

---

# 📂 Dataset Information

The project uses two TMDB datasets:

### 1. Movies Dataset
Contains:
- Movie title
- Genres
- Keywords
- Overview
- Popularity
- Vote average
- Revenue
- Release date
- Budget

### 2. Credits Dataset
Contains:
- Cast information
- Crew information
- Directors
- Actors

These datasets are merged using movie IDs to create a complete movie metadata dataset.

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests
- Joblib
- Matplotlib
- Seaborn

---

# 🔍 Machine Learning Workflow

## 1. Data Preprocessing
- Handled missing values
- Extracted important features
- Converted JSON-like columns into usable text
- Combined metadata into tags

## 2. NLP Processing
- Tokenization
- Stemming
- Text vectorization using CountVectorizer

## 3. Similarity Calculation
- Cosine similarity used to measure movie similarity

## 4. Recommendation Generation
- Top 5 similar movies are recommended

---

# 🖥️ Streamlit Web App

The application allows users to:

- Select a movie from dropdown
- Get top 5 similar movie recommendations
- View movie posters dynamically fetched using TMDB API

---

# 📁 Project Structure

```bash
movie-recommender-system/
│
├── app.py
├── requirements.txt
├── Procfile
├── setup.sh
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
