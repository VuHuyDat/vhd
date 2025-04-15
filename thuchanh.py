import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

movie_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

st.write("""Average Movie Budget, Grouped by Genre""")
avg_budget = movie_data.groupby("genre")['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']

fig = plt.figure(figsize = (19, 10))
plt.bar(genre, avg_bud, color = 'lightblue')

st.pyplot(fig)