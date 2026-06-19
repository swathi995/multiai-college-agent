from backend.utils import call_llm

def admin_agent(query: str):
    return call_llm(
        system_prompt="You are a college admin assistant. Generate reports and insights.",
        query=query
    )