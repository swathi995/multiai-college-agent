from backend.utils import call_llm

def scheduler_agent(query: str):
    return call_llm(
        system_prompt="You manage timetables and scheduling for college system.",
        query=query
    )