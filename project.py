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
df_global_full = pd.read_csv('https://filedn.com/lePVfyAoiNxFBjMKNqcr2O7/MICROCREDENTIAL/ProjectTugasAkhir/survey_2021_responses.csv')
df_global = df_global_full[1:]
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
st.header('Kategori Umur responden di dunia')
st.bar_chart(df_global['Q1'].value_counts().sort_index())

# kategori berdasarkan jenis kelamin
st.header('Kategori Jenis Kelamin Responden Indonesia')
def countPlot():
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(y="Q2", data=df_indonesia)
    st.pyplot(fig)
countPlot()

st.header('Kategori Jenis Kelamin responden di dunia')
def countPlot():
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(y="Q2", data=df_global)
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden berdasarkan tingkat pendidikan
st.header('Perbandingan jumlah responden Indonesia berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(y="Q4", data=df_indonesia, order = df_indonesia['Q4'].value_counts().index)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan jumlah responden di dunia berdasarkan tingkat pendidikan')
def countPlot():
    fig = plt.figure(figsize=(10, 6))
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

st.header('Perbandingan jumlah responden di dunia berdasarkan pekerjaan')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q5", data=df_global, order = df_global['Q5'].value_counts().index)
    st.pyplot(fig)
countPlot()

# Perbandingan jumlah responden berdasarkan pengalaman programming
st.header('Perbandingan jumlah responden Indonesia berdasarkan pengalaman programming')
def barPlot():
    st.bar_chart(df_indonesia['Q6'].value_counts().reindex(['I have never written code', '< 1 years', '1-3 years', '3-5 years','5-10 years','10-20 years','20+ years']))
barPlot()

st.header('Perbandingan jumlah responden di dunia berdasarkan pengalaman programming')
def barPlot():
    st.bar_chart(df_global['Q6'].value_counts().reindex(['I have never written code', '< 1 years', '1-3 years', '3-5 years','5-10 years','10-20 years','20+ years']))
barPlot()

# Perbandingan Bahasa Pemrograman yang Digunakan
st.header('Perbandingan Bahasa Pemrograman yang Digunakan di Indonesia')
def barPlot():
    languages = ['Python','R','SQL','C','C++','Java',"Javascript","Julia","Bash","Matlab"]
    python=df_indonesia.Q7_Part_1.value_counts()[0]
    r= df_indonesia.Q7_Part_2.value_counts()[0]
    sql=df_indonesia.Q7_Part_3.value_counts()[0]
    c=df_indonesia.Q7_Part_4.value_counts()[0]
    c_plus =df_indonesia.Q7_Part_5.value_counts()[0]
    java = df_indonesia.Q7_Part_6.value_counts()[0]
    javascript=df_indonesia.Q7_Part_7.value_counts()[0]
    julia = df_indonesia.Q7_Part_8.value_counts()[0]
    bash = df_indonesia.Q7_Part_10.value_counts()[0]
    matlab = df_indonesia.Q7_Part_11.value_counts()[0]
    values_1 = [python,r,sql,c,c_plus,java,javascript,julia,bash,matlab]

    fig = plt.figure(figsize = (10, 6))

    plt.bar(languages,values_1)
    plt.xticks(rotation=45)
    plt.title("Bahasa Pemrograman yang Paling Banyak Digunakan di Indonesia")
    st.pyplot(fig)
barPlot()

