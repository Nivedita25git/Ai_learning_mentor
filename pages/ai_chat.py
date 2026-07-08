import streamlit as st
from agents.workflow import run_workflow

st.set_page_config(page_title="AI Chat", page_icon="🤖")

st.title("🤖 AI Learning Mentor")

question = st.text_input("Ask a question")

if st.button("Ask"):

    st.write("Question received ✅")

    try:
        st.write("Calling workflow...")

        answer = run_workflow(question)

        st.success("Workflow completed!")

        st.write(answer)

    except Exception as e:
        st.error(str(e))