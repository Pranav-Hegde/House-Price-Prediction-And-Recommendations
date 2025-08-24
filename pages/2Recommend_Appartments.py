import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.set_page_config(page_title="Recommend Appartments")

location_df = pickle.load(open(r'D:\Prediction\DataSets\location_distance.pkl', 'rb'))
loc_df = pickle.load(open(r'D:\Prediction\DataSets\df.pkl', 'rb'))

cosine_sim1= pickle.load(open(r'D:\Prediction\DataSets\cosine_sim1.pkl', 'rb'))
cosine_sim2= pickle.load(open(r'D:\Prediction\DataSets\cosine_sim2.pkl', 'rb'))
cosine_sim3= pickle.load(open(r'D:\Prediction\DataSets\cosine_sim3.pkl', 'rb'))

cosine_sim4 = cosine_sim1 * 0.5 + cosine_sim2 * 0.8 + cosine_sim3 * 1


def recommend4(property_name, cosine_sim=cosine_sim4):
    idx = loc_df.index[loc_df['society'] == property_name].tolist()[0]

    sim_scores = list(enumerate(cosine_sim3[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    property_indices = [i[0] for i in sim_scores]

    recommendations_df = pd.DataFrame({
        'society': loc_df['society'].iloc[property_indices],
        'SimilarityScore': sim_scores
    })

    return recommendations_df

st.title('Select Location and radius')

locations = sorted(location_df.columns.to_list())
selected_location = st.selectbox('Location', locations)

radius = st.number_input('Radius in kms')

if st.button('Search'):
    # Filter for distances less than radius*1000 (assuming distances are in meters)
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    # Show only the first 10 results
    appartment=[]
    for key, value in result_ser.head(10).items():
        st.text(str(key)+" in  "+str(value)+' kms ')

st.title('Recommend Appartments')
selected_appartments = st.selectbox('Select an appartment',sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend4(selected_appartments)

    st.dataframe(recommendation_df)