st.header('Perbandingan Bahasa Pemrograman yang Digunakan di Dunia')
def barPlot():
    languages_global = ['Python','R','SQL','C','C++','Java',"Javascript","Julia","Swift","Bash","Matlab"]
    python=df_global.Q7_Part_1.value_counts()[0]
    r= df_global.Q7_Part_2.value_counts()[0]
    sql=df_global.Q7_Part_3.value_counts()[0]
    c=df_global.Q7_Part_4.value_counts()[0]
    c_plus =df_global.Q7_Part_5.value_counts()[0]
    java = df_global.Q7_Part_6.value_counts()[0]
    javascript=df_global.Q7_Part_7.value_counts()[0]
    julia = df_global.Q7_Part_8.value_counts()[0]
    swift = df_global.Q7_Part_9.value_counts()[0]
    bash = df_global.Q7_Part_10.value_counts()[0]
    matlab = df_global.Q7_Part_11.value_counts()[0]
    values_2 = [python,r,sql,c,c_plus,java,javascript,julia,swift,bash,matlab]

    fig = plt.figure(figsize = (10, 6))

    plt.bar(languages_global,values_2)
    plt.xticks(rotation=45)
    plt.title("Bahasa Pemrograman yang Paling Banyak Digunakan di Dunia")
    st.pyplot(fig)
barPlot()

st.write('Bahasa pemrograman yang paling populer adalah Python, seperti yang diharapkan baik di Indonesia maupun di Dunia.')
st.write('Setelah kita melakukan beberapa penelitian sederhana, Python banyak digunakan dari bahasa lain karena: Python lebih produktif, memiliki daya saing dan inovasi yang cepat, memiliki berbagai library, framework, dan komunitas yang sangat besar.')

# Perbandingan Pekerjaan Berdasarkan Bidang Industri
st.header('Perbandingan Pekerjaan Berdasarkan Bidang Industri di Indonesia')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q20", data=df_indonesia, order = df_indonesia['Q20'].value_counts().index)
    st.pyplot(fig)
countPlot()

st.header('Perbandingan Pekerjaan Berdasarkan Bidang Industri di Dunia')
def countPlot():
    fig = plt.figure(figsize=(10, 8))
    sns.countplot(y="Q20", data=df_global, order = df_global['Q20'].value_counts().index)
    st.pyplot(fig)
countPlot()

st.write('Kita dapat melihat bahwa sebagian besar responden di Dunia saat ini bekerja di industri berbasis teknologi. Sedangkan di Indonesia, sebagian besar saat ini bekerja di bidang akademik/pendidikan. Kita bisa berharap lebih banyak orang Indonesia memasuki industri berbasis teknologi')

# Perbandingan Jumlah Gaji yang Diterima Dalam USD
st.header('Perbandingan Jumlah Gaji yang Diterima di Indonesia Dalam USD')
def barPlot():
    st.bar_chart(df_indonesia['Q25'].value_counts().reindex(['$0-999', '1,000-1,999', '2,000-2,999', '3,000-3,999','4,000-4,999','5,000-7,499', '7,500-9,999','10,000-14,999','15,000-19,999','20,000-24,999','25,000-29,999','30,000-39,999', '40,000-49,999','50,000-59,999','60,000-69,999','70,000-79,999','80,000-89,999', '90,000-99,999','100,000-124,999','125,000-149,999','150,000-199,999','200,000-249,999','250,000-299,999', '300,000-499,999','$500,000-999,999','>$1,000,000']))
barPlot()

st.header('Perbandingan Jumlah Gaji yang Diterima di Dunia Dalam USD')
def barPlot():
    st.bar_chart(df_global['Q25'].value_counts().reindex(['$0-999', '1,000-1,999', '2,000-2,999', '3,000-3,999','4,000-4,999','5,000-7,499', '7,500-9,999','10,000-14,999','15,000-19,999','20,000-24,999','25,000-29,999','30,000-39,999', '40,000-49,999','50,000-59,999','60,000-69,999','70,000-79,999','80,000-89,999', '90,000-99,999','100,000-124,999','125,000-149,999','150,000-199,999','200,000-249,999','250,000-299,999', '300,000-499,999','$500,000-999,999','>$1,000,000']))
barPlot()

st.write('Dari grafik di atas kita dapat melihat bahwa gaji untuk data scientist baik di Indonesia maupun global sebagian besar adalah $0-999. Ini menunjukkan bahwa gaji di Indonesia pun cukup menjanjikan dan kompetitif.')

