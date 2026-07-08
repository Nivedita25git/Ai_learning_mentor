import time
import streamlit as st
from database.user_db import register_user

st.set_page_config(
    page_title="Register",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Student Registration")

with st.form("register_form"):

    full_name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input("Password", type="password")

    course = st.text_input("Course")

    year = st.selectbox(
        "Year",
        [1, 2, 3, 4]
    )

    submitted = st.form_submit_button("Register")

if submitted:

    full_name = full_name.strip()
    email = email.strip()
    password = password.strip()
    course = course.strip()

    if full_name == "":
        st.error("Please enter your Full Name.")

    elif email == "":
        st.error("Please enter your Email.")

    elif password == "":
        st.error("Please enter your Password.")

    elif course == "":
        st.error("Please enter your Course.")

    else:

        success, message = register_user(
            full_name,
            email,
            password,
            course,
            year
        )

        if success:

            st.success("✅ Registration Successful!")

            st.info("Redirecting to Login Page...")

            time.sleep(2)

            st.switch_page("pages/login.py")

        else:

            st.error(message)

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

with col2:
    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/login.py")