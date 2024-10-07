import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul Aplikasi
st.title("Bike sharing dataset ✨")
st.write("Nama: Amalia Putri")
st.write("Email: m384b4kx0446@bangkit.academy")
st.write("ID Dicoding: aleailearn")

# Exploratory Data Analysis (EDA)
st.title("Exploratory Data Analysis (EDA)")

# Sample data for demonstration
df_day = pd.read_csv('Data/day.csv')

# Random sampling of all rows
df_day_sample = df_day.sample(frac=1)

# Descriptive statistics for DAY
st.subheader('Descriptive Statistics for day Data')
st.write("Statistika deskriptif dilakukan untuk memahami karakteristik data, termasuk ukuran pusat, penyebaran, dan pola.")
day_stats = df_day_sample.describe(include='all')
st.write(day_stats)

# Plot histograms for 'temp', 'atemp', 'hum', 'windspeed', and 'cnt' columns
st.subheader('Histograms of Selected Features')
st.write("Analisis histogram dan KDE (Kernel Density Estimation) untuk kolom 'cnt' (jumlah penyewaan) ini membantu dalam pengambilan keputusan strategis berdasarkan pola distribusi jumlah penyewaan.")
fig, ax = plt.subplots(figsize=(10, 8))
df_day_sample[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].hist(bins=30, ax=ax)
plt.suptitle('Histogram of DAY Data')
st.pyplot(fig)

# Plot histogram with seaborn for 'cnt' column
st.subheader('Distribusi Kolom cnt')
st.write("Analisis distribusi kolom 'cnt' memberikan wawasan yang berguna untuk pengambilan keputusan strategis dalam konteks penyewaan.")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.histplot(df_day_sample['cnt'], kde=True, ax=ax2)
ax2.set_title('Distribusi Kolom cnt')
ax2.set_xlabel('Jumlah Penyewaan (cnt)')
ax2.set_ylabel('Frekuensi')
st.pyplot(fig2)

# Memastikan hanya kolom numerik yang dipilih untuk korelasi
df_day_numeric = df_day.select_dtypes(include=[np.number])

