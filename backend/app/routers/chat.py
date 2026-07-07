from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.services.knowledge_base import KnowledgeBase
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])
kb = KnowledgeBase()
chat_service = ChatService(kb)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.question.strip():
        raise HTTPException(400, "Question cannot be empty")
    
    result = chat_service.ask(request.question)
    return ChatResponse(**result)

@router.post("/reset")
async def reset_chat():
    chat_service.reset_memory()
    return {"message": "Chat history reset."}