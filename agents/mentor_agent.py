import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.mentor_prompt import mentor_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3
)

chain = mentor_prompt | llm


def ask_mentor(question: str):

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content