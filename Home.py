import streamlit as st

# --- Set up the main page ---
st.set_page_config(page_title="House Recommendation & Prediction App", layout="centered")

# --- Home Page Header ---
st.title("🏡 House Recommendation & Prediction App")
st.markdown("""
Welcome to the House Recommendation & Prediction App!  
- Get personalized house recommendations.
- Predict the price of your dream home.
""")



st.header("Welcome!")
st.write("""
Use the sidebar to explore:
    - **Recommend Houses**: Get suggestions based on your preferences.
    - **Predict Price**: Estimate the price of a house based on its features.
    """)
st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb", use_column_width=True)
