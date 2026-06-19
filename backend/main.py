from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models.schemas import QueryRequest
from backend.agents.supervisor import route_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(request: QueryRequest):
    print("REQUEST RECEIVED:", request)  # 🔥 DEBUG LINE
    response = route_query(request.query, request.user_type)
    return {"response": response}