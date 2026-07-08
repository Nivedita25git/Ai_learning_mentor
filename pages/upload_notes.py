import streamlit as st
import os

st.set_page_config(
    page_title="Upload Notes",
    page_icon="📄"
)

# Check Login
if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")
    st.stop()

st.title("📄 Upload Study Notes")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("rag/documents", exist_ok=True)

    file_path = os.path.join(
        "rag/documents",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ PDF uploaded successfully!")

    st.write(f"Saved File: **{uploaded_file.name}**")