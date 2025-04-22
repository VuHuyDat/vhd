import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

movies_data = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

movies_data = movies_data.dropna(subset=['score', 'genre', 'year'])

st.title("Phân tích dữ liệu")
st.sidebar.header("Bộ lọc")
st.write("Nhóm sinh viên thực hiện:")
st.write("Vũ Huy Đạt - 2321050062")
st.write("Phạm Đại Đồng - 2321050059")


st. write("Dữ liệu đã qua xử lý:")
st.dataframe(movies_data)

genres = movies_data['genre'].unique()
selected_genres = st.sidebar.multiselect("Chọn thể loại phim:", options=genres, default=['Animation', 'Horror', 'Fantasy', 'Romance'])

filtered_movies = movies_data[
    (movies_data['genre'].isin(selected_genres))
]

# Hiển thị bảng phim đã lọc
if filtered_movies.empty:
    st.write("Không có phim nào khớp với bộ lọc của bạn!")
else:
    st.write("Danh sách phim đã lọc theo thể loại phim (Thông qua bảng bộ lọc):")
    st.dataframe(filtered_movies[['name', 'genre', 'year']])

    # Đếm số lượng phim theo thể loại
    genre_counts = filtered_movies['genre'].value_counts()

    # Vẽ biểu đồ cột
    st.write("Biểu đồ số lượng phim theo thể loại:")
    plt.figure(figsize=(10, 6))
    plt.bar(genre_counts.index, genre_counts, color='lightgreen', edgecolor='black')

    st.subheader("Điểm đánh giá trung bình theo năm")
    avg_score_by_year = data.groupby('year')['score'].mean().reset_index()

    fig1, ax1 = plt.subplots(figsize=(12, 5))
    plt.lineplot(data=avg_score_by_year, x='year', y='score', ax=ax1, marker='o', color='orange')
    ax1.set_title("Score trung bình theo năm")
    st.pyplot(fig1)
    
    plt.xlabel('Thể loại (Genre)')
    plt.ylabel('Số lượng phim')
    plt.title('Số lượng phim theo thể loại')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)
