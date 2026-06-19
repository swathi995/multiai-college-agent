from backend.utils import call_llm

def analytics_agent(query: str):
    return call_llm(
        system_prompt="You are an AI data analyst for student performance.",
        query=query
    )