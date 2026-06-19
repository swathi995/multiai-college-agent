from backend.utils import call_llm

def student_agent(query: str):
    return call_llm(
        system_prompt="You are a helpful student assistant.",
        query=query
    )