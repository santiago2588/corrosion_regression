#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pycaret.regression import load_model, predict_model


# In[2]:


import streamlit as st


# In[3]:


import pandas as pd
import numpy as np


# In[4]:


def predict_corrosion(model, df):
    predictions_data = predict_model(estimator = model, data = df)
    predictions=predictions_data['Label'][0]
    return predictions

model = load_model('corrosion_regressor')


# In[5]:


st.title('Corrosion Prediction Web App')
st.write('This is a web app to predict corrosion rates of oil wells based on         several features that you can see in the sidebar. Please adjust the         value of each feature. After that, click on the Predict button at the bottom to         see the prediction of the model.')


# In[6]:


BPPD = st.sidebar.number_input(label = 'BPPD', min_value = 0,
                          max_value = 2000 ,
                          value = 500)


# In[7]:


BAPD = st.sidebar.number_input(label = 'BAPD', min_value = 0,
                          max_value = 5000 ,
                          value = 1000)
                          
BFPD = st.sidebar.number_input(label = 'BFPD', min_value = 0,
                          max_value = 6000 ,
                          value = 1000)                          

BSW = st.sidebar.number_input(label = 'BSW', min_value = 0.0,
                          max_value = 100.0 ,
                          value = 50.0)

Caudal_gas = st.sidebar.number_input(label = 'Caudal_gas_MSCFD', min_value = 0,
                          max_value = 1000 ,
                          value = 100)
   
Presion_cabeza = st.sidebar.number_input(label = 'Presion_cabeza_psi', min_value = 0,
                          max_value = 500,
                          value = 150)

Temperatura_cabeza = st.sidebar.number_input(label = 'Temperatura_cabeza_F', min_value = 0,
                          max_value = 300 ,
                          value = 150)

Salinidad = st.sidebar.number_input(label = 'Salinidad_ppm', min_value = 0,
                          max_value = 100000 ,
                          value = 50000)

CO2_frac = st.sidebar.slider(label = 'CO2_frac', min_value = 0.00,
                          max_value = 1.00 ,
                          value = 0.50)
                          
Pp_CO2 = st.sidebar.number_input(label = 'Pp_CO2_psi', min_value = 0.0,
                          max_value = 500.0,
                          value = 100.0)

Velocidad_liquido = st.sidebar.number_input(label = 'velocidad_liquido_m/s', min_value = 0.0,
                          max_value = 10.0,
                          value = 2.0)

Bicarbonatos = st.sidebar.number_input(label = 'bicarbonatos_ppm', min_value = 0,
                          max_value = 3000,
                          value = 500)

Dosis_IC = st.sidebar.number_input(label = 'dosis_IC_ppm', min_value = 0,
                          max_value = 300,
                          value = 100)

Fe = st.sidebar.number_input(label = 'Fe_ppm', min_value = 0,
                          max_value = 200,
                          value = 50)


# In[8]:


features = {'BPPD': BPPD, 'BAPD': BAPD,
            'BFPD': BFPD, 'BSW': BSW,
            'Caudal_gas_MSCFD': Caudal_gas, 'Presion_cabeza_psi': Presion_cabeza,
            'Temperatura_cabeza_F': Temperatura_cabeza, 'Salinidad_ppm': Salinidad,
            'CO2_frac': CO2_frac, 'Pp_CO2_psi': Pp_CO2, 
            'velocidad_liquido_m/s': Velocidad_liquido, 'bicarbonatos_ppm': Bicarbonatos,
            'dosis_IC_ppm': Dosis_IC, 'Fe_ppm': Fe
           }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    prediction = predict_corrosion(model, features_df)
    prediction='Based on your input variables, the corrosion rate is '+str('%f' % prediction) + ' mpy'
    st.write(prediction)

