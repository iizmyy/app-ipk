import streamlit as st

# Pendefinisian halaman
halaman_utama = st.Page("halaman_utama.py", title="Halaman Utama", icon="🏠")
hal_1 = st.Page("hal_1.py", title="EDA", icon="🔍")
hal_2 = st.Page("hal_2.py", title="Prediksi IPK", icon="💡")

# Set up Navigation
pg = st.navigation([halaman_utama, hal_1, hal_2])

# Jalankan halaman terpilih
pg.run()