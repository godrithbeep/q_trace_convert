import streamlit as st
from convert_sap_to_template import convert_sap_to_template

# ===== CUSTOM CSS =====
def local_css():
    css = """
    <style>
        /* Title */
        .title {
            font-size: 30px !important;
            font-weight: 800 !important;
            color: #34E09F;  /* main green color */
            padding-bottom: 5px;
        }
        /* Subtitle / Authorized */
        .authorized {
            font-size: 14px !important;
            color: #2e7d5e;  /* darker green */
            margin-bottom: 25px;
            font-style: italic;
        }
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 12px;
            color: #34E09F;
        }
        /* Buttons */
        .stButton>button {
            background-color: #34E09F;
            color: white;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #2bb78a;  /* darker green on hover */
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply custom CSS
local_css()

# ========= TITLE & HEADER ==========
st.markdown('<div class="title">SAP to Standard Template Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="authorized">Authorized by Ngo Danh Thai ® — Sales Operation Data Executive, MPS</div>', unsafe_allow_html=True)

# ========= MAIN LAYOUT ==========
col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("📤 Upload SAP File")
    uploaded_file = st.file_uploader("Choose SAP File", type=["xlsx"])
    convert_btn = st.button("🚀 Convert File", use_container_width=True)

with col2:
    st.subheader("📥 Output File")
    if convert_btn:
        if uploaded_file:
            with st.spinner("Processing file…"):
                try:
                    buffer, filename = convert_sap_to_template(uploaded_file)
                    st.success("✔ Conversion completed!")
                    st.download_button(
                        label="⬇ Download Converted File",
                        data=buffer,
                        file_name=filename,
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
                except Exception as e:
                    st.error(f"❌ Error: {e}")
        else:
            st.warning("⚠ Please upload a file first.")

# ========= FOOTER ==========
st.markdown(
    '<div class="footer">© 2025 MPS Operations Data System — All rights reserved.</div>',
    unsafe_allow_html=True
)
