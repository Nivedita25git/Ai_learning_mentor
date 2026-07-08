import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.router_prompt import router_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

chain = router_prompt | llm


def route_question(question: str):

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content.strip().lower()