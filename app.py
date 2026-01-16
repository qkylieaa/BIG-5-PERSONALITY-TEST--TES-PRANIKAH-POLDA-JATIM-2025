import streamlit as st
import pandas as pd
import os
import datetime as dt

st.set_page_config(page_title="SiPreMarry.id", layout="centered")

# ========================
# PATH FILE EXCEL (AUTO SESUAI OS)
# - Windows (run di laptop): simpan ke path kamu
# - Linux/Cloud: simpan di folder project biar tidak error
# ========================
if os.name == "nt":
    EXCEL_FILENAME = r"C:\Users\APRILIA R.P\Downloads\Draft Sipremarry\data user SiPreMarry.xlsx"
else:
    EXCEL_FILENAME = os.path.join(os.getcwd(), "data user SiPreMarry.xlsx")

COLUMNS = [
    "Timestamp", "Nama", "Umur",
    "Top1", "Hasil_Prediksi",
    "O_count", "C_count", "E_count", "A_count", "N_count",
    "Narasi",
] + [f"Q{i}" for i in range(1, 21)]

def bullet(lines):
    return "\n".join([f"- {x}" for x in lines])

def save_to_excel_append(row, filename=EXCEL_FILENAME):
    """Append 1 row ke 1 file Excel yang sama. Jika belum ada, buat baru + header."""
    # FIX utama: kalau dirname kosong -> pakai "."
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)

    df_new = pd.DataFrame([row], columns=COLUMNS)

    # jika file belum ada: buat baru (header otomatis)
    if not os.path.exists(filename):
        df_new.to_excel(filename, index=False)
        return

    # jika file sudah ada: append baris (tanpa header)
    with pd.ExcelWriter(filename, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        sheet = list(writer.sheets.keys())[0]  # sheet pertama
        startrow = writer.sheets[sheet].max_row
        df_new.to_excel(writer, sheet_name=sheet, index=False, header=False, startrow=startrow)

# ========================
# Title & Header
# ========================
st.title("💍 SiPreMarry.id Test")
st.write("Pengenalan diri adalah langkah awal membangun pernikahan yang sehat. Jawab pertanyaan berikut untuk memahami kecenderungan kepribadian Anda.")
st.write("---")

# ========================
# Form Input Identitas
# ========================
nama = st.text_input("Nama")
umur = st.number_input("Umur", min_value=17, max_value=80, step=1)

st.write("---")

# ========================
# Pertanyaan (Q1–Q20)
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

# ========================
# Opsi (Q1–Q20) - TEKS LENGKAP
# ========================
opsi = [
    [
        "Merasa hidup saya baik-baik saja tanpa perlu membandingkan diri",
        "Penasaran bagaimana jalan hidup mereka bisa berbeda dari saya",
        "Terganggu dan jadi mempertanyakan kemampuan diri sendiri",
        "Termotivasi untuk memperbaiki cara saya bekerja",
        "Tidak terlalu tertarik memikirkan perjalanan hidup orang lain",
    ],
    [
        "Menarik diri karena emosi saya mudah naik turun",
        "Mencoba kembali ke rutinitas agar pikiran lebih stabil",
        "Mencari sudut pandang baru dari apa yang sedang saya alami",
        "Berusaha tetap tenang agar tidak mempengaruhi orang lain",
        "Mengabaikan perasaan itu dan berharap cepat berlalu",
    ],
    [
        "Tenang karena percaya semuanya akan berjalan dengan sendirinya",
        "Antusias membayangkan banyak kemungkinan yang bisa terjadi",
        "Cemas karena takut tidak bisa mengendalikan keadaan",
        "Bersemangat menjalaninya bersama orang-orang terdekat",
        "Perlu rencana jelas agar hidup terasa aman",
    ],
    [
        "Langsung merasa ada yang salah dengan hubungan kami",
        "Menganggap setiap orang punya kesibukan masing-masing",
        "Mengirim pesan lanjutan agar komunikasi tetap berjalan",
        "Tidak terlalu memikirkannya dan fokus ke hal lain",
        "Mencatatnya sebagai hal yang perlu diperhatikan ke depan",
    ],
    [
        "Sulit berhenti memikirkan kesalahan yang terjadi",
        "Menganggap kegagalan sebagai pengalaman biasa dalam hidup",
        "Mengevaluasi langkah saya untuk perbaikan selanjutnya",
        "Mencari kemungkinan arah baru yang belum terpikirkan",
        "Lebih memilih menerima keadaan tanpa banyak menganalisis",
    ],
    [
        "Mengikuti perasaan saya saat itu tanpa banyak pertimbangan",
        "Mempertimbangkan dampaknya terhadap orang-orang terdekat",
        "Merasa ragu dan takut menyesal setelahnya",
        "Berdiskusi agar mendapatkan banyak sudut pandang",
        "Menggunakan nilai dan prinsip pribadi sebagai acuan",
    ],
    [
        "Merasa tidak nyaman dan butuh waktu lama untuk menyesuaikan diri",
        "Mudah memulai percakapan dengan orang baru",
        "Lebih memilih mengamati dulu sebelum terlibat",
        "Berusaha mengikuti aturan agar tidak membuat kesalahan",
        "Tertarik mencoba hal-hal yang belum pernah saya alami",
    ],
    [
        "Menghindari pembicaraan karena takut suasana memburuk",
        "Mengalah meski sebenarnya tidak sepenuhnya setuju",
        "Mencoba melihat perbedaan itu sebagai bahan pembelajaran",
        "Menjaga agar komunikasi tetap terbuka",
        "Mencari solusi yang paling masuk akal bagi kedua pihak",
    ],
    [
        "Tempat yang stabil dengan aturan yang jelas",
        "Ruang yang terus berkembang dan terbuka terhadap perubahan",
        "Lingkungan yang minim konflik meski harus menekan perasaan",
        "Tempat yang hangat dan penuh interaksi",
        "Rumah yang tenang agar emosi tetap terkendali",
    ],
    [
        "Menyampaikan perasaan secara spontan",
        "Memikirkan kata-kata dengan hati-hati sebelum berbicara",
        "Menarik diri saat emosi sedang tidak stabil",
        "Mendengarkan terlebih dahulu sebelum menanggapi",
        "Tidak terlalu tertarik membahas topik yang mendalam",
    ],
    [
        "Merasa panik dan sulit menenangkan diri",
        "Mencoba menyesuaikan diri tanpa banyak mengeluh",
        "Menganggap perubahan sebagai hal yang merepotkan",
        "Menyusun ulang rencana agar tetap terkendali",
        "Melihatnya sebagai kesempatan mencoba hal baru",
    ],
    [
        "Hubungan berjalan apa adanya tanpa banyak aturan",
        "Ada keterbukaan untuk tumbuh bersama",
        "Suasana tetap ramai dan penuh interaksi",
        "Konflik bisa dihindari sebisa mungkin",
        "Emosi saya jarang terganggu oleh hal kecil",
    ],
    [
        "Merasa lelah secara emosional",
        "Mencari cara baru yang belum pernah dicoba",
        "Tetap mengikuti cara lama karena sudah terbiasa",
        "Mengevaluasi pola kesalahan secara sistematis",
        "Membicarakannya agar tidak menumpuk",
    ],
    [
        "Langsung merasa tersinggung",
        "Mendengarkan dengan tenang walau tidak langsung setuju",
        "Membela diri agar posisi saya dipahami",
        "Mencoba memahami maksud di balik kritik tersebut",
        "Menjadikannya bahan evaluasi diri",
    ],
    [
        "Mudah khawatir terhadap hal yang belum terjadi",
        "Cukup fleksibel menghadapi perubahan",
        "Kurang konsisten menjalankan rencana",
        "Mudah berinteraksi dengan berbagai tipe orang",
        "Berusaha menjaga perasaan orang lain",
    ],
    [
        "Memilih yang sudah pasti dan aman",
        "Tertarik mencoba hal baru meski berisiko",
        "Mempertimbangkan dampaknya secara matang",
        "Mengikuti pilihan yang disukai orang sekitar",
        "Merasa cemas dengan pilihan apapun",
    ],
    [
        "Stabilitas lebih penting daripada perubahan",
        "Perencanaan yang jelas membuat hubungan lebih aman",
        "Keintiman emosional perlu sering diekspresikan",
        "Mengalah adalah cara terbaik menjaga keharmonisan",
        "Emosi yang naik turun adalah hal yang wajar bagi saya",
    ],
    [
        "Menyalahkan diri sendiri",
        "Mengajak pasangan berbicara secara terbuka",
        "Mencari cara baru agar situasi membaik",
        "Menunggu keadaan membaik dengan sendirinya",
        "Menjaga sikap agar tidak memperkeruh suasana",
    ],
    [
        "Harus menghadapi perubahan mendadak",
        "Hubungan terasa terlalu kaku",
        "Situasi terasa tidak terkontrol",
        "Tanggung jawab tidak dijalankan dengan baik",
        "Ada konflik terbuka antar orang terdekat",
    ],
    [
        "Membuat perencanaan detail",
        "Mengikuti arus dan melihat nanti",
        "Merasa khawatir apakah saya mampu menjalaninya",
        "Membayangkan berbagai kemungkinan yang bisa terjadi",
        "Mengandalkan dukungan orang sekitar",
    ],
]

# ========================
# KEYS
# ========================
KEYS = [
    {opsi[0][0]:"A", opsi[0][1]:"O", opsi[0][2]:"N", opsi[0][3]:"C", opsi[0][4]:"O"},
    {opsi[1][0]:"N", opsi[1][1]:"C", opsi[1][2]:"O", opsi[1][3]:"A", opsi[1][4]:"N"},
    {opsi[2][0]:"C", opsi[2][1]:"O", opsi[2][2]:"N", opsi[2][3]:"E", opsi[2][4]:"C"},
    {opsi[3][0]:"N", opsi[3][1]:"A", opsi[3][2]:"E", opsi[3][3]:"N", opsi[3][4]:"C"},
    {opsi[4][0]:"N", opsi[4][1]:"N", opsi[4][2]:"C", opsi[4][3]:"O", opsi[4][4]:"C"},
    {opsi[5][0]:"C", opsi[5][1]:"A", opsi[5][2]:"N", opsi[5][3]:"E", opsi[5][4]:"O"},
    {opsi[6][0]:"N", opsi[6][1]:"E", opsi[6][2]:"E", opsi[6][3]:"C", opsi[6][4]:"O"},
    {opsi[7][0]:"N", opsi[7][1]:"A", opsi[7][2]:"O", opsi[7][3]:"E", opsi[7][4]:"C"},
    {opsi[8][0]:"C", opsi[8][1]:"O", opsi[8][2]:"A", opsi[8][3]:"E", opsi[8][4]:"N"},
    {opsi[9][0]:"E", opsi[9][1]:"C", opsi[9][2]:"N", opsi[9][3]:"A", opsi[9][4]:"O"},
    {opsi[10][0]:"N", opsi[10][1]:"A", opsi[10][2]:"O", opsi[10][3]:"C", opsi[10][4]:"O"},
    {opsi[11][0]:"C", opsi[11][1]:"O", opsi[11][2]:"E", opsi[11][3]:"A", opsi[11][4]:"N"},
    {opsi[12][0]:"N", opsi[12][1]:"O", opsi[12][2]:"O", opsi[12][3]:"C", opsi[12][4]:"E"},
    {opsi[13][0]:"N", opsi[13][1]:"A", opsi[13][2]:"E", opsi[13][3]:"O", opsi[13][4]:"C"},
    {opsi[14][0]:"N", opsi[14][1]:"O", opsi[14][2]:"C", opsi[14][3]:"E", opsi[14][4]:"A"},
    {opsi[15][0]:"O", opsi[15][1]:"O", opsi[15][2]:"C", opsi[15][3]:"A", opsi[15][4]:"N"},
    {opsi[16][0]:"O", opsi[16][1]:"C", opsi[16][2]:"E", opsi[16][3]:"A", opsi[16][4]:"N"},
    {opsi[17][0]:"N", opsi[17][1]:"E", opsi[17][2]:"O", opsi[17][3]:"C", opsi[17][4]:"A"},
    {opsi[18][0]:"O", opsi[18][1]:"E", opsi[18][2]:"N", opsi[18][3]:"C", opsi[18][4]:"A"},
    {opsi[19][0]:"C", opsi[19][1]:"C", opsi[19][2]:"N", opsi[19][3]:"O", opsi[19][4]:"E"},
]

# ========================
# NARASI
# ========================
NARASI = {
    "O": {
        "nama": "Keterbukaan terhadap Pengalaman (Openness)",
        "kecenderungan": "Anda cenderung terbuka terhadap hal-hal baru, ide yang beragam, dan pengalaman yang memberi makna. Anda relatif fleksibel dan mudah beradaptasi dengan perubahan.",
        "kelebihan": [
            "Memiliki kreativitas dan ide-ide baru yang segar",
            "Lebih mudah menerima perubahan dan hal unik",
            "Mampu melihat situasi dari berbagai sudut pandang",
            "Terbuka untuk belajar dan memperluas wawasan",
            "Fleksibel terhadap berbagai tipe orang dan lingkungan",
        ],
        "kekurangan": [
            "Rutinitas yang sangat sama bisa terasa kurang menarik",
            "Banyaknya ide kadang membuat fokus mudah berpindah",
            "Minat yang berubah-ubah bisa terlihat kurang konsisten",
        ],
        "saran_pasangan": [
            "Bangun komunikasi tentang hal-hal baru yang ingin dicoba bersama",
            "Susun rencana yang jelas namun tetap memberi ruang eksplorasi",
        ],
        "komunikasi": [
            "Gunakan kalimat: 'Aku ingin kita mencoba hal baru, tapi tetap aman untuk kita berdua.'",
            "Diskusikan perubahan sebagai rencana bersama, bukan keputusan sepihak.",
        ],
    },
    "C": {
        "nama": "Keteraturan dan Tanggung Jawab (Conscientiousness)",
        "kecenderungan": "Anda cenderung terstruktur, disiplin, dan merasa tenang ketika tanggung jawab serta rencana berjalan dengan jelas.",
        "kelebihan": [
            "Terorganisir dan dapat diandalkan",
            "Konsisten memenuhi tanggung jawab dan komitmen",
            "Mampu merencanakan langkah dengan cermat",
        ],
        "kekurangan": [
            "Standar tinggi kadang terlihat seperti perfeksionisme",
            "Kurang nyaman dengan perubahan mendadak",
        ],
        "saran_pasangan": [
            "Susun pembagian tugas rumah tangga yang realistis dan disepakati",
            "Hargai perbedaan gaya kerja antara yang terstruktur dan spontan",
        ],
        "komunikasi": [
            "Gunakan kalimat: 'Agar aku tenang, aku butuh kejelasan soal…'",
            "Fokus pada solusi kecil yang bisa dilakukan bersama.",
        ],
    },
    "E": {
        "nama": "Ekspresivitas dan Interaksi Sosial (Extraversion)",
        "kecenderungan": "Anda cenderung nyaman berinteraksi, mudah mengekspresikan perasaan, dan terbantu ketika komunikasi berlangsung terbuka.",
        "kelebihan": [
            "Komunikatif dan mudah membangun kedekatan",
            "Membawa energi positif dalam hubungan",
        ],
        "kekurangan": [
            "Bisa terasa terlalu intens saat pasangan butuh waktu",
            "Mudah kecewa jika komunikasi minim",
        ],
        "saran_pasangan": [
            "Sediakan waktu ngobrol rutin agar kebutuhan komunikasi terpenuhi",
            "Berikan respons singkat saat sibuk agar tetap terasa aman",
        ],
        "komunikasi": [
            "Gunakan kalimat: 'Aku ingin ngobrol supaya kita lebih dekat, bukan untuk berdebat.'",
            "Tanya kesiapan pasangan: 'Kamu siap ngobrol sekarang atau butuh waktu dulu?'",
        ],
    },
    "A": {
        "nama": "Kehangatan dan Kerja Sama (Agreeableness)",
        "kecenderungan": "Anda cenderung hangat, empatik, dan berusaha menjaga keharmonisan dalam hubungan.",
        "kelebihan": [
            "Empati tinggi dan suportif",
            "Mudah bekerja sama dan menjaga suasana",
        ],
        "kekurangan": [
            "Bisa terlalu mengalah hingga kebutuhan diri tidak tersampaikan",
            "Menghindari konflik bisa membuat masalah menumpuk",
        ],
        "saran_pasangan": [
            "Ajak berdiskusi dengan lembut dan beri ruang untuk menyampaikan kebutuhan",
            "Buat aturan konflik sehat agar tetap aman",
        ],
        "komunikasi": [
            "Gunakan kalimat: 'Aku ingin kita tetap rukun, tapi ini penting bagiku…'",
            "Latih berkata jujur tanpa merasa bersalah.",
        ],
    },
    "N": {
        "nama": "Sensitivitas Emosional (Neuroticism)",
        "kecenderungan": "Anda cenderung peka terhadap stres dan perubahan emosi, serta membutuhkan rasa aman dan kepastian dalam hubungan.",
        "kelebihan": [
            "Peka terhadap masalah sebelum membesar",
            "Berhati-hati dan reflektif terhadap perasaan",
        ],
        "kekurangan": [
            "Mudah overthinking saat situasi tidak jelas",
            "Emosi bisa terasa intens saat tertekan",
        ],
        "saran_pasangan": [
            "Berikan kepastian kecil yang konsisten (misalnya kabar singkat saat sibuk)",
            "Validasi emosi dulu sebelum mencari solusi",
        ],
        "komunikasi": [
            "Gunakan kalimat: 'Aku lagi kepikiran, boleh minta kepastian sedikit?'",
            "Sepakati waktu ngobrol saat emosi sudah lebih stabil.",
        ],
    },
}

# ========================
# TAMPILAN SOAL (LOOP)
# ========================
jawaban = []
for idx, q in enumerate(pertanyaan):
    st.write(f"### {idx+1}. {q}")
    pilihan = st.radio("", opsi[idx], index=None, key=f"q{idx}")
    jawaban.append(pilihan)
    st.write("")

st.write("---")

# ========================
# TOMBOL PROSES (AUTO SAVE, TANPA DOWNLOAD)
# ========================
if st.button("🔍 Lihat Hasil"):
    if not nama:
        st.error("Nama wajib diisi.")
        st.stop()

    if None in jawaban:
        st.error("Masih ada pertanyaan yang belum dijawab.")
        st.stop()

    trait_list = [KEYS[i][jawaban[i]] for i in range(20)]
    traits = ["O", "C", "E", "A", "N"]
    counts = {t: trait_list.count(t) for t in traits}

    top1 = max(counts, key=counts.get)
    hasil_prediksi = NARASI[top1]["nama"]

    n = NARASI[top1]
    narasi = f"""
## 📌 Kecenderungan Kepribadian
Berdasarkan pilihan Anda, kecenderungan kepribadian Anda adalah **{n['nama']}**.

{n['kecenderungan']}

## ⭐ Kelebihan
{bullet(n['kelebihan'])}

## ⚠ Tantangan (bukan label negatif)
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

    timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    row = [
        timestamp,
        nama,
        int(umur),
        top1,
        hasil_prediksi,
        counts["O"],
        counts["C"],
        counts["E"],
        counts["A"],
        counts["N"],
        narasi,
    ] + jawaban

    # anti double-save: pakai timestamp juga biar payload unik
    payload = (timestamp, nama, int(umur), top1, tuple(jawaban))
    if st.session_state.get("last_saved") != payload:
        try:
            save_to_excel_append(row)
            st.session_state["last_saved"] = payload
            st.info("📊 Jawaban kamu tersimpan otomatis.")
            st.caption(f"Lokasi file: {EXCEL_FILENAME}")
        except Exception as e:
            st.error("❌ Gagal menyimpan jawaban.")
            st.exception(e)
