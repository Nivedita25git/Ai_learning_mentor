import streamlit as st
from database.user_db import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

st.title("🔐 Student Login")

email = st.text_input("Email")

password = st.text_input("Password", type="password")

if st.button("Login"):

    if not email or not password:

        st.warning("Please enter Email and Password.")

    else:

        success, student = login_user(email, password)

        if success:

            st.session_state["logged_in"] = True
            st.session_state["student"] = student

            st.success(f"Welcome {student['full_name']} 🎉")

            st.switch_page("pages/dashboard.py")

        else:

            st.error("Invalid Email or Password")

st.divider()

if st.button("📝 New User? Register"):

    st.switch_page("pages/register.py")

if st.button("⬅ Back to Home"):

    st.switch_page("app.py")