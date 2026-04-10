# Jai Hanuman 🙏🙏🙏🙏🙏

import streamlit as st

st.set_page_config(page_title='IntelliEstate',layout='wide')


#  --------------Main Title -----------------
st.markdown("""
<h1 style='text-align: center; color: Black; font-size: 60px;'>
🏠 IntelliEstate
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align: center; color: black;'>
Smart Real Estate Analytics, Prediction & Recommendation System
</h3>
""", unsafe_allow_html=True)

st.markdown("---")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown("""
    <a href="/Perform_Analytics" target="_self" style="text-decoration:none;">
        <div style="background-color:black; width: 100%; height: 200px; border-radius:15px; text-align:center;">
            <h3 style="color:white;padding-top:34px">📊 Analytics</h3>
            <p style="color:white;padding-top:37px">Explore price trends and market insights</p>
        </div>
    </a>
    """, unsafe_allow_html=True)        

with col2:
    st.markdown("""
    <a href="/Price_Prediction" target="_self" style="text-decoration:none;">
        <div style="background-color:#111; width: 100%; height: 200px; border-radius:15px; text-align:center; cursor:pointer;">
            <h3 style="color:white;padding-top:34px">💰Prediction</h3>
            <p style="color:white;padding-top:37px">Predict property prices using ML</p>
        </div>
    </a>
    """, unsafe_allow_html=True)

    
with col3:
    st.markdown("""
    <a href="/Insights" target="_self" style="text-decoration:none;">
        <div style="background-color:#111; width: 100%; height: 200px; border-radius:15px; text-align:center;">
            <h3 style="color:white;padding-top:34px">💡 Insights</h3>
            <p style="color:white; padding-top:37px">Understand key price factors</p>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
with col4:
    st.markdown("""
    <a href="/Recommendation_System" target="_self" style="text-decoration:none;">
        <div style="background-color:#111; width: 115%; height: 200px;  border-radius:15px; text-align:center;">
            <h3 style="color:white;">🏠Recommendation</h3>
            <p style="color:white;">Find similar properties easily</p>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
# st.markdown("---")
# # ---------- CALL TO ACTION ----------
# st.markdown("""
# <h3 style='text-align: center; color: black;'>
# Use the sidebar to explore different modules
# </h3>
# """, unsafe_allow_html=True)