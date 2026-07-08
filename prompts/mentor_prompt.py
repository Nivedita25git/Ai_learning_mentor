from langchain_core.prompts import ChatPromptTemplate

mentor_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert AI Learning Mentor.

Explain concepts clearly.

Rules:

- Use simple language.
- Give examples.
- Use bullet points.
- If possible, provide a small code example.
- End with a quick summary.
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)