import streamlit as st
import pandas as pd

# ========================
# Load dataset hasil Big Five
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
# 10 Pertanyaan Kuesioner
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
# OPSI – PERSIS PUNYAMU
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
    pilihan = st.radio(
        "",
        opsi[idx],
        index=None,
        key=f"q{idx}"
    )
    jawaban.append(pilihan)
    st.write("")

# ========================
# Tombol Proses
# ========================
if st.button("Proses Hasil"):

    # Validasi
    if "" in jawaban or None in jawaban:
        st.error("Masih ada pertanyaan yang belum dijawab.")
        st.stop()

    st.success("Hasil berhasil diproses!")

    # ========================
    # SKORING AKURAT
    # ========================
    skor_A = 0
    skor_B = 0
    skor_C = 0
    skor_D = 0
    skor_E = 0

    # Mapping setiap opsi ke tipe kepribadian
    mapping_opsi = {
        0: ["A", "B", "C", "D", "E"],
        1: ["A", "B", "C", "D", "E"],
        2: ["A", "B", "C", "D", "E"],
        3: ["A", "B", "C", "D", "E"],
        4: ["A", "B", "C", "D", "E"],
        5: ["A", "B", "C", "D", "E"],
        6: ["A", "B", "C", "D", "E"],
        7: ["A", "B", "C", "D", "E"],
        8: ["A", "B", "C", "D", "E"],
        9: ["A", "B", "C", "D", "E"]
    }

    # Hitung skor final
    for i in range(10):
        tipe = mapping_opsi[i][opsi[i].index(jawaban[i])]
        if tipe == "A": skor_A += 1
        if tipe == "B": skor_B += 1
        if tipe == "C": skor_C += 1
        if tipe == "D": skor_D += 1
        if tipe == "E": skor_E += 1

    # Tentukan tipe final
    skor_dict = {
        "A": skor_A,
        "B": skor_B,
        "C": skor_C,
        "D": skor_D,
        "E": skor_E
    }

    tipe_letter = max(skor_dict, key=skor_dict.get)

    data_tipe = df[df["Tipe_Letter"] == tipe_letter].iloc[0]

    # ========================
    # Tampilkan hasil akhir
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
    # Simpan hasil ke Excel otomatis
    # ========================

    import os

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

# Jika file belum ada → buat file baru
if not os.path.exists(output_file):
    df_baru.to_csv(output_file, index=False, encoding="utf-8-sig")

# Jika file sudah ada → append
else:
    df_lama = pd.read_csv(output_file)
    df_final = pd.concat([df_lama, df_baru], ignore_index=True)
    df_final.to_csv(output_file, index=False, encoding="utf-8-sig")

st.success("Hasil berhasil disimpan ke CSV!")

