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
df1 = pd.read_csv('https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/survey_2021_responses.csv')
df_sample_global = df1.head()
st.write(df_sample_global)

# persiapan data frame Indonesia
st.header('Sample Data Survey Indonesia')
df_indonesia=df1[df1["Q3"]=="Indonesia"]
st.write('Dataset sudah difilter hanya Indonesia:')
df_sample_indo = df_indonesia.head()
st.write(df_sample_indo)
