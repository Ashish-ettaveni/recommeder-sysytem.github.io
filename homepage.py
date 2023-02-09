from tkinter import HORIZONTAL
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
import json
from streamlit_lottie import st_lottie



# st.title("main Page")
# if 'key' not in st.session_state:
#     st.session_state['key'] = 'value'

selected = option_menu(
"Pick Your Choice", ['Books'],icons=[':movies:', ':books:',":tv:"],menu_icon="cast",
orientation = HORIZONTAL
)



if selected == 'Books':

   



    

    # if selected_opt=='Top 50 Books':
    #    
        

   
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
        
        
####################################################################        

# if selected == 'Movies':
#     movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
#     movies = pd.DataFrame(movies_dict)
#     movie_dictionary = pickle.load(open('dictionary.pkl', 'rb'))
#     similarity = pickle.load(open('similarity.pkl', 'rb'))
#     cast = pickle.load(open('cast.pkl', 'rb'))
#     votes= pickle.load(open('votes.pkl', 'rb'))



#     def load_lottieurl(url: str):
#         r = requests.get(url)
#         if r.status_code != 200:
#            return None
#         return r.json()


#     def fetch_poster(movies_id):
#         response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=306d75e9feb743e9c797d7329dfa20ae&language=en-US'.format(movies_id))
#         data = response.json()
#         try:
#             return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
#         except:
#             return     


#     def recommend(movie):
#         movie_index = movies[movies['title'] == movie].index[0]
#         distances = similarity[movie_index]
#         movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:16]
#         recommended_movies = []
#         recommended_movies_posters = []
#         movie_details = []
#         cast_d=[]
#         votes_details=[]
#         for i in movies_list:
#             movies_id = movies.iloc[i[0]].movie_id
#             movie_details.append(movie_dictionary.iloc[i[0]])
#             recommended_movies.append(movies.iloc[i[0]].title)
#             cast_d.append(cast.iloc[i[0]])
#             votes_details.append(votes.iloc[i[0]])
#             recommended_movies_posters.append(fetch_poster(movies_id))

#         return recommended_movies, recommended_movies_posters, movie_details,cast_d,votes_details




#     lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_feuwapl6.json")
#     lottie_end = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_bb9bkg1h.json")

#     left, right = st.columns(2)
#     with left:
#         st.title('Movie Recommender')

#         selected_movie_name = st.selectbox('search your favourite movie for recommendation',movies['title'].values)
#         st.session_state['key']=selected_movie_name

#     with right:
#         st_lottie(lottie_hello, height=300, key="hello")


#     def selection(selected_movie_name):
#         names=[]
#         images=[]
#         movie_details=[]
#         names, images, movie_details,cast_details,votes_de= recommend(selected_movie_name)
#         searched_image, searched_info = st.columns((1, 2))
#         with searched_image:
#             st.image(images[0])
#         with searched_info:
#             st.header(names[0])
#             st.write("Overview")
#             st.write(movie_details[0])
#             st.write("Cast :"+cast_details[0])
#             st.write("average votes:"+str(votes_de[0]))


#         st.write('Recommended movies')
#         col1, col2, col3 = st.columns(3)
#         col4, col5, col6 = st.columns(3)
#         col7, col8, col9 = st.columns(3)
#         col10, col11, col12 = st.columns(3)
#         col13, col14, col15 = st.columns(3)

#         with col1:
#             try:
#                 st.write(names[1])
#                 st.image(images[1])
#                 st.write("average votes:"+str(votes_de[1]))
#             except:
#                 pass
                
            

#         with col2:
#             try:
#                 st.write(names[2])
#                 st.image(images[2])
#                 st.write("average votes:" + str(votes_de[2]))
#             except:
#                 pass

