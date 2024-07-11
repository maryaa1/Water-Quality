import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# Memuat model yang disimpan
filename = 'model_water_quality_prediction.h5'  # Sesuaikan nama file sesuai kebutuhan
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
# Tambahkan input lainnya sesuai kebutuhan

# Tombol prediksi dan hasil
if st.button('Test Prediksi Air'):
    # Mengumpulkan nilai input
    input_values = [ph, Hardness]  # Tambahkan semua input yang diperlukan
    input_values = [float(x.replace(',', '')) if x else 0.0 for x in input_values]
    input_data = np.array([input_values])

    # Debugging output
    print("Input data:", input_data)  # Menampilkan data input
    prediction = model_water_quality_prediction.predict(input_data)
    print("Raw prediction output:", prediction)  # Menampilkan output prediksi mentah

    # Menginterpretasikan prediksi
    if prediction[0] > 0.5:  # Mengasumsikan model output adalah probabilitas
        result_text = 'Air dapat Diminum'
        color = 'green'
        print("Predicted label: Air dapat Diminum")  # Debugging label prediksi
        st.success("Air dapat Diminum")
    else:
        result_text = 'Air Tidak dapat Diminum'
        color = 'red'
        print("Predicted label: Air Tidak dapat Diminum")  # Debugging label prediksi
        st.success("Air Tidak dapat Diminum")
