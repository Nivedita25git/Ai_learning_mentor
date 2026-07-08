import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.planner_prompt import planner_prompt

# Load .env file
load_dotenv()

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

# Create LangChain chain
chain = planner_prompt | llm


def create_plan(question: str):
    """
    Generates a study plan using Gemini.
    """

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content