import streamlit as st
import os
from PIL import Image
st.set_page_config(page_title="Mehraj.AI",page_icon=':brain:',layout="wide")
def projects():
    with st.container():
        # This part represents the Title
        st.title("Projects 📱")
        st.markdown("""------------------------------------------""")
        st.write("#")
    #For displaying project list
    image_subs=Image.open("Images/ViewAnalytics.png")
    with st.container():
        images1,text1=st.columns((3,5))
        with images1:
            st.image(image_subs)
        with text1:
            st.subheader(":red[Directing customers to subscription through app behavior analysis]")
            st.markdown("""
                     In this project, we use advanced data analytics and predictive modeling to boost customer engagement and increase subscription rates for a mobile app. We analyze user behavior to identify patterns and triggers that encourage premium subscriptions and in-app purchases.  
                     [GitHub>>](https://github.com/IMMRM/AppSubsAnalyser)  
                        [Video Explanation>>](https://www.linkedin.com/feed/update/urn:li:activity:7127639418512842752/)""")
        
        
        

        


if(__name__=="__main__"):
    projects()