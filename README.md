# Bike Sharing Data Analysis Dashboard

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data penggunaan layanan penyewaan sepeda berdasarkan dataset Bike Sharing Dataset. Analisis ini mencakup eksplorasi data, pembersihan data, visualisasi data, dan pembuatan dashboard interaktif menggunakan Streamlit.

## Struktur Proyek

```
Bike_Sharing_Analysis/
│-- dataset/
│   ├── day.csv
│   ├── hour.csv
│-- dashboard.py
│-- notebooks.ipynb
│-- requirements.txt
│-- README.md
│-- url.txt (Opsional, jika dashboard dideploy)
```

## Cara Menjalankan Dashboard

### 1. Persiapan Lingkungan
Sebelum menjalankan proyek ini, pastikan Anda telah menginstal Python dan pustaka yang diperlukan. Anda dapat menginstal pustaka yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
```

### 2. Menjalankan Dashboard
Setelah semua dependensi terinstal, jalankan perintah berikut untuk memulai dashboard Streamlit:

```bash
streamlit run dashboard.py
```

Dashboard akan berjalan dan dapat diakses melalui browser di alamat yang diberikan oleh Streamlit, biasanya `http://localhost:8501`.

## Konten Dashboard
- **Visualisasi data penggunaan sepeda** berdasarkan dataset.
- **Analisis tren penggunaan sepeda** berdasarkan faktor-faktor tertentu.
- **Interaksi dinamis** untuk mengeksplorasi data lebih lanjut.

## Opsi Deploy ke Streamlit Cloud (Opsional)
Jika ingin mendeply dashboard ke Streamlit Cloud, pastikan proyek ini tersedia di repositori GitHub, lalu ikuti panduan pada [Streamlit Cloud](https://share.streamlit.io/).

Jika dashboard telah berhasil dideploy, tautannya bisa ditulis di dalam `url.txt`.

## Kontributor
- **Nama:** Wahyu Bagas Prastyo
- **Email:** wbagas700@gmail.com
- **ID Dicoding:** MC129D5Y0205

