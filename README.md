# 🏛️ GovInfoHub

*GovInfoHub* is an **AI-powered chatbot platform** that helps users explore and understand *government schemes, policies, and services*.  
It features a **multilingual chatbot** (auto-detect + translate), a **FastAPI backend**, and a **minimal HTML/JS frontend**.  

This project was built as part of my *learning journey in AI + full-stack development*.  
I’m actively seeking **internship opportunities, collaborations, and open-source contributions**.

---

## 🚀 Live Demo
🔗 https://gov-info-hub.vercel.app/

---

## 🔧 Tech Stack

### 🔹 Frontend:
- *HTML5*  
- *CSS3*  
- *Vanilla JavaScript*  

### 🔹 Backend:
- *Python*  
- *FastAPI*  
- *LangChain*  
- *LlamaCpp* (local LLM inference, Mistral-7B GGUF)  

### 🔹 Other Tools & Services:
- *Hugging Face Hub* – Model hosting  
- *Google Translate API* – Language detection & translation  
- *Uvicorn* – ASGI server  
- *Render / Vercel* – Deployment  

---

## 📦 Features

### 👤 User Features:
- Chat with AI about government schemes & services.  
- Automatic language detection (supports multiple languages).  
- Responses translated back into the user’s language.  
- Simple and responsive web interface.  

### 🛠 Developer Features:
- Backend served with *FastAPI*.  
- Integrated with *LangChain* for prompt engineering.  
- *CORS enabled* for frontend-backend communication.  
- Ready-to-deploy setup with `requirements.txt`.  

---

## 🌟 Upcoming Features
- 🔍 *Search functionality* for government documents.  
- 📊 *Dashboard* for usage analytics.  
- 🗄 *Database integration* (PostgreSQL/MongoDB).  
- ☁ *Option to switch from local LLM to OpenAI API*.  

---

## 🛠 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yashvi00/GovInfoHub.git
cd GovInfoHub
2️⃣ Backend Setup
bash
Copy code
cd "AI - CHATBOT-MAIN"
python -m venv venv
.\venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # macOS/Linux

pip install --upgrade pip setuptools wheel
pip install -r ../requirements-frozen.txt
Start Backend:

bash
Copy code
uvicorn app:app --reload
3️⃣ Frontend Setup
Option A: Served by FastAPI → open
👉 http://127.0.0.1:8000

Option B: Run locally:

bash
Copy code
cd FRONTEND/src
python -m http.server 8080
👉 Open http://127.0.0.1:8080/main.html




🤝 Looking to Collaborate
I’m currently working solo and open to:

Internship roles 🧑‍💻

Open-source contribution opportunities 🌐

Project collaborations 🤝

📫 Contact
📧 Email: yashvirajpal0@gmail.com
💼 LinkedIn: www.linkedin.com/in/yashvi-rajpal
🐙 GitHub: github.com/yashvi00

⭐ Don’t forget to star this repo if you like it!