#         with col3:
#             try:
#                 st.write(names[3])
#                 st.image(images[3])
#                 st.write("average votes:" + str(votes_de[3]))
#             except:
#                 pass
#         with col4:
#             try:
#                 st.write(names[4])
#                 st.image(images[4])
#                 st.write("average votes:"+str(votes_de[4]))
#             except:
#                 pass
#         with col5:
#             try:
#                 st.write(names[5])
#                 st.image(images[5])
#                 st.write("average votes:" + str(votes_de[5]))
#             except:
#                 pass
#         with col6:
#             try:
#                 st.write(names[6])
#                 st.image(images[6])
#                 st.write("average votes:" + str(votes_de[6]))
#             except:
#                 pass
#         with col7:
#             try:
#                 st.write(names[7])
#                 st.image(images[7])
#                 st.write("average votes:" + str(votes_de[7]))
#             except:
#                 pass
#         with col8:
#             try:
#                 st.write(names[8])
#                 st.image(images[8])
#                 st.write("average votes:" + str(votes_de[8]))
#             except:
#                 pass
#         with col9:
#             try:
#                 st.write(names[9])
#                 st.image(images[9])
#                 st.write("average votes:" + str(votes_de[9]))
#             except:
#                 pass
#         with col10:
#             try:
#                 st.write(names[10])
#                 st.image(images[10])
#                 st.write("average votes:" + str(votes_de[10]))
#             except:
#                 pass
#         with col11:
#             try:
#                 st.write(names[11])
#                 st.image(images[11])
#                 st.write("average votes:" + str(votes_de[11]))
#             except:
#                 pass
#         with col12:
#             try:
#                 st.write(names[12])
#                 st.image(images[12])
#                 st.write("average votes:" + str(votes_de[12]))
#             except:
#                 pass
#         with col13:
#             try:
#                 st.write(names[13])
#                 st.image(images[13])
#                 st.write("average votes:" + str(votes_de[13]))
#             except:
#                 pass
#         with col14:
#             try:
#                 st.write(names[14])
#                 st.image(images[14])
#                 st.write("average votes:" + str(votes_de[14]))
#             except:
#                 pass
#         with col15:
#             try:
#                 st.write(names[15])
#                 st.image(images[15])
#                 st.write("average votes:" + str(votes_de[15]))
#             except:
#                 pass
    
    

#     if st.button('Search'):
#         selection(selected_movie_name)


#     st_lottie(lottie_end, height=300, key="end")

#####################################################################################################

