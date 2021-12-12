# import modul-modul yang dibutuhkan
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# me-non aktifkan peringatan pada python
import warnings 
warnings.filterwarnings('ignore')

# judul project
st.title('Analisa Survey Perkembangan Data Scientist di Indonesia')

# persiapan data frame global
st.header('Sample Data Survey Global')
df_global = pd.read_csv('https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/survey_2021_responses.csv')
df_sample_global = df_global.head()
st.write(df_sample_global)

# persiapan data frame Indonesia
st.header('Sample Data Survey Indonesia')
df_indonesia=df_global[df_global["Q3"]=="Indonesia"]
st.write('Dataset sudah difilter hanya Indonesia:')
df_sample_indo = df_indonesia.head()
st.write(df_sample_indo)

# kategori berdasarkan umur
st.header('Kategori Umur Responden Indonesia')
st.bar_chart(df_indonesia['Q1'].value_counts().sort_index())
st.header('Kategori Umur Responden Global')
st.bar_chart(df_global['Q1'].value_counts().sort_index())

# kategori berdasarkan jenis kelamin
st.header('Kategori Jenis Kelamin Responden Indonesia')
def countPlot():
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(y="Q2", data=df_indonesia)
    st.pyplot(fig)
countPlot()

st.header('Kategori Jenis Kelamin Responden Global')
def countPlot():
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(y="Q2", data=df_global[1:])
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden Indonesia berdasarkan tingkat pendidikan
st.header('Perbandingan jumlah responden Indonesia berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q4", data=df_indonesia)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan jumlah responden Global berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q4", data=df_global[1:])
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden Indonesia berdasarkan status pekerjaan
st.header('Perbandingan jumlah responden Indonesia berdasarkan pekerjaan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q5", data=df_indonesia)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan jumlah responden Global berdasarkan pekerjaan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q5", data=df_global[1:])
    st.pyplot(fig)
countPlot()
