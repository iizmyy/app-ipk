import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from pathlib import Path

# Konfigurasi halaman harus diletakkan sebelum komponen Streamlit lainnya
st.set_page_config(
    layout="wide"
)

# Lokasi file mengikuti folder tempat app.py berada
BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR/"dataset/dataset_alumni_2.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.sidebar.markdown("#### Halaman EDA 🔍")

st.title("Exploratory Data Analysis")
st.write("Explorasi data IPS semester 1-3 dan IPK akhir mahasiswa")

# Eksplorasi awal data
kolom_angka = ["IPS1", "IPS2", "IPS3", "IPK_Akhir"]
jumlah_data = len(df)
jumlah_kolom = len(df.columns)
jumlah_missing = int(df.isna().sum().sum())

# Summary Card
c1, c2, c3 = st.columns(3)
c1.metric("Jumlah Data", jumlah_data)
c2.metric("Jumlah Atribut", jumlah_kolom)
c3.metric("Missing Values", jumlah_missing)

st.subheader("Sampel Data Alumni")
st.dataframe(df.head(), use_container_width=True)

st.subheader("Statistik Deskriptif")
st.dataframe(
    df[kolom_angka].describe().T,
    use_container_width=True
)

# Visualisasi 1 : Distribusi IPK akhir
st.subheader("1. Distribusi IPK Akhir")
fig, ax = plt.subplots(figsize=(8,4))
sns.histplot(
    data=df, x="IPK_Akhir",
    bins=5, kde=True, ax=ax
)
ax.set_title("Distribusi IPK Akhir")
ax.set_xlabel("IPK Akhir")
ax.set_ylabel("Frekuensi")
st.pyplot(fig)
plt.close(fig)

# Visualisasi 2: perbandingan IPS dan IPK akhir
st.subheader("2. Hubungan IPS dengan IPK Akhir")
fig, ax = plt.subplots(figsize=(8, 4))
for kolom in ["IPS1", "IPS2", "IPS3"]:
    sns.scatterplot(
        data=df, x=kolom, y="IPK_Akhir",
        label=kolom, ax=ax
    )
ax.set_title("IPS Semester 1–3 dan IPK Akhir")
ax.set_xlabel("Nilai IPS")
ax.set_ylabel("IPK Akhir")
ax.legend()
st.pyplot(fig)
plt.close(fig)

# Visualisasi 3: korelasi
st.subheader("3. Korelasi Antarvariabel")
corr = df[kolom_angka].corr()
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    corr, annot=True, cmap="Blues",
    vmin=-1, vmax=1, ax=ax
)
ax.set_title("Matriks Korelasi")
st.pyplot(fig)
plt.close(fig)

st.info("Catatan : Korelasi bukan menunjukkan hubungan sebab akibat")