# if selected == "Series":
#     def load_lottieurl(url: str):
#         r = requests.get(url)
#         if r.status_code != 200:
#            return None
#         return r.json()

    # def recommend(series_name):
    #     series_index = series_dict[series_dict['title']== series_name].index[0]
    #     distances=series_similarity[series_index]
    #     series_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:16]

    #     recommended_series=[]
    #     recommended_overview=[]
    #     for i in series_list:
    #         recommended_series.append(series_dict.iloc[i[0]]['title'])
    #         recommended_overview.append(series_dict.iloc[i[0]]['description'])
    #     return recommended_series,recommended_overview    

    # def recommend1(series_name):
    #     series_index=series_d[series_d['title']== series_name].index[0]
    #     distances=series_similarity[series_index]
    #     movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[0:16]
    #     recommended_series=[]
    #     recommended_overview=[]
    #     recommended_directors=[]
    #     recomended_type=[]
    #     recomended_platform=[]
    #     for i in movies_list:
    #         recommended_series.append(series_d.iloc[i[0]]['title'])
    #         recommended_overview.append(series_d.iloc[i[0]]['description'])
    #         recommended_directors.append(series_d.iloc[i[0]]['director'])
    #         recomended_type.append(series_d.iloc[i[0]]['type'])
    #         recomended_platform.append(series_d.iloc[i[0]]['platform'])
    #     return recommended_series,recommended_overview,recommended_directors,recomended_type,recomended_platform
            


    # # for i in range( len(recommended_series))  :
    # #     id = recommended_series[i].getID()
    # #     movies = ia.get_movie(id)
    # #

    # # for movie in movies:
    # #     url=movie['cover url']
    # #     posters.append(url)
    # # movies=[]
    # # movie_ids=[]
    # # for i in recommended_series:
    # #     movies = ia.search_movie(i)
    # #     movieid = movies[0].movieID

    # #     movie_ids.append(movieid)

        






    # def selection1(selected_series_name):

    #     series_details,ser_rec_overview,directors,types,platforms = recommend1(selected_series_name)
    # # posters=[]
    # # for i in ids:
    # #     series = ia.get_movie(i)
    # #     cover = series.data['cover url']
    # #     posters.append(cover)



    #     searched_image, searched_info = st.columns((1, 2))
    #     with searched_image:
    #         st.text(series_details[0])
    #     with searched_info:
    #         st.header(series_details[0])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[0])
    #         st.write("Director : " + str(directors[0]))
    #         st.write("Type : "+ types[0])
    #         st.write("Platform :"+ platforms[0])

    #     st.write('Recommended Series')
    #     col1, col2 = st.columns(2)
    #     col3, col4 = st.columns(2)
    #     col5, col6= st.columns(2)
    #     col7, col8 = st.columns(2)
    #     col9, col10 = st.columns(2)
    #     col11,col12 =st.columns(2)
    #     col13,col14 =st.columns(2)

    #     with col1:
    #         st.subheader(series_details[1])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[1])
    #         st.write("Director : " + str(directors[1]))
    #         st.write("Type : "+ types[1])
    #         st.write("Platform :"+ platforms[1])

    #     with col2:
    #         st.subheader(series_details[2])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[2])
    #         st.write("Director : " + str(directors[2]))
    #         st.write("Type : "+ types[2])
    #         st.write("Platform :"+ platforms[2])

    #     with col3:
    #         st.subheader(series_details[3])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[3])
    #         st.write("Director : " + str(directors[3]))
    #         st.write("Type : "+ types[3])
    #         st.write("Platform :"+ platforms[3])
   
    #     with col4:
    #         st.subheader(series_details[4])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[4])
    #         st.write("Director : " + str(directors[4]))
    #         st.write("Type : "+ types[4])
    #         st.write("Platform :"+ platforms[4])

    #     with col5:
    #         st.subheader(series_details[5])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[5])
    #         st.write("Director : " + str(directors[5]))
    #         st.write("Type : "+ types[5])
    #         st.write("Platform :"+ platforms[5])
   
    #     with col6:
    #         st.subheader(series_details[6])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[6])
    #         st.write("Director : " + str(directors[6]))
    #         st.write("Type : "+ types[6])
    #         st.write("Platform :"+ platforms[6])

    #     with col7:
    #         st.subheader(series_details[7])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[7])
    #         st.write("Director : " + str(directors[7]))
    #         st.write("Type : "+ types[7])
    #         st.write("Platform :"+ platforms[7])

    #     with col8:
    #         st.subheader(series_details[8])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[8])
    #         st.write("Director : " + str(directors[8]))
    #         st.write("Type : "+ types[8])
    #         st.write("Platform :"+ platforms[8])
   
    #     with col9:
    #         st.subheader(series_details[9])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[9])
    #         st.write("Director : " + str(directors[9]))
    #         st.write("Type : "+ types[9])
    #         st.write("Platform :"+ platforms[9])

    #     with col10:
    #         st.subheader(series_details[10])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[10])
    #         st.write("Director : " + str(directors[10]))
    #         st.write("Type : "+ types[10])
    #         st.write("Platform :"+ platforms[0])
  
    #     with col11:
    #         st.subheader(series_details[11])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[11])
    #         st.write("Director : " + str(directors[11]))
    #         st.write("Type : "+ types[11])
    #         st.write("Platform :"+ platforms[11])

    #     with col12:
    #         st.subheader(series_details[12])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[12])
    #         st.write("Director : " + str(directors[12]))
    #         st.write("Type : "+ types[12])
    #         st.write("Platform :"+ platforms[12])

    #     with col13:
    #         st.subheader(series_details[13])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[13])
    #         st.write("Director : " + str(directors[13]))
    #         st.write("Type : "+ types[13])
    #         st.write("Platform :"+ platforms[13])
    
    #     with col14:
    #         st.subheader(series_details[14])
    #         st.write("Overview")
    #         st.write(ser_rec_overview[14])
    #         st.write("Director : " + str(directors[14]))
    #         st.write("Type : "+ types[14])
    #         st.write("Platform :"+ platforms[14])

        

        


    # lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_qm8eqzse.json")

    # series_dict = pickle.load(open('series2.pkl', 'rb'))
    # series_d= pd.DataFrame(series_dict)

    # series=series_dict['title'].values
    # series_overview=series_dict['description'].values
    # directors=series_dict['director'].values
    # types=series_dict['type'].values
    # platforms=series_dict['platform'].values
    # series_similarity = pickle.load(open('similarity_series2.pkl', 'rb'))

    # left,right = st.columns(2)
    # with left:
    #     st.title("Series Recommenders")
    #     selected_series = st.selectbox("select the series", series_d['title'].values)
    # with right:
    #     st_lottie(lottie_hello, height=400, key="hello")
        

    # if st.button("Search"):
    #     selection1(selected_series)

