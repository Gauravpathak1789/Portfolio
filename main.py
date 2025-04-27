import streamlit as st

# Set page configuration
st.set_page_config(page_title='Gaurav Pathak - Portfolio', layout='wide')

# Profile Section
st.sidebar.image('mypic.jpg', caption='Gaurav Pathak', width=200)
st.sidebar.title("Gaurav Pathak")
st.sidebar.subheader("Data Science and ML Enthusiast")
st.sidebar.write("📍 Phagwāra, Kapurthala, Punjab, IND")
st.sidebar.write("📧 pathakgaurav21june@gmail.com")

# Social Media Links
st.sidebar.markdown("""
[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](http://www.linkedin.com/in/gauravpathak1789)
[![GitHub](https://img.icons8.com/ios-glyphs/48/000000/github.png)](https://github.com/Gauravpathak1789)
[![Kaggle](https://img.icons8.com/external-tal-revivo-filled-tal-revivo/48/000000/external-kaggle-an-online-community-of-data-scientists-and-machine-learners-owned-by-google-logo-filled-tal-revivo.png)](https://www.kaggle.com/gauravpathak1789)
""")

# About Me
st.title("About Me")
st.write(
    "Passionate about Machine Learning and Data Science, with experience in predictive modeling, data visualization, and API development using FastAPI and Flask. Skilled in transforming data into actionable insights to solve complex problems. Eager to contribute to innovative projects and collaborate with dynamic teams."
)

# Education
st.title("Education")
st.write("**Lovely Professional University** - B.Tech CSE (Data Science with ML) | 2022 - 2026")
st.write("**Millia Convent English School, Bihar** - Higher Secondary (Mathematics, Physics, Chemistry) | May 2020 - Mar 2022 | Grade: 83.43")

# Skills
st.title("Skills")
skill_icons = {
    "Python": "https://img.icons8.com/color/48/000000/python.png",
    "FastAPI": "https://img.icons8.com/?size=100&id=ZeaY7GVy1j1L&format=png&color=000000.png",
    "Machine Learning": "https://img.icons8.com/?size=100&id=z3YMXqHDYl9X&format=png&color=000000.png",
    "SQL": "https://img.icons8.com/color/48/000000/sql.png",
    "Statistics": "https://img.icons8.com/?size=100&id=21244&format=png&color=000000.png",
    "EDA": "https://img.icons8.com/external-flat-juicy-fish/48/000000/external-data-analytics-data-science-flat-flat-juicy-fish.png",
    "Data Visualization": "https://img.icons8.com/color/48/000000/combo-chart.png",
    "Data Analysis": "https://img.icons8.com/?size=100&id=4uuqSOuAOAxP&format=png&color=000000.png",
    "Database": "https://img.icons8.com/color/48/000000/database.png"
}

for skill, icon_url in skill_icons.items():
    st.markdown(f"<img src='{icon_url}' width='30' style='vertical-align:middle;'> {skill}", unsafe_allow_html=True)




# Certifications
st.title("Certifications")
certifications = [
    "✅ Complete Python With DSA Bootcamp + LEETCODE Exercises - Udemy",
    "✅ Data Science Masters - PW Skills",
    "✅ Data Structures and Algorithms using Python - CSE Pathshala"
]
for cert in certifications:
    st.write(cert)

# # Education
# st.title("Education")
# st.write("**Lovely Professional University** - B.Tech CSE (Data Science with ML) | 2022 - 2026")
# st.write("**Millia Convent English School, Bihar** - Higher Secondary (Mathematics, Physics, Chemistry) | May 2020 - Mar 2022 | Grade: 83.43")

# Projects
st.title("Projects")

# Project 1
st.subheader("🌾✨ Agriculture/Horticulture 🌱🍎 Commodities Price Prediction 📊💹")
st.image('agripred.png', caption='Agriculture Price Prediction',width=300)
st.write(
    "Implemented a hybrid machine learning model integrating Random Forest and Prophet to predict the prices of agricultural and horticultural commodities. Improved prediction accuracy and handled both seasonal and non-seasonal data with Flask APIs."
)
st.write("**Skills:** Python, Scikit-Learn, Flask, Machine Learning")
st.markdown("[GitHub Repo](https://github.com/Gauravpathak1789/https-githubAgricultur-Horticulture_commodities_price_prediction)")

# Project 2
st.subheader("🎬 Movie Recommendation System – Find Your Next Favorite Movie! 🍿🚀")
st.image('movie.png', caption='Movie Recommendation System',width=300)
st.write(
    "Built using Bag of Words and Similarity Score techniques! Helps users discover new movies based on their interests in just a few clicks."
)
st.write("**Skills:** Python, Scikit-Learn, Machine Learning, NLP, Streamlit")
st.markdown("[Live Demo](https://movie-recommendation-system-1729.streamlit.app/)")
st.markdown("[GitHub Repo](https://github.com/Gauravpathak1789/Movie-Recommendation-System)")

# Resume Section
st.title("Resume")
st.write("Download my latest resume below:")
st.download_button(label='📥 Download Resume', data=open('UPDATEDRESUME.pdf', 'rb').read(), file_name='Gaurav_Pathak_Resume.pdf', mime='application/pdf')


