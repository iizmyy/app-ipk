import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import joblib
from pathlib import Path

# Konfigurasi halaman harus diletakkan sebelum komponen Streamlit lainnya
st.set_page_config(
    layout="wide"
)

# Lokasi file mengikuti folder tempat app.py berada
BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR/"model_ipk.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.sidebar.markdown("#### Halaman Prediksi 💡")

st.title("Prediksi IPK Akhir Mahasiswa")
st.write(
    "Masukkan nilai IP Semester 1,2, dan 3 untuk "
    "memperoleh estimasi IPK akhir."
)

st.subheader("Input Nilai IP")
col1, col2, col3 = st.columns(3)

with col1:
    ips1 = st.number_input(
        "IP Semester 1",
        min_value=0.0, max_value=4.0,
        value=3.00, step=0.01, format="%.2f"
    )

with col2:
    ips2 = st.number_input(
        "IPS Semester 2",
        min_value=0.0, max_value=4.0,
        value=3.00, step=0.01, format="%.2f"
    )

with col3:
    ips3 = st.number_input(
        "IPS Semester 3",
        min_value=0.0, max_value=4.0,
        value=3.00, step=0.01, format="%.2f"
    )

if st.button("Prediksi IPK Akhir", type="primary"):
    # Nama dan urutan kolom harus sama dengan data training
    data_baru = pd.DataFrame([{
        "IPS1" : ips1,
        "IPS2" : ips2,
        "IPS3" : ips3
    }])

    hasil = float(model.predict(data_baru)[0])

    st.subheader("Hasil Prediksi")
    st.metric("Estimasi IPK Akhir", f"{hasil:.2f}")

    if 0 <= hasil <= 4:
        st.success(
            f"Berdasarkan input yang diberikan, estimasi IPK akhir "
            f"mahasiswa adalah {hasil:.2f}."
        )
    else:
        st.warning(
            f"Model menghasilkan estimasi {hasil:.2f}, di luar "
            "rentang IPK 0–4. Hasil perlu ditinjau."
        )

    with st.expander("Lihat data yang dikirim ke model"):
        st.dataframe(data_baru, use_container_width=True)

st.caption(
    "Hasil merupakan estimasi model berdasarkan pola pada data latih, "
    "bukan jaminan menjadi IPK akhir mahasiswa."
)