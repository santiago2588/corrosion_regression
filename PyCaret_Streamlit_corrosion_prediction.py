#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pycaret.classification import load_model, predict_model


# In[2]:


import streamlit as st


# In[3]:


import pandas as pd
import numpy as np


# In[5]:


def predict_corrosion(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    
model = load_model('corrosion_regressor')


# In[6]:


st.title('Corrosion Prediction Web App')
st.write('This is a web app to predict corrosion rates of oil wells based on         several features that you can see in the sidebar. Please adjust the         value of each feature. After that, click on the Predict button at the bottom to         see the prediction of the model.')


# In[7]:


BPPD = st.sidebar.slider(label = 'BPPD', min_value = 0,
                          max_value = 10000 ,
                          value = 1000,
                          step = 10)


# In[9]:


BAPD = st.sidebar.slider(label = 'BAPD', min_value = 0,
                          max_value = 10000 ,
                          value = 1000,
                          step = 10)
                          
BFPD = st.sidebar.slider(label = 'BFPD', min_value = 0,
                          max_value = 10000 ,
                          value = 1000,
                          step = 10)                          

BSW = st.sidebar.slider(label = 'BSW', min_value = 0.0,
                          max_value = 100.0 ,
                          value = 50.0,
                          step = 1.0)

Caudal_gas = st.sidebar.slider(label = 'Caudal_gas_MSCFD', min_value = 0,
                          max_value = 1000 ,
                          value = 100,
                          step = 1)
   
Presion_cabeza = st.sidebar.slider(label = 'Presion_cabeza_psi', min_value = 0,
                          max_value = 500,
                          value = 150,
                          step = 1)

Temperatura_cabeza = st.sidebar.slider(label = 'Temperatura_cabeza_F', min_value = 0,
                          max_value = 500 ,
                          value = 150,
                          step = 1)

Salinidad = st.sidebar.slider(label = 'Salinidad_ppm', min_value = 0,
                          max_value = 100000 ,
                          value = 50000,
                          step = 100)

CO2_frac = st.sidebar.slider(label = 'CO2_frac', min_value = 0.00,
                          max_value = 1.00 ,
                          value = 0.50,
                          step = 0.01)
                          
Pp_CO2 = st.sidebar.slider(label = 'Pp_CO2_psi', min_value = 0.0,
                          max_value = 500.0,
                          value = 100.0,
                          step = 1.0)

Velocidad_liquido = st.sidebar.slider(label = 'velocidad_liquido_m/s', min_value = 0.0,
                          max_value = 10.0,
                          value = 2.0,
                          step = 0.1)

Bicarbonatos = st.sidebar.slider(label = 'bicarbonatos_ppm', min_value = 0,
                          max_value = 5000,
                          value = 100,
                          step = 1)

Dosis_IC = st.sidebar.slider(label = 'dosis_IC_ppm', min_value = 0,
                          max_value = 500,
                          value = 100,
                          step = 1)

Fe = st.sidebar.slider(label = 'Fe_ppm', min_value = 0,
                          max_value = 500,
                          value = 100,
                          step = 1)

Diametro_tuberia = st.select_slider('Seleccione el diametro de la tuberia, mm', options = [73, 88.9])


# In[15]:


features = {'BPPD': BPPD, 'BAPD': BAPD,
            'BFPD': BFPD, 'BSW': BSW,
            'Caudal_gas_MSCFD': Caudal_gas, 'Presion_cabeza_psi': Presion_cabeza,
            'Temperatura_cabeza_F': Temperatura_cabeza, 'Salinidad_ppm': Salinidad,
            'CO2_frac': CO2_frac, 'Pp_CO2_psi': Pp_CO2, 
            'velocidad_liquido_m/s': Velocidad_liquido, 'bicarbonatos_ppm': Bicarbonatos,
            'dosis_IC_ppm': Dosis_IC, 'Fe_ppm': Fe,
            'Diametro_tuberia_mm': Diametro_tuberia,
            }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    prediction = predict_corrosion(model, features_df)
    st.write(prediction)

