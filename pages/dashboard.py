import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.switch_page("pages/login.py")

student = st.session_state["student"]

st.title("🎓 AI Learning Mentor Dashboard")

st.success(f"Welcome, {student['full_name']} 👋")

st.write(f"**Course:** {student['course']}")
st.write(f"**Year:** {student['year']}")

st.divider()

col1, col2 = st.columns(2)

with col1:

    if st.button("🤖 AI Learning Mentor", use_container_width=True):
        st.switch_page("pages/ai_chat.py")

    if st.button("📅 Study Planner", use_container_width=True):
        st.switch_page("pages/ai_chat.py")

with col2:

    if st.button("📊 Progress ", use_container_width=True):
        st.info("Progress Tracker will be added soon.")

    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.clear()

        st.switch_page("pages/login.py")