# Korelasi untuk DAY
st.subheader('Analisis Korelasi')
st.write("Secara keseluruhan, analisis korelasi ini memberikan pemahaman mendalam tentang faktor-faktor yang mempengaruhi jumlah penyewaan sepeda, serta bagaimana memanfaatkan wawasan ini untuk strategi bisnis yang lebih baik.")
day_corr = df_day_numeric.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(day_corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap for DAY Data')
st.pyplot(plt)

# Menghitung korelasi Pearson antara temp dan cnt untuk df_day
correlation = df_day['temp'].corr(df_day['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada dataset DAY: {correlation}")

# Scatter plot untuk visualisasi
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_day['temp'], y=df_day['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Dataset DAY')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)

# Membagi data menjadi hari kerja dan hari libur
df_workingday = df_day[df_day['workingday'] == 1]
df_holiday = df_day[df_day['workingday'] == 0]

# Menghitung korelasi Pearson antara suhu (temp) dan jumlah penyewaan (cnt) pada hari kerja
correlation_workingday = df_workingday['temp'].corr(df_workingday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari kerja: {correlation_workingday}")

# Menghitung korelasi Pearson antara suhu (temp) dan jumlah penyewaan (cnt) pada hari libur
correlation_holiday = df_holiday['temp'].corr(df_holiday['cnt'])
st.write(f"Korelasi antara suhu (temp) dan jumlah penyewaan (cnt) pada hari libur: {correlation_holiday}")

# Membuat scatter plot untuk hari kerja
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_workingday['temp'], y=df_workingday['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Hari Kerja')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)

# Membuat scatter plot untuk hari libur
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df_holiday['temp'], y=df_holiday['cnt'])
plt.title('Hubungan antara Suhu (temp) dan Jumlah Penyewaan (cnt) pada Hari Libur')
plt.xlabel('Suhu (temp)')
plt.ylabel('Jumlah Penyewaan (cnt)')
st.pyplot(plt)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Menghitung rata-rata suhu dan jumlah penyewaan per kategori
mean_workingday = df_workingday.groupby('workingday')[['temp', 'cnt']].mean().reset_index()
mean_holiday = df_holiday.groupby('workingday')[['temp', 'cnt']].mean().reset_index()

# Set style
sns.set(style="whitegrid")

# Menambahkan offset untuk membuat bar bersanding
bar_width = 0.35  # Lebar bar
index = np.arange(2)  # Indeks posisi untuk kategori

# Bar plot untuk hari kerja
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot untuk 'cnt' (Jumlah Penyewaan) dengan warna biru
bars1 = ax1.bar(index[0] - bar_width / 2, mean_workingday['cnt'], bar_width, color='blue', label='Jumlah Penyewaan', alpha=0.6)

# Membuat sumbu y kedua untuk 'temp' (Suhu)
ax2 = ax1.twinx()
bars2 = ax2.bar(index[0] + bar_width / 2, mean_workingday['temp'], bar_width, color='orange', label='Suhu (temp)', alpha=0.9)

# Menambahkan label, judul, dan legend
ax1.set_xlabel('Hari Kerja', fontsize=14)
ax1.set_ylabel('Jumlah Penyewaan', fontsize=14)
ax2.set_ylabel('Suhu (temp)', fontsize=14)
plt.title('Rata-rata Suhu dan Jumlah Penyewaan pada Hari Kerja', fontsize=16)

# Modifikasi label pada sumbu x
ax1.set_xticks(index)  # Set tick positions
ax1.set_xticklabels(['Hari Libur', 'Hari Kerja'])  # Set tick labels

# Menambahkan legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Menambahkan nilai pada bar
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

# Tampilkan plot di Streamlit
st.pyplot(fig)

# Bar plot untuk hari libur
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot untuk 'cnt' (Jumlah Penyewaan) dengan warna biru
bars1 = ax1.bar(index[1] - bar_width / 2, mean_holiday['cnt'], bar_width, color='blue', label='Jumlah Penyewaan', alpha=0.6)

# Membuat sumbu y kedua untuk 'temp' (Suhu)
ax2 = ax1.twinx()
bars2 = ax2.bar(index[1] + bar_width / 2, mean_holiday['temp'], bar_width, color='orange', label='Suhu (temp)', alpha=0.9)

# Menambahkan label, judul, dan legend
ax1.set_xlabel('Hari Libur', fontsize=14)
ax1.set_ylabel('Jumlah Penyewaan', fontsize=14)
ax2.set_ylabel('Suhu (temp)', fontsize=14)
plt.title('Rata-rata Suhu dan Jumlah Penyewaan pada Hari Libur', fontsize=16)

# Modifikasi label pada sumbu x
ax1.set_xticks(index)  # Set tick positions
ax1.set_xticklabels(['Hari Libur', 'Hari Kerja'])  # Set tick labels

# Menambahkan legend
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Menambahkan nilai pada bar
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval, int(yval), ha='center', va='bottom')

# Tampilkan plot di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Menjawab pertanyaan 1
st.subheader('Visualization & Explanatory Analysis')
st.write("Pertanyaan 1: Bagaimana pengaruh suhu (temp) terhadap jumlah total sewa (cnt) pada hari kerja dibandingkan dengan hari libur?")

# Pastikan kolom 'workingday' ada
if 'workingday' not in df_day.columns:
    st.error("Kolom 'workingday' tidak ditemukan dalam DataFrame.")
else:
    # Membagi data menjadi hari kerja dan hari libur
    df_workingday = df_day[df_day['workingday'] == 1]
    df_holiday = df_day[df_day['workingday'] == 0]

    # Menghitung rata-rata suhu dan jumlah penyewaan per kategori
    mean_workingday = df_workingday[['temp', 'cnt']].mean()
    mean_holiday = df_holiday[['temp', 'cnt']].mean()

    # Set style
    sns.set(style="whitegrid")

    # Memisahkan data menjadi hari kerja dan hari libur
if 'workingday' not in df_day.columns:
    st.error("Kolom 'workingday' tidak ditemukan dalam DataFrame.")
