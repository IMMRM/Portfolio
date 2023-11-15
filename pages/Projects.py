import streamlit as st
import os
st.set_page_config(page_title="Mehraj.AI",page_icon=':brain:',layout="wide")
def projects():
    with st.container():
        # This part represents the Title
        st.title("Projects 📱")
        st.markdown("""------------------------------------------""")
        st.write("#")
    #For displaying project list
    with st.container():
        images,text=st.columns((1,4))
        

        


if(__name__=="__main__"):
    projects()