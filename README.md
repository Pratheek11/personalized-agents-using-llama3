# 🧠 Electron + LangChain + LLaMA 3 Personal Assistant

This project is a local AI-powered personal assistant that:
- Uses **LLaMA 3** (via Ollama) as the local LLM
- Integrates with **LangChain agents** to summarize Gmail and Google Calendar
- Has a desktop UI built with **Electron**
- Uses **FastAPI** as the backend API server
- Returns responses in **Markdown format** for rich UI rendering

---

## ⚙️ Architecture Overview

        ┌────────────┐         ┌────────────┐
        │  Electron  │  ─────▶ │  FastAPI   │
        │  Frontend  │         │  Backend   │
        └────────────┘         └────┬───────┘
                                     │
                     ┌────────────┐  │
                     │ LangChain  │◀─┘
                     │ Agents     │
                     └────┬───────┘
                          │
                   ┌────────────┐
                   │ LLaMA 3 LLM│
                   │ via Ollama │
                   └────────────┘


---

## 🛠️ Features

- 🔌 Local-only LLM via [Ollama](https://ollama.com)
- 📅 Summarize today's Google Calendar events
- 📬 Summarize unread Gmail emails
- 🧠 LangChain agents with tool calling
- 💬 Frontend sends prompt → backend handles agent logic → returns Markdown summary

---

## 🖥️ Frontend (Electron)

```bash
cd frontend
npm install
npm start
```

## Local LLM

```bash
ollama run llama3
```

## 🖥️ Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```