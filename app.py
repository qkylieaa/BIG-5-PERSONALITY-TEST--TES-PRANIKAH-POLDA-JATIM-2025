import streamlit as st
import pandas as pd
import os

# ========================
# Load dataset Big Five
# ========================
df = pd.read_csv("fileoutput2025.csv")

# ========================
# Title & Header
# ========================
st.title("Blueprint Personality Test")
st.write("Isi 10 pertanyaan berikut untuk mengetahui tipe kepribadian Anda.")

# ========================
# Form Input Identitas
# ========================
nama = st.text_input("Nama")
umur = st.number_input("Umur", min_value=1, max_value=100)

st.write("---")

# ========================
# Pertanyaan
# ========================
pertanyaan = [
    "Saat melihat orang sukses, saya…",
    "Ketika suasana hati saya tidak stabil, saya…",
    "Saat saya menatap masa depan, saya merasa…",
    "Saat orang lain lambat merespons pesan saya, saya…",
    "Saat rencana besar gagal, saya…",
    "Saat membuat keputusan penting, saya lebih sering…",
    "Saat berada di lingkungan baru, saya…",
    "Saat menghadapi perbedaan pendapat dalam hubungan, saya…",
    "Saya ingin rumah tangga kami dikenal sebagai…",
    "Dalam berkomunikasi dengan pasangan, saya lebih suka…"
]

# ========================
# OPSI (SAMA PERSIS PUNYAMU)
# ========================
opsi = [
    [
        "Terinspirasi dan ingin tahu proses mereka.",
        "Termotivasi untuk bekerja lebih keras.",
        "Mengucapkan selamat dan menjadikannya energi positif.",
        "Ikut senang tanpa iri.",
        "Merasa minder dan membandingkan diri sendiri."
    ],
    [
        "Menulis jurnal atau refleksi diri.",
        "Mencari rutinitas untuk mengembalikan fokus.",
        "Berbicara pada orang lain.",
        "Berdiam dan menenangkan diri.",
        "Sulit mengontrol emosi."
    ],
    [
        "Penasaran akan hal baru.",
        "Termotivasi membangun hidup terencana.",
        "Bersemangat bersama orang terdekat.",
        "Tenang karena yakin semuanya baik.",
        "Cemas karena banyak yang tak bisa dikontrol."
    ],
    [
        "Berpikir mereka sedang sibuk.",
        "Mencatat agar tidak terulang.",
        "Mengirim pesan kedua yang ringan.",
        "Memakluminya.",
        "Merasa tidak dianggap penting."
    ],
    [
        "Melihatnya sebagai arah baru.",
        "Mengevaluasi kesalahan.",
        "Tetap tersenyum dan mencari cara lain.",
        "Menenangkan diri dan mendengarkan masukan.",
        "Sulit menerima kegagalan."
    ],
    [
        "Mengikuti intuisi.",
        "Mempertimbangkan data.",
        "Berdiskusi dengan orang lain.",
        "Memikirkan dampak bagi orang lain.",
        "Ragu karena takut salah."
    ],
    [
        "Tertantang mengenal hal baru.",
        "Menyesuaikan dengan aturan.",
        "Mudah berbaur.",
        "Membuat orang lain nyaman.",
        "Canggung dan menunggu diajak."
    ],
    [
        "Melihatnya sebagai peluang belajar.",
        "Mencari jalan tengah logis.",
        "Menjaga percakapan tetap hangat.",
        "Mengalah agar tidak konflik.",
        "Jadi sangat sensitif."
    ],
    [
        "Terbuka dan berkembang.",
        "Tertib dan terencana.",
        "Hangat dan penuh semangat.",
        "Damai dan memahami.",
        "Tenang tanpa tekanan."
    ],
    [
        "Membahas topik beragam.",
        "Menyampaikan hal penting secara terstruktur.",
        "Berbicara ekspresif.",
        "Mendengarkan dulu.",
        "Menarik diri saat suasana hati buruk."
    ]
]

# ========================
# Tampilan Soal
# ========================
jawaban = []

for idx, q in enumerate(pertanyaan):
    st.write(f"### {idx+1}. {q}")
    pilihan = st.radio("", opsi[idx], index=None, key=f"q{idx}")
    jawaban.append(pilihan)
    st.write("")


# ========================
# Tombol PROSES
# ========================
if st.button("Proses Hasil"):

    # Validasi
    if None in jawaban:
        st.error("Masih ada pertanyaan yang belum dijawab.")
        st.stop()

    # SKORING SEDERHANA (sementara)
    tipe_letter = "A"  # TODO: nanti bisa disesuaikan skoringnya

    # Ambil row tipe dari dataset
    data_tipe = df[df["Tipe_Letter"] == tipe_letter].iloc[0]

    # ========================
    # TAMPILKAN HASIL
    # ========================
    st.write("## 📌 Hasil Kepribadian Anda")
    st.write(f"**Nama:** {nama}")
    st.write(f"**Umur:** {umur}")
    st.write(f"**Tipe Kepribadian:** {data_tipe['Tipe_Big5']}")
    st.write("## 🧠 Deskripsi Kepribadian")
    st.write(data_tipe["Deskripsi"])
    st.write("## 💡 Saran untuk Hubungan / Pasangan")
    st.write(data_tipe["Saran_Pasangan"])
    st.write("## ⭐ Kelebihan")
    st.write(data_tipe["Kelebihan"])
    st.write("## ⚠ Kekurangan")
    st.write(data_tipe["Kekurangan"])

    # ========================
    # SIMPAN CSV (FIXED)
    # ========================
    output_file = "hasil_test_personality.csv"

    data_baru = {
        "Nama": [nama],
        "Umur": [umur],
        "Tipe_Letter": [tipe_letter],
        "Tipe_Big5": [data_tipe["Tipe_Big5"]],
        "Deskripsi": [data_tipe["Deskripsi"]],
        "Saran_Pasangan": [data_tipe["Saran_Pasangan"]],
        "Kelebihan": [data_tipe["Kelebihan"]],
        "Kekurangan": [data_tipe["Kekurangan"]],
    }

    df_baru = pd.DataFrame(data_baru)

    if not os.path.exists(output_file):
        df_baru.to_csv(output_file, index=False, encoding="utf-8-sig")
    else:
        df_lama = pd.read_csv(output_file)
        df_final = pd.concat([df_lama, df_baru], ignore_index=True)
        df_final.to_csv(output_file, index=False, encoding="utf-8-sig")

    st.success("Hasil berhasil disimpan ke CSV!")

