import pandas as pd
import numpy as np
import streamlit as st
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib


def main():
    model = joblib.load('model_joblib')
    st.title('House Price Prediction for Silicon Valley of India - Bangalore')
    st.markdown(
        'Just Enter the following details and we will predict the price of your **Dream House**')

        
    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![Chethan-Reddy]'
                        '(https://img.shields.io/badge/Author-Chethan%20Reddy-brightgreen)]'
                        '(https://www.linkedin.com/in/chethan-reddy-0201791ba/)') 


    
    st.warning('Only Enter Numeric Values in the Following Fields')
    bhk = st.text_input("Total BHK")
    area = st.text_input("Area in Square Feet")
    baths = st.text_input("Total Bathrooms")
    balcony = st.selectbox("Total Balcony", ['0', '1', '2', '3'])
    areatype = st.selectbox("Type Of Area" , ["1","2","3","4"])
    submit = st.button('Predict Price')
    if submit:
        if bhk and area and baths and balcony:
            with st.spinner('Predicting...'):
                time.sleep(2)
                bhk, area, baths, balcony , areatype = int(bhk), int(
                    area), int(baths), int(balcony), int(areatype)
                x_test = np.array([[areatype, bhk, area, baths, balcony]])
                prediction = model.predict(x_test)
                st.info(f"Your **Dream House** Price is {prediction[0][0]} lacs :)")
        else:
            st.error('Please Enter All the Details')

if __name__ == '__main__':
    main()
