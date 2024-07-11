import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model


# Memuat model yang disimpan
filename = 'model_water_quality_prediction.h5'
model_water_quality_prediction = load_model(filename)

# Judul web
st.title('Prediksi Kualitas Air')

# Membagi kolom untuk input
col1, col2 = st.columns(2)

with col1:
    ph = st.text_input('Masukan nilai pH')
with col2:
    Hardness = st.text_input('Masukan nilai Hardness')
with col1:
    Solids = st.text_input('Masukan nilai Solids')
with col2:
    Chloramines = st.text_input('Masukan nilai Chloramines')
with col1:
    Sulfate = st.text_input('Masukan nilai Sulfate')
with col2:
    Conductivity = st.text_input('Masukan nilai Conductivity')
with col1:
    Organic_carbon = st.text_input('Masukan nilai Organic carbon')
with col2:
    Trihalomethanes = st.text_input('Masukan nilai Trihalomethanes')
with col1:
    Turbidity = st.text_input('Masukan nilai Turbidity')

# Mengubah format desimal jika menggunakan koma
input_values = [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]
input_values = [float(x.replace(',', '')) if x else 0.0 for x in input_values]

# Buat numpy array dari nilai-nilai tersebut
input_data = np.array([input_values])

# Prediksi
water_prediction = ''

# Tombol prediksi
if st.button('Test Prediksi Air'):
    water_prediction = model_water_quality_prediction.predict(input_data)
    if water_prediction[0] == 1:
        water_prediction = 'Air dapat Diminum'
    else:
        water_prediction = 'Air Tidak dapat Diminum'
        
    st.success(water_prediction)

        
   


