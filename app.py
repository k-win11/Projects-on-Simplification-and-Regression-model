import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Create web app using streamlit
st.title('Concrete Age Prediction in days')

# User input
cement = st.text_input('Enter Cement value')
water = st.text_input('Enter Water value')
strength = st.text_input('Enter Strength value')
Blast_Furnace_Slag = st.text_input('Enter Blast_Furnace_Slag value')
Fly_Ash = st.text_input('Enter Fly_Ash value')
Superplasticizer  = st.text_input('Enter Superplasticizer value')
Coarse_Aggregate = st.text_input('Enter Coarse_Aggregate value')
Fine_Aggregate = st.text_input('Enter Fine_Aggregate value')


# Feature creation for model
feature = np.array([[cement, water,strength,Fine_Aggregate,Coarse_Aggregate ,Superplasticizer ,Fly_Ash,Blast_Furnace_Slag]])
if st.button('Get Age'):
    prediction = model.predict(feature).reshape(1, -1)
    st.write('Concrete age in days:', prediction[0])

