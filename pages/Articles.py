import streamlit as st
import os
from PIL import Image
st.set_page_config(page_title="Mehraj.AI",page_icon=':brain:',layout="wide")
def article():
    with st.container():
        # This part represents the Title
        st.title("Articles 📰")
        st.markdown("""------------------------------------------""")
        st.write("#")
    #image asset
    image_knn=Image.open("Images/KNN.jpeg")
    #Article Menu
    with st.container():
        #First article
        images1,text1=st.columns((1,2))
        #First article
        with images1:
            st.image(image_knn)
        with text1:
            st.subheader(":red[An Easy explanation of KNN (K-Nearest Neighbour)]")
            st.write("""
                     When we start our journey in machine learning, we come across multiple simple algorithms like Linear Regression, Logistic Regression etc.
                    Among them one of the simplest algorithms is K-Nearest Neighbours (KNN for short). I really like this algorithm due to its simplicity and ease of understanding as it very much aligns itself to the real world. In this article, we're going to understand what KNN is, how it works and its applications in the easiest way possible.
                        [Read More>>](https://www.linkedin.com/pulse/easy-explanation-knn-k-nearest-neighbour-mehrajur-rahman-mirdha/)""")
        
            
            
        


if(__name__=="__main__"):
    article()