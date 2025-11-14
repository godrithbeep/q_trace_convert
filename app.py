import streamlit as st
import base64

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Order Management System", layout="centered")

# ---- BACKGROUND GIF ----
# Replace the GIF link with yours
gif_url = "https://lh3.googleusercontent.com/proxy/kjrf6Y_jVTpZA9bxVsLDwzRgXUx0MxKAD_ka-yRsIGCHTFjGsFyC4jK_rf4JzDyKJ-O0vny_-yQoSz5FqWFMomOWu0fWj2lnyurug8dq2L8"

page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("{gif_url}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    opacity: 0.92;   /* Lower this to dim more */
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

.main-glass {{
    background: rgba(255, 255, 255, 0.65);
    padding: 3rem;
    border-radius: 25px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 40px rgba(0, 128, 0, 0.25);
    max-width: 750px;
    margin: auto;
    border: 1px solid rgba(255,255,255,0.35);
}}

h1, h2, h3, label {{
    color: #0d5e33 !important;  /* Professional green */
}}

.stButton>button {{
    background-color: #1d8f4a !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.2rem;
    border: none;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---- HEADER ----
st.markdown(
    "<h2 style='text-align:center; font-weight:600;'>Authorized by Ngo Danh Thai ®<br> Sales Operation Data Executive at MPS</h2>",
    unsafe_allow_html=True
)

# ---- MAIN CONTENT BOX ----
with st.container():
    st.markdown("<div class='main-glass'>", unsafe_allow_html=True)

    st.markdown("## 🌿 Order Management Dashboard")
    st.write("Welcome to your professionally designed green-themed management system.")

    st.text_input("Order ID")
    st.text_input("Customer Name")
    st.number_input("Quantity", min_value=1)
    st.selectbox("Status", ["Pending", "Processing", "Delivered"])

    st.button("Submit Order")

    st.markdown("</div>", unsafe_allow_html=True)
