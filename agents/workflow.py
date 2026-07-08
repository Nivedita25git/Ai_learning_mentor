from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.router_agent import route_question
from agents.mentor_agent import ask_mentor
from agents.planner_agent import create_plan


# ---------------- State ----------------

class AgentState(TypedDict):
    question: str
    agent: str
    answer: str


# ---------------- Router Node ----------------

def router_node(state: AgentState):

    agent = route_question(state["question"])

    state["agent"] = agent

    return state


# ---------------- Mentor Node ----------------

def mentor_node(state: AgentState):

    state["answer"] = ask_mentor(state["question"])

    return state


# ---------------- Planner Node ----------------

def planner_node(state: AgentState):

    state["answer"] = create_plan(state["question"])

    return state


# ---------------- Conditional Routing ----------------

def decide_agent(state: AgentState):

    if state["agent"] == "planner":
        return "planner"

    return "mentor"


# ---------------- Build Graph ----------------

builder = StateGraph(AgentState)

builder.add_node("router", router_node)
builder.add_node("mentor", mentor_node)
builder.add_node("planner", planner_node)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    decide_agent,
    {
        "mentor": "mentor",
        "planner": "planner"
    }
)

builder.add_edge("mentor", END)
builder.add_edge("planner", END)

graph = builder.compile()


# ---------------- Function ----------------

def run_workflow(question):

    result = graph.invoke(
        {
            "question": question,
            "agent": "",
            "answer": ""
        }
    )

    return result["answer"]