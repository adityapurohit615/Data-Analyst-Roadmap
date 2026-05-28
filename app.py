import streamlit as st

st.set_page_config(page_title="Data Analyst Roadmap", layout="wide")

st.title("Data Analyst Roadmap")
st.markdown("This roadmap provides a comprehensive guide to becoming a Data Analyst.")

# Sidebar navigation
st.sidebar.title("Navigation")
sections = [
    "Introduction",
    "1. Programming Language",
    "2. Statistics",
    "3. Databases",
    "4. ETL Tools",
    "5. Business Intelligence Tools",
    "6. Advanced Excel",
    "7. Real Time Internships"
]
selection = st.sidebar.radio("Go to", sections)

if selection == "Introduction":
    st.header("Work Of Data Analyst")
    st.image("https://user-images.githubusercontent.com/20041231/211466839-e0145119-20fd-4efe-bbd7-d2c3b10fdfba.JPG")
    st.image("https://user-images.githubusercontent.com/20041231/211468652-d4316856-0ee5-44ea-9dd9-538beef38180.JPG")

elif selection == "1. Programming Language":
    st.header("1. Programming Language")
    st.subheader("Python")
    st.image("https://user-images.githubusercontent.com/20041231/211466229-df1c12da-ed6e-4bb9-97f7-84871a287580.png")
    st.markdown("- [Python In English](https://www.youtube.com/watch?v=bPrmA1SEN2k&list=PLZoTAELRMXVNUL99R4bDlVYsncUNvwUBB)")
    st.markdown("- [Python In Hindi](https://www.youtube.com/watch?v=MJd9d9Mpxg0&list=PLTDARY42LDV4qqiJd1Z1tShm3mp9-rP4v)")

    st.subheader("R Programming Language")
    st.image("https://user-images.githubusercontent.com/20041231/211466981-43ebae2c-0581-4604-8b01-35a97d350080.png")

elif selection == "2. Statistics":
    st.header("2. Statistics")
    st.image("https://user-images.githubusercontent.com/20041231/211467108-a82c82fa-4366-440b-8294-5bd3e0bbf081.png")
    st.markdown("- [English: 7 Days Statistics Live Session](https://www.youtube.com/watch?v=11unm2hmvOQ&list=PLZoTAELRMXVMgtxAboeAx-D9qbnY94Yay)")
    st.markdown("- [Statistics in ML(43 videos)](https://www.youtube.com/watch?v=zRUliXuwJCQ&list=PLZoTAELRMXVMhVyr3Ri9IQ-t5QPBtxzJO)")
    st.markdown("- [Hindi: Stats Playlist](https://www.youtube.com/watch?v=7y3XckjaVOw&list=PLTDARY42LDV6YHSRo669_uDDGmUEmQnDJ)")

    st.subheader("EDA")
    st.markdown("- [EDA Live](https://www.youtube.com/playlist?list=PLZoTAELRMXVPzj1D0i_6ajJ6gyD22b3jh)")
    st.markdown("- [EDA Detailed Playlist](https://www.youtube.com/watch?v=ioN1jcWxbv8&list=PLZoTAELRMXVPQyArDHyQVjQxjj_YmEuO9)")

    st.subheader("Feature Engineering")
    st.markdown("- [Complete Detailed Feature Engineering](https://www.youtube.com/watch?v=6WDFfaYtN6s&list=PLZoTAELRMXVPwYGE2PXD3x0bfKnR0cJjN)")
    st.markdown("- [Live EDA Feature Engineering Playlist](https://www.youtube.com/watch?v=bTN-6VPe8c0&list=PLZoTAELRMXVPzj1D0i_6ajJ6gyD22b3jh)")

    st.subheader("Final Goal Outcome:")
    st.markdown("1. Techniques to Perform Statistical Analysis")
    st.markdown("2. Familiar with all concepts which will be important for Machine Learning")

elif selection == "3. Databases":
    st.header("3. Databases")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://user-images.githubusercontent.com/20041231/211467463-3fe5e606-e11b-49cf-9071-3abdd25584c8.png")
        st.markdown("[Mysql](https://www.youtube.com/watch?v=us1XyayQ6fU&list=PLZoTAELRMXVNMRWlVf0bDDSxNEn38u9Cl)")
    with col2:
        st.image("https://user-images.githubusercontent.com/20041231/211467512-c1e429b7-1bb9-47c0-b39c-99932b9043a5.png")
        st.markdown("[Mongodb](https://www.youtube.com/watch?v=magzEfYqIos&list=PLZoTAELRMXVN_8zzsevm1bm6G-plsiO1I)")

elif selection == "4. ETL Tools":
    st.header("4. ETL Tools")
    st.image("https://user-images.githubusercontent.com/20041231/211472581-3b05b5d7-2d76-4002-835a-172cada11672.png")
    st.markdown("- [Amazing Article on ETL](https://www.informatica.com/resources/articles/what-is-etl.html)")
    st.image("https://user-images.githubusercontent.com/20041231/211473712-f8737fd4-0622-49de-b751-706322813b31.JPG")
    st.markdown("- [FSDA 2.0](https://ineuron.ai/course/Full-Stack-Data-Analytics-2.0)")
    st.markdown("- [Top ETL Tools](https://www.integrate.io/blog/top-7-etl-tools/)")

elif selection == "5. Business Intelligence Tools":
    st.header("5. Business Intelligence Tools")
    st.image("https://user-images.githubusercontent.com/20041231/211717386-39f75daf-0c1e-4295-8e00-657578f397a1.jpg")
    st.image("https://user-images.githubusercontent.com/20041231/211717508-ccd3da44-1e33-47c0-a1ec-66583f73c496.jpg")

elif selection == "6. Advanced Excel":
    st.header("6. Advanced Excel")
    st.image("https://user-images.githubusercontent.com/20041231/211717601-a7520e3b-bd50-4cbd-957a-8ff2bbce25b3.png")

elif selection == "7. Real Time Internships":
    st.header("7. Real Time Internships")
    st.image("https://user-images.githubusercontent.com/20041231/211743026-4f3da97c-897b-4d10-acea-503591ca935d.jpg")
    st.markdown("[ineuron Internship Portal](https://internship.ineuron.ai/)")

    st.subheader("Best Affordable Data Science Course From Pwskills (6-7 Months)")
    st.markdown("**Impact Batch:- Data-Science-Masters (Full Stack Data Science)**")
    st.markdown("1. [Data Science Masters Hindi](https://bit.ly/3CKX1od)")
    st.markdown("2. [Data Science Masters English](https://bit.ly/3iEjWuH)")


# Interactive checklist
st.sidebar.markdown("---")
st.sidebar.subheader("Your Progress")

total_tasks = 7
completed_tasks = 0

if st.sidebar.checkbox("Programming Language"):
    completed_tasks += 1
if st.sidebar.checkbox("Statistics"):
    completed_tasks += 1
if st.sidebar.checkbox("Databases"):
    completed_tasks += 1
if st.sidebar.checkbox("ETL Tools"):
    completed_tasks += 1
if st.sidebar.checkbox("Business Intelligence Tools"):
    completed_tasks += 1
if st.sidebar.checkbox("Advanced Excel"):
    completed_tasks += 1
if st.sidebar.checkbox("Real Time Internships"):
    completed_tasks += 1

progress = completed_tasks / total_tasks
st.sidebar.progress(progress)
st.sidebar.text(f"{completed_tasks}/{total_tasks} Completed")