else:
    df_workingday = df_day[df_day['workingday'] == 1]
    df_holiday = df_day[df_day['workingday'] == 0]

    # Menghitung rata-rata suhu dan jumlah penyewaan per kategori
    mean_workingday = df_workingday[['temp', 'cnt']].mean()
    mean_holiday = df_holiday[['temp', 'cnt']].mean()

    # Menghitung rata-rata suhu dan jumlah sewa
    summary_df = df_day.groupby('workingday').agg({'temp': 'mean', 'cnt': 'mean'}).reset_index()
    summary_df['workingday'] = summary_df['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

    # Menampilkan DataFrame summary
    st.write(summary_df)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
df = pd.read_csv("Data/day.csv")  # Make sure to specify the correct path to your CSV file
df = pd.read_csv("Data/hour.csv")

# Check if the 'holiday' column exists in the DataFrame
if 'holiday' not in df.columns:
    st.error("Kolom 'holiday' tidak ditemukan dalam DataFrame.")
else:
    # Memisahkan data berdasarkan hari kerja dan hari libur
    workdays_df = df[df['holiday'] == 0]
    holidays_df = df[df['holiday'] == 1]

    # Menghitung rata-rata suhu dan jumlah sewa
    summary_df = df.groupby('holiday').agg({'temp': 'mean', 'cnt': 'mean'}).reset_index()
    summary_df['holiday'] = summary_df['holiday'].map({0: 'Hari Kerja', 1: 'Hari Libur'})

    # Menampilkan DataFrame summary
    st.write(summary_df)

    plt.figure(figsize=(12, 6))

    # Subplot untuk Suhu
    plt.subplot(1, 2, 1)
    sns.barplot(x='holiday', y='temp', data=summary_df, palette='coolwarm')
    plt.title('Rata-Rata Suhu pada Hari Kerja vs Hari Libur')
    plt.ylabel('Rata-Rata Suhu (°C)')
    plt.xlabel('Tipe Hari')

    # Subplot untuk Jumlah Sewa
    plt.subplot(1, 2, 2)
    sns.barplot(x='holiday', y='cnt', data=summary_df, palette='coolwarm')
    plt.title('Rata-Rata Jumlah Sewa pada Hari Kerja vs Hari Libur')
    plt.ylabel('Rata-Rata Jumlah Sewa')
    plt.xlabel('Tipe Hari')

    plt.tight_layout()

    # Display the plots in Streamlit
    st.pyplot(plt)

    # Jawaban
    st.write("Dari visualisasi di atas, kita dapat menarik beberapa kesimpulan:")
    st.write("- Rata-Rata Suhu: Rata-rata suhu pada hari kerja dan hari libur dapat berbeda secara signifikan. Perhatikan apakah hari libur memiliki suhu yang lebih tinggi atau lebih rendah.")
    st.write("- Rata-Rata Jumlah Sewa: Rata-rata jumlah sewa pada hari kerja mungkin lebih tinggi dibandingkan dengan hari libur atau sebaliknya. Ini bisa mengindikasikan pengaruh suhu terhadap perilaku penyewa, di mana suhu yang lebih tinggi mungkin meningkatkan jumlah sewa, baik pada hari kerja maupun hari libur.")


# Menjawab pertanyaan 2
st.write("Pertanyaan 2: Strategi marketing apa yang dapat diterapkan untuk meningkatkan jumlah pengguna (cnt) pada hari kerja ketika kondisi cuaca buruk?")

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.dates import DateFormatter

# Definisikan ambang untuk kondisi cuaca buruk
bad_weather_threshold_temp = 0.3  # Misalnya, suhu di bawah 0.3
bad_weather_threshold_weathersit = 2  # Kategorikan kondisi cuaca 2 (hujan)

# Mengubah kolom 'dteday' menjadi tipe datetime
df['dteday'] = pd.to_datetime(df['dteday'])

# Ambil data hari kerja dengan kondisi cuaca buruk
bad_weather_workdays_df = df[(df['workingday'] == 1) &
                             (df['temp'] < bad_weather_threshold_temp) &
                             (df['weathersit'] >= bad_weather_threshold_weathersit)]

# Menampilkan data yang telah difilter
st.write("Data Hari Kerja dengan Cuaca Buruk:")
st.write(bad_weather_workdays_df.head())

# Membuat visualisasi
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=bad_weather_workdays_df, x='dteday', y='cnt', marker='o', color='orange', ax=ax)

# Mengatur format tanggal dan tampilan x-axis
date_form = DateFormatter("%Y-%m-%d")  # Format tanggal
ax.xaxis.set_major_formatter(date_form)
ax.set_title('Jumlah Sewa pada Hari Kerja dengan Cuaca Buruk')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Sewa (cnt)')
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Analisis Jumlah Sewa
average_cnt = bad_weather_workdays_df['cnt'].mean()
max_cnt = bad_weather_workdays_df['cnt'].max()
min_cnt = bad_weather_workdays_df['cnt'].min()

# Menampilkan hasil analisis
st.write(f"Rata-rata jumlah sewa pada hari kerja dengan cuaca buruk: {average_cnt:.2f}")
st.write(f"Jumlah sewa maksimum: {max_cnt}")
st.write(f"Jumlah sewa minimum: {min_cnt}")

