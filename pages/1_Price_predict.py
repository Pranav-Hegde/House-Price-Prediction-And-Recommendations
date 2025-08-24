import streamlit as st
import pickle
import pandas as pd
import numpy as np



st.set_page_config(page_title="Viz Demo")

with open('X.pkl','rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = pickle.load(file)

st.header("Enter your Inputs")

Property_type = st.selectbox('Property Type',['flat','house'])

Sector=st.selectbox('Sector name',sorted(df['sector'].unique().tolist()))

BedRoom=float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

BathRoom=float(st.selectbox('Number of Bathroom',sorted(df['bathroom'].unique().tolist())))

Balcony=float(st.selectbox('Number of Balconies',sorted(df['balcony'].unique().tolist())))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

Area = st.number_input("area_sqft")

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishDetails'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category',sorted(df['Luxury_category'].unique().tolist()))

floor_category = float(st.selectbox('Floor Category',sorted(df['floorNum'].unique().tolist())))

if st.button('Predict'):

    # Use your actual variable values here
    data = [[
        Property_type,  # society
        Area,  # area
        BedRoom,  # bedRoom
        BathRoom,  # bathroom
        Balcony,  # balcony
        floor_category,  # floorNum
        property_age,  # agePossession
        furnishing_type,  # furnishDetails
        luxury_category,  # Luxury_category
        Sector
    ]]

    columns = [
        'Property_type','area', 'bedRoom', 'bathroom', 'balcony',
        'floorNum', 'agePossession', 'furnishDetails',
        'Luxury_category', 'sector'
    ]

    one_df = pd.DataFrame(data, columns=columns)

    st.dataframe(one_df)

    base_price = np.expm1(pipeline.predict(one_df))[0]

    low = base_price - 0.22
    high = base_price + 0.22

    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))


