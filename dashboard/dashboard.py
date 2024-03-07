import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set_theme(style='dark')

def showReport():
    fig, ax = plt.subplots(figsize=(10, 6))
    count_per_month = df.groupby("mnth")["cnt"].sum()
    plt.plot(count_per_month.index, count_per_month.values, marker='o', linestyle='-')
    plt.title('Bike share per month')
    plt.xlabel('Bulan')
    plt.ylabel('Count')
    plt.grid(True)
    st.pyplot(fig)

def showCorrelation():
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df['temp'], df['cnt'])
    plt.title('Scatter Plot of Temperature vs Count')
    plt.xlabel('Temperature')
    plt.ylabel('Count')
    plt.grid(True)

    correlation_coefficient = np.corrcoef(df['temp'], df['cnt'])[0, 1]
    plt.annotate(f'Correlation Coefficient: {correlation_coefficient:.2f}',
                xy=(0.15, 0.90),
                xycoords='axes fraction',
                ha='center',
                fontsize=10)

    st.pyplot(fig)

df = pd.read_csv("main_data.csv")

st.header(':bike: Bike Sharing Report :bike:')

tab1, tab2 = st.tabs(["Annual report", "Temp vs Count Correlation"])
 
with tab1:
    st.header("Annual report")
    showReport()
    with st.expander("Penjelasan lebih lanjut"):
        st.write(
            """ Terlihat, puncak penggunaan sewa sepeda terjadi pada bulan 8 atau bulan Agustus, yang diikuti
            dengan penurun berlanjut sampai bulan 12 atau Desember. Kita dapat menebak bahwa ini terjadi karena
            mulainya musim gugur di bulan September yang artinya adanya penurunan temperatur.
            """
        )
 
with tab2:
    st.header("Temp vs Count Correlation")
    showCorrelation()
    with st.expander("Penjelasan lebih lanjut"):
        st.write(
            """ Temperatur dan Count (pengguna user terdaftar dan user kasual) memiliki tingkat korelasi yang tinggi,
            yang berarti temperatur merupakan salah satu faktor penggunaan sewa sepeda.
            """
        )
