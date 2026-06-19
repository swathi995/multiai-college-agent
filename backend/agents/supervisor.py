from backend.agents.admin_agent import admin_agent
from backend.agents.student_agent import student_agent

def route_query(query: str, user_type: str):

    if user_type == "admin":
        return admin_agent(query)

    if user_type == "student":
        return student_agent(query)

    return "Invalid user type"