from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from app.config import get_settings
from app.services.knowledge_base import KnowledgeBase

class ChatService:
    def __init__(self, kb: KnowledgeBase):
        self.settings = get_settings()
        self.kb = kb
        
        self.llm = HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            temperature=0.3,
            max_new_tokens=512
        )
        
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.kb.db.as_retriever(search_kwargs={"k": 4}),
            memory=self.memory,
            return_source_documents=True
        )
    
    def ask(self, question: str) -> dict:
        try:
            result = self.chain.invoke({"question": question})
        except Exception:
            return {
                "answer": "I don't have any documents to reference. Please upload company documents first, then ask your question.",
                "sources": []
            }
        
        answer = result["answer"]
        sources = [doc.metadata.get("source", "") for doc in result.get("source_documents", [])]
        
        source_docs = result.get("source_documents", [])
        if not source_docs or all(len(d.page_content.strip()) < 20 for d in source_docs):
            answer = "I don't have enough information to answer that. Please contact support."
        
        return {
            "answer": answer,
            "sources": list(set(s for s in sources if s))
        }