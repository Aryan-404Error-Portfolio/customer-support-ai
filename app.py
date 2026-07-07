import sys
import os
sys.path.insert(0, './backend')

import streamlit as st
from app.services.document_loader import DocumentLoader
from app.services.knowledge_base import KnowledgeBase
from app.services.chat_service import ChatService

st.set_page_config(page_title="Customer Support AI", page_icon="🤖")

if 'kb' not in st.session_state:
    st.session_state.kb = KnowledgeBase()
if 'chat' not in st.session_state:
    st.session_state.chat = ChatService(st.session_state.kb)
if 'loader' not in st.session_state:
    st.session_state.loader = DocumentLoader()

st.title("🤖 Customer Support AI Assistant")
st.markdown("Upload company documents (PDF, DOCX, TXT) and ask questions.")

tab1, tab2 = st.tabs(["💬 Chat", "📁 Upload Documents"])

with tab1:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    if st.button("Reset Chat"):
        st.session_state.chat.reset_memory()
        st.session_state.messages = []
        st.rerun()

with tab2:
    uploaded_file = st.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"])
    
    if uploaded_file:
        if st.button("Upload & Index"):
            with st.spinner("Processing..."):
                try:
                    file_path = os.path.join("/tmp", uploaded_file.name)
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getvalue())
                    docs = st.session_state.loader.load(file_path)
                    st.session_state.kb.add_documents(docs)
                    st.success(f"✅ '{uploaded_file.name}' uploaded & indexed. ({len(docs)} pages)")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    
    if st.button("Clear Knowledge Base"):
        st.session_state.kb.clear()
        st.success("Knowledge base cleared.")

# Chat input MUST be at the root level, not inside tabs
if prompt := st.chat_input("Ask about company policies, FAQs..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                result = st.session_state.chat.ask(prompt)
                answer = result["answer"]
                sources = result.get("sources", [])
                if sources:
                    answer += "\n\n**Sources:**\n" + "\n".join([f"- {s}" for s in sources])
            except Exception as e:
                answer = f"Error: {str(e)}"
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})