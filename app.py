import streamlit as st

st.set_page_config(
    page_title="AI Learning Mentor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Learning Mentor")

st.markdown(
"""
### Welcome to AI Learning Mentor

Learn smarter using Agentic AI.
"""
)

st.divider()

st.subheader("Get Started")

col1, col2 = st.columns(2)

with col1:

    if st.button("🔐 Login", use_container_width=True):
        st.switch_page("pages/login.py")

with col2:

    if st.button("📝 Register", use_container_width=True):
        st.switch_page("pages/register.py")

st.divider()

st.info("🤖 AI Mentor")
st.success("📅 Study Planner")
st.warning("📊 Progress Tracker")
st.error("👨‍🏫 Teacher Dashboard")

st.caption("Built with Streamlit • LangGraph • Gemini • MySQL")