import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Pastikan path dataset sesuai agar bisa dijalankan dari mana saja
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Path ke lokasi script
DATASET_DIR = os.path.join(BASE_DIR, "dataset")

# Load dataset
day_df = pd.read_csv(os.path.join(DATASET_DIR, "day.csv"))
hour_df = pd.read_csv(os.path.join(DATASET_DIR, "hour.csv"))

# Konversi tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Judul dashboard
st.title("🚴‍♂️ Bike Sharing Data Analysis")

# Heatmap korelasi
st.subheader("🔍 Faktor yang Mempengaruhi Penyewaan")
fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(day_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

# Visualisasi penyewaan berdasarkan jam
st.subheader("⏰ Tren Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=hour_df, x='hr', y='cnt', estimator='mean', ci=None, ax=ax)
ax.set_xlabel("Hour of the Day")
ax.set_ylabel("Average Rentals")
st.pyplot(fig)

# Filter interaktif berdasarkan musim
st.subheader("📅 Penyewaan Sepeda Berdasarkan Musim")
selected_season = st.selectbox("Pilih Musim", options=day_df['season'].unique())
filtered_df = day_df[day_df['season'] == selected_season]
fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=filtered_df, x='dteday', y='cnt', ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Total Rentals")
st.pyplot(fig)

st.write("✨ Dashboard ini dibuat menggunakan Streamlit.")
