# from tkinter import HORIZONTAL
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
import json
from streamlit_lottie import st_lottie


selected = option_menu(
"Pick Your Choice", ['Books'],icons=[':movies:', ':books:',":tv:"],menu_icon="cast")


if selected == 'Books':

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_kq5rGs.json")

    def recommend(book_name):
        book_index = np.where(pt.index==book_name)[0][0]
        distances = similarity[book_index]
        books_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:11]
        recommended_books = []
        recommended_books_posters = []
        author= []
        year=[]
        publisher=[]

        for i in books_list:
            recommended_books.append(all.iloc[i[0]]['Book-Title'])
            recommended_books_posters.append(all.iloc[i[0]]['Image-URL-L'])
            author.append(all.iloc[i[0]]['Book-Author'])
            year.append(all.iloc[i[0]]['Year-Of-Publication'])
            publisher.append(all.iloc[i[0]]['Publisher'])

        return recommended_books,recommended_books_posters,author,year,publisher


    def selection(bookname):
        books_re,book_posters,author_de,years,pub= recommend(bookname)
        # st.write('Recommended Books')
       
        book_img,book_det=st.columns(2)
        col0,colx=st.columns(2)
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        col7, col8, col9 = st.columns(3)
        with book_img:
            url=book_posters[0]
            st.image(url)
        with book_det:
            st.title(books_re[0])
            st.caption("Author : "+ author_de[0])
            st.caption("Publisher: "+ pub[0])
            st.caption("Year of Publication : "+ str(years[0]))
            

        with col0:
            st.header("Recommended Books")

        with col1:
            st.write(books_re[1])
            url=book_posters[1]
            st.image(url)
        with col2:
            st.write(books_re[2])
            url=book_posters[2]
            st.image(url)
        with col3:
            st.write(books_re[3])
            url=book_posters[3]
            st.image(url)
        with col4:
            st.write(books_re[4])
            url=book_posters[4]
            st.image(url)
        with col5:
            st.write(books_re[5])
            url=book_posters[5]
            st.image(url)

        with col6:
            st.write(books_re[6])
            url=book_posters[6]
            st.image(url)

        with col7:
            st.write(books_re[7])
            url=book_posters[7]
            st.image(url)

        with col8:
            st.write(books_re[8])
            url = book_posters[8]
            st.image(url)

        with col9:
            st.write(books_re[9])
            url = book_posters[9]
            st.image(url)


    books_dict = pickle.load(open('finalratings_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity_scores.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    posters = pickle.load(open('posters.pkl', 'rb'))
    all = pickle.load(open('all.pkl', 'rb'))
    popular_dict = pickle.load(open('popular.pkl', 'rb'))
    popular_books=popular_dict['Book-Title'].values
    books = books_dict['Book-Title'].values
    popular_pics= popular_dict['Image-URL-M'].values



    def top():
        col1, col2, col3,col4,col5= st.columns(5)
        col6, col7, col8,col9,col10= st.columns(5)
        col11, col12, col13,col14,col15= st.columns(5)
        col16, col17, col18,col19,col20= st.columns(5)
        col21, col22, col23,col24,col25= st.columns(5)
        col26, col27, col28,col29,col30= st.columns(5)
        col31, col32, col33,col34,col35= st.columns(5)
        col36, col37, col38,col39,col40= st.columns(5)
        col41, col42, col43,col44,col45= st.columns(5)
        col46, col47, col48,col49,col50= st.columns(5)
        
        with col1:
            st.write(popular_books[0])
            st.image(popular_pics[0])
        with col2:
            st.write(popular_books[1])
            st.image(popular_pics[1])
        with col3:
            st.write(popular_books[2])
            st.image(popular_pics[2])    
        with col4:
            st.write(popular_books[3])
            st.image(popular_pics[3])
        with col5:
            st.write(popular_books[4])
            st.image(popular_pics[4])    
        with col6:
            st.write(popular_books[5])
            st.image(popular_pics[5])
        with col7:
            st.write(popular_books[6])
            st.image(popular_pics[6])
        with col8:
            st.write(popular_books[7])
            st.image(popular_pics[7])    
        with col9:
            st.write(popular_books[8])
            st.image(popular_pics[8])
        with col10:
            st.write(popular_books[9])
            st.image(popular_pics[9])  
        with col11:
            st.write(popular_books[10])
            st.image(popular_pics[10])
        with col12:
            st.write(popular_books[11])
            st.image(popular_pics[11])
        with col13:
            st.write(popular_books[12])
            st.image(popular_pics[12])    
        with col14:
            st.write(popular_books[13])
            st.image(popular_pics[13])
        with col15:
            st.write(popular_books[14])
            st.image(popular_pics[14])    
        with col16:
            st.write(popular_books[15])
            st.image(popular_pics[15])
        with col17:
            st.write(popular_books[16])
            st.image(popular_pics[16])
        with col18:
            st.write(popular_books[17])
            st.image(popular_pics[17])    
        with col19:
            st.write(popular_books[18])
            st.image(popular_pics[18])
        with col20:
            st.write(popular_books[19])
            st.image(popular_pics[19])
        with col21:
            st.write(popular_books[20])
            st.image(popular_pics[20])
        with col22:
            st.write(popular_books[21])
            st.image(popular_pics[21])
        with col23:
            st.write(popular_books[22])
            st.image(popular_pics[22])    
        with col24:
            st.write(popular_books[23])
            st.image(popular_pics[23])
        with col25:
            st.write(popular_books[24])
            st.image(popular_pics[24])    
        with col26:
            st.write(popular_books[25])
            st.image(popular_pics[25])
        with col27:
            st.write(popular_books[26])
            st.image(popular_pics[26])
        with col28:
            st.write(popular_books[27])
            st.image(popular_pics[27])    
        with col29:
            st.write(popular_books[28])
            st.image(popular_pics[28])
        with col30:
            st.write(popular_books[29])
            st.image(popular_pics[29]) 
        with col31:
            st.write(popular_books[30])
            st.image(popular_pics[30])
        with col32:
            st.write(popular_books[31])
            st.image(popular_pics[31])
        with col33:
            st.write(popular_books[32])
            st.image(popular_pics[32])    
        with col34:
            st.write(popular_books[33])
            st.image(popular_pics[33])
        with col35:
            st.write(popular_books[34])
            st.image(popular_pics[34])    
        with col36:
            st.write(popular_books[35])
            st.image(popular_pics[35])
        with col37:
            st.write(popular_books[36])
            st.image(popular_pics[36])
        with col38:
            st.write(popular_books[37])
            st.image(popular_pics[37])    
        with col39:
            st.write(popular_books[38])
            st.image(popular_pics[38])
        with col40:
            st.write(popular_books[39])
            st.image(popular_pics[39]) 
        with col41:
            st.write(popular_books[40])
            st.image(popular_pics[40])
        with col42:
            st.write(popular_books[41])
            st.image(popular_pics[41])
        with col43:
            st.write(popular_books[42])
            st.image(popular_pics[42])    
        with col44:
            st.write(popular_books[43])
            st.image(popular_pics[43])
        with col45:
            st.write(popular_books[44])
            st.image(popular_pics[44])    
        with col46:
            st.write(popular_books[45])
            st.image(popular_pics[45])
        with col47:
            st.write(popular_books[46])
            st.image(popular_pics[46])
        with col48:
            st.write(popular_books[47])
            st.image(popular_pics[47])    
        with col49:
            st.write(popular_books[48])
            st.image(popular_pics[48])
        with col50:
            st.write(popular_books[49])
            st.image(popular_pics[49])                      
    

    right,left =st.columns(2)
    with right:
        st.title("Book Recommender")
        selected_book =st.selectbox("select your favorite book",books)
    # with left:
    #     st_lottie(lottie_hello, height=400, key="hello")
    if st.button('Search'):
        selection(selected_book)
    if st.button('Top 50 Books'):
        top()
