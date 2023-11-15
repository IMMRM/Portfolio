import streamlit as st
import os
st.set_page_config(page_title="Mehraj.AI",page_icon=':brain:',layout="wide")
def main():
    with st.container():
        # This part represents the Title
        #st.title("Mehrajur Rahman Mirdha 👨‍💻")

        #Designation
        st.markdown("# Mehrajur Rahman Mirdha",unsafe_allow_html=True)
        st.subheader("Data Scientist 🤖 | Data Analyst 📊 ")
        st.markdown("""------------------------------------------""")
        st.write("#")
        st.markdown(
        """
        <p>
            <a href="https://github.com/immrm" target="_blank" style="text-decoration:none;">
                <img src="https://cdn-icons-png.flaticon.com/128/919/919847.png" alt="GitHub" style="width:40px;height:40px;margin-right:15px;">
            </a>
            <a href="mailto:mehraj.mirdha@.com" target="_blank" style="text-decoration:none;">
                <img src="https://cdn-icons-png.flaticon.com/128/2875/2875394.png" alt="Email" style="width:40px;height:40px;margin-right:15px;">
            </a>
            <a href="https://www.linkedin.com/in/mrmirdha" target="_blank" style="text-decoration:none;">
                <img src="https://cdn-icons-png.flaticon.com/128/1383/1383262.png" alt="LinkedIn" style="width:40px;height:40px;">
            </a>
        </p>
        """
        , unsafe_allow_html=True)
    # About Me section
    with st.container():
        st.write("##")
        st.subheader("About Me")
        st.info(
                """
                - I'm a data wizard with :red[4 plus years] of experience in the land of numbers and statistics.🧙‍♂️ My secret power is using data to solve real-world problems and make sense of all that chaos out there.

    - I'm a big fan of all things data, from crunching numbers to building fancy dashboards that show off my skills.📊 I'm pretty good at programming languages like Python , and I'm a pro at manipulating data using SQL and other tools.

    - But my greatest joy comes from turning raw data into actionable insights that help businesses grow and thrive.🚀 Whether it's building predictive models or creating data visualizations, I'm always looking for ways to help businesses make smarter decisions.

    - When I'm not playing with data, you can find me collaborating with other teams, like product managers and software engineers.👩‍💻 I believe that teamwork makes the dream work, and I love being part of a team that's working towards a common goal.

    - So if you're looking for a data professional who knows how to have fun while getting stuff done, then look no further! I'm your guy, and I'm ready to help you take your data game to the next level.🌟"""

            )

    #Work Experience
    with st.container():
        st.write("#")
        st.subheader("Work Experience")
        #For TCS:
        st.markdown('''
        #### Tata Consultancy Services Pvt. Ltd. (TCS)
        ##### :red[Analytics and Reporting Lead] &nbsp; &nbsp; &nbsp; *May'22 - Oct'23*
        - Lead a team of `4+ data analysts`.
        - Understand the requirements of the respective stakeholders and plan the sprint.
        - Developed queries in SQL Server and T-SQL to create and use complex stored procedures and
        to facilitate efficient and meaningful data transformation.
        - Presented key deliverables and valuable insights to stakeholders in monthly business review
        meetings.
        - Fetched required form of data from Azure Data Explorer by writing KQL script and embedding it
        PowerBI to design visuals for proper data analysis.
        - Automated the team utilisation reporting process by replacing the manual MS Excel filling
        process by directly fetching the data from Azure Analytics Views and building up visualisation
        in PowerBI which saved `7 hours per month of manual efforts` and `100%` accurate data.
        - Created complex DAX queries for generating calculated columns and measures
        ##### :red[Data Analyst] &nbsp; &nbsp; &nbsp; *July'19 - Apr'22*
        - Developed multiple business value KPIs by using PowerBI functionalities and wrote complex
        SQL queries to fetch required data distributed across multiple source tables. These KPIs help
        stakeholders to identify various issues at different stages of the project lifecycle and tracking
        major reasons for SLA breach.

        ''',unsafe_allow_html=True)

    #Education
    with st.container():
        st.write("#")
        st.subheader("Education")
        #For Amity:
        st.markdown('''
        ####  Amity University
        ##### :red[Bachelor of Technology(B.Tech)] &nbsp; &nbsp; &nbsp; *Aug'15 - May'19*
        - **Major**: `Computer Science and Engineering (CSE)`.
        - **Grade**: `9.22` C.G.P.A
        - **Achievements**: Awarded with `Bronze Medal` for securing `Third` Position in University.
        ''',unsafe_allow_html=True)


    state = st.session_state.get("state", False)
    if st.button("Contact Me"):
        state = not state
        st.session_state["state"] = state
    if(state):
       st.markdown("""
        Mail me @: mehraj.mirdha@gmail.com
                   <br>
        LinkedIn : <a href='https://www.linkedin.com/in/mrmirdha'> Profile </a>
                   

        """,unsafe_allow_html=True)
    
       
    


if __name__ == "__main__":
    main()
