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

# 📅 **Fitur Interaktif: Filter berdasarkan rentang tanggal**
st.subheader("📅 Penyewaan Sepeda Berdasarkan Rentang Waktu")

date_range = st.date_input(
    "Pilih Rentang Waktu",
    value=(day_df['dteday'].min(), day_df['dteday'].max()),
    min_value=day_df['dteday'].min(),
    max_value=day_df['dteday'].max()
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = day_df['dteday'].min(), day_df['dteday'].max()

filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & (day_df['dteday'] <= pd.to_datetime(end_date))]

# 📊 **Total Penyewaan Sepeda per Bulan**
st.subheader("📊 Total Penyewaan Sepeda per Bulan")
filtered_day_df['month'] = filtered_day_df['dteday'].dt.month
monthly_rentals = filtered_day_df.groupby('month')['cnt'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10,6))
sns.barplot(data=monthly_rentals, x='month', y='cnt', ax=ax, palette='viridis')
ax.set_xlabel("Bulan")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

# 🌡️ **Pengaruh Suhu terhadap Penyewaan Sepeda**
st.subheader("🌡️ Pengaruh Suhu terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(data=filtered_day_df, x='temp', y='cnt', ax=ax)
ax.set_xlabel("Suhu Normalisasi")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

# 🍂 **Interaksi: Filter berdasarkan musim**
st.subheader("🍂 Penyewaan Sepeda Berdasarkan Musim")
selected_season = st.selectbox("Pilih Musim", options=day_df['season'].unique())

season_filtered_df = day_df[day_df['season'] == selected_season]

fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=season_filtered_df, x='dteday', y='cnt', ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

# 🌦 **Fitur Interaktif Baru: Penyewaan Sepeda Berdasarkan Cuaca**
st.subheader("🌦 Penyewaan Sepeda Berdasarkan Cuaca")
selected_weather = st.selectbox("Pilih Kondisi Cuaca", options=day_df['weathersit'].unique())

weather_filtered_df = day_df[day_df['weathersit'] == selected_weather]

fig, ax = plt.subplots(figsize=(12,6))
sns.lineplot(data=weather_filtered_df, x='dteday', y='cnt', ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan")
st.pyplot(fig)

st.write("✨ Dashboard ini dibuat menggunakan Streamlit dengan fitur interaktif.")

