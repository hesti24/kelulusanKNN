import pickle
import streamlit as st
#membaca model

mahasiswa_model = pickle.load(open('mahasiswa_modelKNN.sav', 'rb'))

#Nama Web
st.title('Prediksi Kelulusan Mahasiswa STT Wastukancana')


col1, col2 = st.columns(2)

with col1 :
    IPS1 = st.number_input ('masukan IPS1')
    IPS2 = st.number_input('masukan IPS2')
    IPS3 = st.number_input('masukan IPS3')
    IPS4 = st.number_input('masukan IPS4')
with col2 :    
    IPS5 = st.number_input('masukan IPS5')
    IPS6 = st.number_input('masukan IPS6')
    IPS7 = st.number_input('masukan IPS7')
    IPS8 = st.number_input('masukan IPS8')

# Code untuk Prediksi
ket_Kelulusan = ''

# membuat Tombol Untuk Prediksi
if st.button('Test Prediksi Kelulusan') :
    ket_prediction = mahasiswa_model.predict([[ IPS1, IPS2, IPS3, IPS4, IPS5, IPS6 , IPS7 , IPS8]])

    if(ket_prediction==1):
        ket_Kelulusan = 'Mahasiswa Lulus'
    else : 
        ket_Kelulusan = 'Mahasiswa tidak lulus'

    st.success(ket_Kelulusan)
