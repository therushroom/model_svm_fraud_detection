# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:15:01 2021

@author: BOUSSAIRI
"""

import streamlit as st
import numpy as np 
import pandas as pd
import pickle


loaded_model = pickle.load(open("C:/Users/Xps/Desktop/S4/interpretation/best_model.sav",'rb'))



# creating a function for Prediction

def Fraud_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The Credit Card is classified as non-fraudulent'
    else:
      return 'The Credit Card is classified as fraudulent'
  
    
  
def main():
    
    
    # giving a title
    st.title('Credit Card Fraud detection')
    
    
    # getting the input data from the user
    
    
    V1 = st.text_input('V1')
    V3 = st.text_input('V3')
    V4 = st.text_input('V4')
    V8 = st.text_input('V8')
    V17 = st.text_input('V17')
    V21 = st.text_input('V21')
    Amount = st.text_input('Amount')
    
    
    # code for Prediction
    Detect = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        Detect = Fraud_prediction([V3, V1, V8, Amount, V17, V21, V4])
        
        
    st.success(Detect)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  