# 🤖 Customer Support AI Assistant

An AI-powered customer support chatbot that answers questions based on uploaded company documents (PDF, DOCX, TXT). Built with Streamlit, LangChain, ChromaDB, and Hugging Face models.

---

## 📋 Project Deliverables

| Deliverable | Status | File |
|-------------|--------|------|
| Streamlit Frontend | ✅ Complete | `app.py` |
| Document Upload & Indexing | ✅ Complete | `backend/app/routers/upload.py` |
| AI Chat with Memory | ✅ Complete | `backend/app/services/chat_service.py` |
| Vector Knowledge Base (ChromaDB) | ✅ Complete | `backend/app/services/knowledge_base.py` |
| PDF/DOCX/TXT Document Loader | ✅ Complete | `backend/app/services/document_loader.py` |
| FastAPI Backend | ✅ Complete | `backend/main.py` |
| Source Citations | ✅ Complete | Built into chat response |
| "I Don't Know" Fallback | ✅ Complete | Built into chat service |
| Hugging Face Integration | ✅ Complete | `HuggingFaceEndpoint` LLM + Embeddings |
| Deployment Ready (Streamlit Cloud) | ✅ Complete | `requirements.txt` + `README.md` |

---

## 🚀 Quick Start

### Local Development
```bash
# 1. Clone the repo
git clone https://github.com/Aryan-404Error-Portfolio/customer-support-ai.git
cd customer-support-ai

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set Hugging Face API token
export HUGGINGFACEHUB_API_TOKEN="your_token_here"

# 5. Run the app
streamlit run app.py
```

### Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Connect your GitHub account
3. Select repo: `Aryan-404Error-Portfolio/customer-support-ai`
4. Main file: `app.py`
5. Add secret: `HUGGINGFACEHUB_API_TOKEN = your_token`
6. Click **Deploy**

---

## 📁 Project Structure

```
customer-support-ai/
├── app.py                          ← Streamlit frontend (chat + upload UI)
├── requirements.txt                ← Python dependencies
├── README.md                       ← This file
├── .gitignore                      ← Git ignore rules
│
└── backend/
    ├── main.py                     ← FastAPI app entry point
    ├── requirements.txt            ← Backend dependencies
    │
    └── app/
        ├── __init__.py
        ├── config.py               ← App settings (models, paths)
        │
        ├── services/
        │   ├── __init__.py
        │   ├── document_loader.py  ← PDF/DOCX/TXT parser
        │   ├── knowledge_base.py   ← ChromaDB vector store
        │   └── chat_service.py     ← AI chat with memory
        │
        └── routers/
            ├── __init__.py
            ├── upload.py           ← File upload API endpoints
            └── chat.py             ← Chat API endpoints
```

---

## ✨ Features

- **📁 Multi-format Upload** — Supports PDF, DOCX, and TXT files
- **🔍 Semantic Search** — Uses sentence-transformers embeddings + ChromaDB
- **💬 Conversational AI** — HuggingFace Zephyr-7B with conversation memory
- **📎 Source Citations** — Shows which document the answer came from
- **🛡️ Safe Fallback** — "I don't know" when no relevant info found
- **🧠 Memory Reset** — Clear chat history anytime
- **🗑️ KB Reset** — Clear all uploaded documents anytime

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| Backend API | FastAPI |
| LLM | HuggingFaceH4/zephyr-7b-beta |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector DB | ChromaDB |
| Document Parsing | PyPDF, python-docx |
| Framework | LangChain |

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `HUGGINGFACEHUB_API_TOKEN` | ✅ Yes | Hugging Face API token for LLM access |

Get your token: [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `HUGGINGFACEHUB_API_TOKEN` missing | Set the environment variable |
| "Collection does not exist" | Upload a document first before chatting |
| Build fails on deploy | Ensure `requirements.txt` has no strict version pins |

---

## 👤 Author

**Aryan-404Error-Portfolio**

---

*Built for educational purposes — Customer Support AI Assistant*
