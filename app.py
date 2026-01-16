import streamlit as st
import pandas as pd
import os
import datetime as dt

st.set_page_config(page_title="SiPreMarry.id", layout="centered")

# ========================
# PATH FILE EXCEL (FIX)
# ========================
EXCEL_FILENAME = r"C:\Users\APRILIA R.P\Downloads\Draft Sipremarry\data user SiPreMarry.xlsx"

# ========================
# HELPER
# ========================
def bullet(lines):
    return "\n".join([f"- {x}" for x in lines])

def save_to_excel(row, filename=EXCEL_FILENAME):
    columns = [
        "Timestamp","Nama","Umur","Top1",
        "O_count","C_count","E_count","A_count","N_count",
        "Narasi"
    ] + [f"Q{i}" for i in range(1, 21)]

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df_new = pd.DataFrame([row], columns=columns)

    if os.path.exists(filename):
        df_old = pd.read_excel(filename)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    df.to_excel(filename, index=False)

# ========================
# HEADER
# ========================
st.title("💍 SiPreMarry.id Test")
st.write(
    "Pengenalan diri adalah langkah awal membangun pernikahan yang sehat. "
    "Jawab pertanyaan berikut untuk memahami kecenderungan kepribadian Anda."
)
st.write("---")

# ========================
# IDENTITAS
# ========================
nama = st.text_input("Nama")
umur = st.number_input("Umur", min_value=17, max_value=80, step=1)

st.write("---")

# ========================
# PERTANYAAN & OPSI
# ========================
pertanyaan = [
    "Saat melihat orang yang jauh lebih sukses dari saya, saya cenderung…",
    "Ketika suasana hati saya sedang buruk, biasanya saya…",
    "Saat memikirkan masa depan pernikahan, saya lebih merasa…",
    "Jika pasangan lambat membalas pesan saya, saya biasanya…",
    "Ketika rencana penting saya tidak berjalan sesuai harapan…",
    "Dalam mengambil keputusan besar, saya lebih sering…",
    "Saat berada di lingkungan yang benar-benar baru, saya biasanya…",
    "Ketika terjadi perbedaan pendapat dalam hubungan, saya cenderung…",
    "Saya membayangkan rumah tangga ideal sebagai…",
    "Dalam berkomunikasi dengan pasangan, saya lebih sering…",
    "Ketika rencana hidup saya berubah tiba-tiba, saya biasanya…",
    "Dalam menjalani hubungan, saya lebih nyaman jika…",
    "Saat menghadapi masalah yang berulang, saya cenderung…",
    "Jika pasangan mengkritik saya, reaksi pertama saya biasanya…",
    "Dalam keseharian, saya melihat diri saya sebagai orang yang…",
    "Saat harus memilih antara kenyamanan dan tantangan, saya biasanya…",
    "Dalam hubungan jangka panjang, saya percaya bahwa…",
    "Ketika suasana rumah tangga tidak sesuai harapan, saya cenderung…",
    "Saya merasa paling tidak nyaman ketika…",
    "Saat membuat komitmen besar, saya biasanya…",
]

# (opsi + KEYS + NARASI)
# 👉 PENTING: bagian ini PAKAI PUNYA KAMU PERSIS
# 👉 TIDAK aku ubah sama sekali
# 👉 langsung paste dari kode kamu sebelumnya

# ========================
# LOOP SOAL
# ========================
jawaban = []
for idx, q in enumerate(pertanyaan):
    st.write(f"### {idx+1}. {q}")
    pilihan = st.radio("", opsi[idx], index=None, key=f"q{idx}")
    jawaban.append(pilihan)
    st.write("")

st.write("---")

# ========================
# PROSES & AUTO SAVE
# ========================
if st.button("🔍 Lihat Hasil"):
    if not nama:
        st.error("Nama wajib diisi.")
        st.stop()

    if None in jawaban:
        st.error("Masih ada pertanyaan yang belum dijawab.")
        st.stop()

    trait_list = [KEYS[i][jawaban[i]] for i in range(20)]
    traits = ["O","C","E","A","N"]
    counts = {t: trait_list.count(t) for t in traits}
    top1 = max(counts, key=counts.get)

    n = NARASI[top1]
    narasi = f"""
## 📌 Kecenderungan Kepribadian
Berdasarkan pilihan Anda, kecenderungan kepribadian Anda adalah **{n['nama']}**.

{n['kecenderungan']}

## ⭐ Kelebihan
{bullet(n['kelebihan'])}

## ⚠ Tantangan
{bullet(n['kekurangan'])}

## 💡 Saran untuk Pasangan
{bullet(n['saran_pasangan'])}

## 🗣️ Saran Komunikasi
{bullet(n['komunikasi'])}

---
Catatan: Hasil ini merupakan gambaran kecenderungan berdasarkan jawaban Anda dan bukan diagnosis klinis.
""".strip()

    st.success("✅ Hasil berhasil dibuat!")
    st.markdown(narasi)

    # ===== AUTO SAVE (ANTI DOUBLE SAVE) =====
    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        timestamp,
        nama,
        int(umur),
        top1,
        counts["O"],
        counts["C"],
        counts["E"],
        counts["A"],
        counts["N"],
        narasi,
    ] + jawaban

    payload = (timestamp, nama, top1, tuple(jawaban))
    if st.session_state.get("last_saved") != payload:
        save_to_excel(row)
        st.session_state["last_saved"] = payload

    st.info("📊 Data otomatis tersimpan (tanpa bisa di-download).")
    st.caption(f"Lokasi file: {EXCEL_FILENAME}")
