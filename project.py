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
df_global = df_global[1:]
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
    sns.countplot(y="Q2", data=df_global)
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden berdasarkan tingkat pendidikan
st.header('Perbandingan jumlah responden Indonesia berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q4", data=df_indonesia, order = df_indonesia['Q4'].value_counts().index)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan jumlah responden Global berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q4", data=df_global, order = df_global['Q4'].value_counts().index)
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden berdasarkan status pekerjaan
st.header('Perbandingan jumlah responden Indonesia berdasarkan pekerjaan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q5", data=df_indonesia, order = df_indonesia['Q5'].value_counts().index)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan jumlah responden Global berdasarkan pekerjaan')
def countPlot():
    fig = plt.figure(figsize=(10, 12))
    sns.countplot(y="Q5", data=df_global, order = df_global['Q5'].value_counts().index)
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden berdasarkan pengalaman programming
st.header('Perbandingan jumlah responden Indonesia berdasarkan pengalaman programming')
def barPlot():
    st.bar_chart(df_indonesia['Q6'].value_counts().reindex(['Belum Pernah', '< 1 years', '1-3 years', '3-5 years','5-10 years','10-20 years','20+ years']))
barPlot()

st.header('Perbandingan jumlah responden Global berdasarkan pengalaman programming')
def barPlot():
    df_global_full = pd.read_csv('https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/survey_2021_responses.csv')
    st.bar_chart(df_global_full['Q6'].value_counts().reindex(['Belum Pernah', '< 1 years', '1-3 years', '3-5 years','5-10 years','10-20 years','20+ years']))
barPlot()