# Perbandingan Penyedia Course yang Digunakan
st.header('Perbandingan Penyedia Course yang Digunakan di Indonesia')
def barPlot():
    course = ['Cousera','edX',"Kaggle Learn Courses",'DataCamp','Fast.ai','Udacity',"Udemy","LinkedIn Learning","Cloud","University Courses","None"]
    coursera=df_indonesia.Q40_Part_1.value_counts()[0]
    edx= df_indonesia.Q40_Part_2.value_counts()[0]
    klc=df_indonesia.Q40_Part_3.value_counts()[0]
    dc=df_indonesia.Q40_Part_4.value_counts()[0]
    fa =df_indonesia.Q40_Part_5.value_counts()[0]
    udacity = df_indonesia.Q40_Part_6.value_counts()[0]
    udemy=df_indonesia.Q40_Part_7.value_counts()[0]
    ll = df_indonesia.Q40_Part_8.value_counts()[0]
    cc = df_indonesia.Q40_Part_9.value_counts()[0]
    uc = df_indonesia.Q40_Part_10.value_counts()[0]
    none = df_indonesia.Q40_Part_11.value_counts()[0]
    values_3 = [coursera,edx,klc,dc,fa,udacity,udemy,ll,cc,uc,none]

    fig = plt.figure(figsize = (10, 6))

    plt.bar(course,values_3)
    plt.xticks(rotation=90)
    plt.title("Penyedia Course yang Sering Digunakan di Indonesia")
    st.pyplot(fig)
barPlot()

st.header('Perbandingan Penyedia Course yang Digunakan di Indonesia')
def barPlot():
    course_global = ['Cousera','edX',"Kaggle Learn Courses",'DataCamp','Fast.ai','Udacity',"Udemy","LinkedIn Learning","Cloud","University Courses","None"]
    coursera=df_global.Q40_Part_1.value_counts()[0]
    edx= df_global.Q40_Part_2.value_counts()[0]
    klc=df_global.Q40_Part_3.value_counts()[0]
    dc=df_global.Q40_Part_4.value_counts()[0]
    fa =df_global.Q40_Part_5.value_counts()[0]
    udacity = df_global.Q40_Part_6.value_counts()[0]
    udemy=df_global.Q40_Part_7.value_counts()[0]
    ll = df_global.Q40_Part_8.value_counts()[0]
    cc = df_global.Q40_Part_9.value_counts()[0]
    uc = df_global.Q40_Part_10.value_counts()[0]
    none = df_global.Q40_Part_11.value_counts()[0]
    values_4 = [coursera,edx,klc,dc,fa,udacity,udemy,ll,cc,uc,none]

    fig = plt.figure(figsize = (10, 6))

    plt.bar(course_global,values_4)
    plt.xticks(rotation=90)
    plt.title("Penyedia Course yang Sering Digunakan di Dunia")
    st.pyplot(fig)
barPlot()

st.write('Dari bagan di atas, kita dapat melihat bahwa Kaggle Learn Courses adalah platform paling populer di Indonesia di kalangan pelajar baru untuk kursus terkait Ilmu Data, sementara Coursera adalah platform paling populer secara global.')

# Perbandingan Tools yang Digunakan
st.header('Perbandingan Tools yang Digunakan di Indonesia')
def countPlot():
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(y="Q41",palette = 'muted', data=df_indonesia, order = df_indonesia['Q41'])
    st.pyplot(fig)
countPlot()

st.header('Perbandingan Tools yang Digunakan di Dunia')
def countPlot():
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(y="Q41",palette = 'muted', data=df_global, order = df_global['Q41'])
    st.pyplot(fig)
countPlot()

st.write('Dari grafik di atas, orang Indonesia tampaknya lebih memilih perangkat lunak statistik dasar untuk melakukan analisis data mereka sementara orang-orang secara global menggunakan development tools (RStudio, jupyterlab, dll) sebagai tools utama mereka.')
st.write('Hal ini menunjukkan bahwa data scientist di Indonesia harus meningkatkan skillnya agar dapat bersaing secara global.')