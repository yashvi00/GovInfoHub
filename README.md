# GovInfoHub 🏛️🤖

An AI-powered chatbot that helps users quickly get information about government schemes, policies, and services.  
Built with **FastAPI**, **LangChain**, **LlamaCpp**, and a simple **HTML/JS frontend**.

---

## ✨ Features
- 🌐 Multilingual support (auto-detects language, translates, responds back in the same language)
- 🤖 AI chatbot designed to use a local LLM (Mistral-7B GGUF via `llama-cpp`) when available
- ⚡ REST API built with FastAPI
- 🎨 Minimal frontend served with FastAPI or run standalone in browser
- 🚀 Ready to deploy on Render (recommended) or Vercel (experimental)

---



## ⚡ Getting Started (Local)

### 1. Clone the repo
```bash
git clone https://github.com/yashvi00/GovInfoHub.git
cd GovInfoHub
2. Set up Python environment
⚠️ Recommended: Python 3.11 (not 3.13 — some binary wheels are not yet available for newer versions)

bash
Copy code
# Create virtual environment
python -m venv venv

# Activate venv
# Windows (PowerShell):
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Upgrade pip/setuptools/wheel
python -m pip install --upgrade pip setuptools wheel
3. Install dependencies
bash
Copy code
# Use the frozen requirements (preferred)
pip install -r requirements-frozen.txt

# Or use the original requirements (may require build tools)
pip install -r requirements.txt
If pip install fails on packages like numpy or other native libraries, consider installing Python 3.11 or the Microsoft Build Tools (C++ workload) on Windows.

4. Run backend
bash
Copy code
# from project root or from AI - CHATBOT-MAIN folder
uvicorn "AI - CHATBOT-MAIN.app:app" --reload
Backend runs at → http://127.0.0.1:8000

5. Open frontend
Option A: Let FastAPI serve it → open http://127.0.0.1:8000

Option B: Run local static server

bash
Copy code
cd FRONTEND/src
python -m http.server 8080
Open http://127.0.0.1:8080/main.html

☁️ Deployment
Render (recommended)
Render runs full Python web services (no serverless packaging limits):

Push the repository to GitHub.

On Render, create a New → Web Service, connect to your GitHub repo.

Use these settings:

Build Command

bash
Copy code
pip install -r requirements-frozen.txt
Start Command

bash

cd "AI - CHATBOT-MAIN" && uvicorn app:app --host 0.0.0.0 --port $PORT
Deploy and Render will give you a public URL.


🛠️ Development Notes
First-time model run will download Mistral-7B GGUF (~several GB) from HuggingFace if the app attempts to use a local GGUF model.

If you don't want to run a local LLM, replace the LlamaCpp usage with an external API (OpenAI or another hosted LLM) — that's simpler and faster for a demo.

We include guarded imports in app.py so the server can run without heavy ML libs for frontend testing.

Keep venv/ out of the repository (add to .gitignore).

✅ Quick Troubleshooting
ModuleNotFoundError for fastapi / uvicorn: activate venv, then pip install fastapi uvicorn[standard].

pip errors building numpy: switch to Python 3.11 or install Visual Studio Build Tools.

git push 403/permission errors: use gh auth login (GitHub CLI), HTTPS with a PAT, or set up SSH keys.

🤝 Contributing
Contributions are welcome! Please open issues for bugs or feature requests, and submit pull requests for improvements.

📜 License
This project is open source — include your chosen license file (e.g., MIT).

Contact
If you need help running or deploying the project, open an issue or contact the maintainer at 
yashvirajpal0@gmail.com
www.linkedin.com/in/yashvi-rajpal






