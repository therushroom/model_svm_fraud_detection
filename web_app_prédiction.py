# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/PC IMANE/Desktop/trained_model.sav', 'rb'))

# creating a function for Prediction
def fraud_prediction(input_data):
        
  # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

  # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'transaction non fraduleuse'
    else:
      return 'transaction fraduleuse'

def main():
    
    
    # giving a title
    st.title(' Prediction des transaction fraduleuse Web App')
    
    
    # getting the input data from the user
    
    
    Time = st.text_input('Time')
    V1= st.text_input('V1')
    V2= st.text_input('V2')
    V3= st.text_input('V3')
    V4= st.text_input('V4')
    V5= st.text_input('V5')
    V6= st.text_input('V6')
    V7 = st.text_input('V7')
    V8= st.text_input('V8')
    V9= st.text_input('V9')
    V10= st.text_input('V10')
    V11= st.text_input('V11')
    V12= st.text_input('V12')
    V13= st.text_input('V13')
    V14 = st.text_input('V14')
    V15= st.text_input('V15')
    V16= st.text_input('V16')
    V17= st.text_input('V17')
    V18= st.text_input('V18')
    V19= st.text_input('V19')
    V20= st.text_input('V20')
    V21= st.text_input('V21')
    V22= st.text_input('V22')
    V23= st.text_input('V23')
    V24= st.text_input('V24')
    V25= st.text_input('V25')
    V26= st.text_input('V26')
    V27= st.text_input('V27')
    V28 = st.text_input('V28')
    Amount= st.text_input('Amount')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('résultat du test'):
        diagnosis = fraud_prediction([Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount])
        
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()