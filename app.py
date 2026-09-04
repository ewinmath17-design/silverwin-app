import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="Silverwin Kendari - Cokelat Artisan Premium",
    page_icon="🍫",
    layout="centered"
)

# Custom Styling CSS sederhana agar tampilannya selaras
st.markdown("""
    <style>
    .main {
        background-color: #fffbeb;
    }
    .stButton>button {
        width: 100%;
        background-color: #059669;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem;
    }
    .stButton>button:hover {
        background-color: #047857;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER & HERO SECTION
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.markdown("### 🍫 100% Asli Kendari & Halal")
st.title("Cokelat Artisan Asli Kendari, Dijamin Aman!")
st.markdown("</div>", unsafe_allow_html=True)

# 3 Bullet Points Keuntungan
st.info("""
- **✓** 100% diolah di Kendari dari biji kakao Sulawesi terbaik dengan tekstur ultra-halus.  
- **✓** Pengiriman luar kota dijamin aman menggunakan kemasan insulasi khusus anti-leleh.  
- **✓** Tersedia varian eksklusif (Mete, Almond, Dark Chocolate) serta paket grosir untuk oleh-oleh.
""")

st.write("---")
st.subheader("🛒 Pilih Varian Favorit Anda")

# Data Produk & Tombol WhatsApp
products = [
    {
        "id": "SLV-01",
        "name": "Silverwin Cashew (Mete)",
        "price": "Rp35.000",
        "desc": "Cokelat artisan premium khas Kendari berpadu gurihnya kacang mete pilihan asli Sulawesi.",
        "wa": "https://wa.me/6281278904321?text=Halo%20Kak,%20saya%20mau%20pesan%20Silverwin%20Cashew%20(Mete).%20Mohon%20info%20ketersediaan%20stok%20dan%20cara%20pengirimannya%20ya."
    },
    {
        "id": "SLV-02",
        "name": "Silverwin Almond",
        "price": "Rp38.000",
        "desc": "Sensasi kelezatan cokelat lembut berkualitas tinggi dengan taburan renyah kacang almond pilihan.",
        "wa": "https://wa.me/6281278904321?text=Halo%20Kak,%20saya%20tertarik%20dengan%20Silverwin%20Almond.%20Bagaimana%20cara%20pemesanan%20untuk%20pengiriman%20luar%20kota?"
    },
    {
        "id": "SLV-03",
        "name": "Silverwin Dark Chocolate",
        "price": "Rp35.000",
        "desc": "Cokelat hitam pekat kaya antioksidan dengan rasa autentik biji kakao pilihan Sulawesi.",
        "wa": "https://wa.me/6281278904321?text=Halo%20Kak,%20saya%20ingin%20pesan%20Silverwin%20Dark%20Chocolate.%20Apa%20saja%20paket%20grosir%20yang%20tersedia?"
    },
    {
        "id": "SLV-04",
        "name": "Paket Oleh-Oleh Eksklusif",
        "price": "Rp100.000",
        "desc": "Bundling spesial berisi 3 varian rasa terbaik Silverwin dengan kemasan insulasi aman luar kota.",
        "wa": "https://wa.me/6282293274916?text=Halo%20Kak,%20saya%20mau%20pesan%20Paket%20Oleh-Oleh%20Eksklusif%20Silverwin%20untuk%20kado.%20Mohon%20info%20detailnya."
    }
]

for p in products:
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{p['name']}** `ID: {p['id']}`")
            st.markdown(f"### {p['price']}")
            st.write(p['desc'])
        with col2:
            st.write("") # Spacer
            if st.link_button("Pesan WA ➔", p['wa']):
                pass
        st.write("---")

# Footer
st.markdown("<div style='text-align: center; color: gray; font-size: 12px;'>🔒 Pengiriman Aman: Dilengkapi insulasi khusus anti-leleh ke seluruh Indonesia.<br>© 2026 Silverwin Kendari.</div>", unsafe_allow_html=True)
