from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import shutil
import os
from app.config import get_settings
from app.services.document_loader import DocumentLoader
from app.services.knowledge_base import KnowledgeBase

router = APIRouter(prefix="/upload", tags=["Knowledge Base"])
settings = get_settings()
loader = DocumentLoader()
kb = KnowledgeBase()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    if ext not in loader.SUPPORTED:
        raise HTTPException(400, f"Unsupported: {ext}. Use PDF, DOCX, TXT.")
    
    os.makedirs(settings.upload_dir, exist_ok=True)
    file_path = os.path.join(settings.upload_dir, file.filename)
    
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    docs = loader.load(file_path)
    kb.add_documents(docs)
    
    return {"message": f"'{file.filename}' uploaded & indexed.", "chunks": len(docs)}

@router.delete("/")
async def clear_knowledge_base():
    kb.clear()
    return {"message": "Knowledge base cleared."}