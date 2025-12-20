from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import AgentOrchestrator

app = FastAPI(title="CredResolve Agent API")

orchestrator = AgentOrchestrator()

class ChatRequest(BaseModel):
    user_id: str
    session_id: str
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(req: ChatRequest):
    return await orchestrator.handle_turn(
        user_id=req.user_id,
        session_id=req.session_id,
        text=req.text
    )