# Membuat subplot tambahan jika diperlukan
fig, axes = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot jumlah sewa pada cuaca buruk
sns.lineplot(data=bad_weather_workdays_df, x='dteday', y='cnt', marker='o', color='blue', ax=axes[0])
axes[0].set_title('Jumlah Sewa pada Hari Kerja dengan Cuaca Buruk')
axes[0].set_ylabel('Jumlah Sewa (cnt)')
axes[0].xaxis.set_major_formatter(date_form)

# Plot rata-rata suhu harian (misalnya)
sns.lineplot(data=bad_weather_workdays_df, x='dteday', y='temp', marker='o', color='red', ax=axes[1])
axes[1].set_title('Suhu pada Hari Kerja dengan Cuaca Buruk')
axes[1].set_xlabel('Tanggal')
axes[1].set_ylabel('Suhu (temp)')
axes[1].xaxis.set_major_formatter(date_form)

# Rotasi tanggal agar terbaca dengan baik
plt.xticks(rotation=45)
plt.tight_layout()

# Menampilkan subplot di Streamlit
st.pyplot(fig)



# kesimpulan
st.subheader('Kesimpulan')
st.write("Grafik di atas menunjukkan fluktuasi jumlah penyewaan sepeda pada hari kerja dengan cuaca buruk, dengan tren penyewaan berkisar antara 100 hingga 200 penyewaan per hari, namun terdapat lonjakan signifikan yang mencapai lebih dari 700 penyewaan, yang kemungkinan dipengaruhi oleh faktor-faktor seperti acara khusus atau kebutuhan mendesak. Meskipun cuaca buruk umumnya berdampak negatif pada penggunaan sepeda, beberapa orang tetap memilih untuk menyewa sepeda. Saya mengkaji ulang pertanyan, dan mendapatkan beberapa ide ataupun strategi baru, seperti memberikan diskon khusus pada hari cuaca buruk, kampanye promosi berbasis cuaca melalui email atau aplikasi, serta pengembangan fitur yang memberikan rekomendasi aktivitas saat cuaca tidak mendukung. Selain itu, peluang kolaborasi dengan bisnis lokal dan fokus pada iklan yang menyoroti manfaat bersepeda sebagai solusi untuk tetap aktif meski cuaca buruk juga dapat dioptimalkan.")

# Menjawab pertanyaan 2
st.write("Berdasarkan analisis ini, saya memberikan beberapa strategi marketing yang dapat diterapkan untuk meningkatkan jumlah pengguna pada hari kerja ketika cuaca buruk dapat mencakup:")

st.write("1. Promosi Diskon untuk Hari Buruk: Tawarkan diskon khusus atau penawaran khusus untuk pengguna yang menyewa pada hari-hari dengan kondisi cuaca buruk.")

st.write("2. Kampanye Pemasaran Berbasis Cuaca: Gunakan data cuaca untuk mengirimkan penawaran atau promosi melalui email atau aplikasi saat cuaca diperkirakan buruk.")

st.write("3. Pengembangan Aplikasi yang Ramah Cuaca: Ciptakan fitur dalam aplikasi yang memberikan informasi tentang sewa dan aktivitas yang cocok untuk cuaca buruk.")

st.write("4. Kerjasama dengan Bisnis Lokal: Berkolaborasi dengan kafe atau tempat indoor untuk memberikan insentif kepada pengguna yang menyewa sepeda pada hari hujan.")

st.write("5. Strategi Pengiklanan: Fokus pada iklan yang menyoroti bagaimana menggunakan sepeda bisa menjadi solusi alternatif untuk tetap aktif bahkan ketika cuaca kurang baik.")

# kesimpulan
st.subheader("Analisis lanjutan yang saya lakukan, sebagai berikut:")
st.write("Analisis RFM (Recency, Frequency, Monetary) bertujuan untuk mengidentifikasi dan memahami perilaku pelanggan berdasarkan seberapa baru mereka melakukan transaksi, seberapa sering mereka berbelanja, dan berapa banyak yang mereka belanjakan. Meskipun hasil analisis menunjukkan bahwa hanya ada satu entri dalam DataFrame RFM, yang menandakan kurangnya variasi dalam data pelanggan, analisis ini tetap relevan sebagai langkah awal untuk menggali wawasan pelanggan. Dengan informasi ini, bisnis dapat memfokuskan upaya pemasaran untuk meningkatkan retensi pelanggan dan memaksimalkan pendapatan. Dalam konteks ini, meskipun data saat ini terbatas, analisis RFM dapat dijadikan alat untuk merencanakan strategi yang lebih baik di masa depan, terutama ketika lebih banyak data tersedia.")


