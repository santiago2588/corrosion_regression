#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pycaret.classification import load_model, predict_model


# In[5]:


import streamlit as st


# In[6]:


import pandas as pd
import numpy as np


# In[7]:


def predict_corrosion(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    return predictions_data['Label'][0]
    
model = load_model('ada_model_regressor')


# In[8]:


st.title('Corrosion Prediction Web App')
st.write('This is a web app to predict corrosion rates of oil wells based on         several features that you can see in the sidebar. Please adjust the         value of each feature. After that, click on the Predict button at the bottom to         see the prediction of the model.')


# In[10]:


BPPD = st.sidebar.slider(label = 'BPPD', min_value = 0,
                          max_value = 10000 ,
                          value = 1000,
                          step = 10)


# In[11]:


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

Diametro_tuberia = st.sidebar.slider(label = 'Diametro_tuberia_mm', min_value = 0.0,
                          max_value = 100.0,
                          value = 88.9,
                          step = 1.0)


# In[13]:


features = {'Barriles de petroleo por dia': BPPD, 'Barriles de agua por dia': BAPD,
            'Barriles de fluido por dia': BFPD, 'BSW %': BSW,
            'Caudal de gas, MSCFD': Caudal_gas, 'Presion en cabeza, psi': Presion_cabeza,
            'Temperatura en cabeza, F': Temperatura_cabeza, 'Salinidad, ppm': Salinidad,
            'Fraccion de CO2 en gas': CO2_frac, 'Presion parcial CO2, psi': Pp_CO2, 
            'Velocidad del liquido, m/s': Velocidad_liquido, 'Bicarbonatos, ppm': Bicarbonatos,
            'Dosis de Anticorrosivo, ppm': Dosis_IC, 'Contenido de hierro, ppm': Fe,
            'Diametro de tuberia, mm': Diametro_tuberia,
            }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_corrosion(model, features_df)
    
    st.write(' Based on feature values, the corrosion rate is '+ str(prediction))


# In[ ]:




