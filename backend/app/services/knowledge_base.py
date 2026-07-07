import os
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import get_settings

class KnowledgeBase:
    def __init__(self):
        self.settings = get_settings()
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.settings.embedding_model
        )
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        self.db = None
        self._init_db()
    
    def _init_db(self):
        persist = self.settings.chroma_persist_dir
        os.makedirs(persist, exist_ok=True)
        self.db = Chroma(
            persist_directory=persist,
            embedding_function=self.embeddings
        )
    
    def add_documents(self, docs: List[Document]):
        chunks = self.splitter.split_documents(docs)
        self.db.add_documents(chunks)
        self.db.persist()
    
    def search(self, query: str, k: int = 4) -> List[Document]:
        try:
            return self.db.similarity_search(query, k=k)
        except Exception:
            return []
    
    def clear(self):
        self.db.delete_collection()
        self._init_db()