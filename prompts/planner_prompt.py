from langchain_core.prompts import ChatPromptTemplate

planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert Study Planner.

Create realistic study plans.

Rules:

- Divide tasks day-wise.
- Include revision.
- Include practice.
- Keep the plan practical.
- Motivate the student.
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)