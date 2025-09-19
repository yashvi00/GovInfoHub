# app.py (guarded version — replace your current file with this)
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

# -------------------------
# Guarded / optional imports
# -------------------------
def try_import(module_name, fromlist=None):
    try:
        if fromlist:
            return __import__(module_name, fromlist=fromlist)
        return __import__(module_name)
    except Exception as e:
        print(f"Optional import failed: {module_name} -> {e}")
        return None

langchain = try_import("langchain")
hf_hub = try_import("huggingface_hub")
googletrans = try_import("googletrans")
# Try to import LlamaCpp class if langchain is present
LlamaCpp = None
PromptTemplate = None
if langchain is not None:
    try:
        from langchain.llms import LlamaCpp as _LlamaCpp
        from langchain.prompts import PromptTemplate as _PromptTemplate
        LlamaCpp = _LlamaCpp
        PromptTemplate = _PromptTemplate
    except Exception as e:
        print("Could not import LlamaCpp or PromptTemplate from langchain:", e)

# Try to import HF download helper
hf_hub_download = None
if hf_hub is not None:
    try:
        from huggingface_hub import hf_hub_download as _hf_hub_download
        hf_hub_download = _hf_hub_download
    except Exception as e:
        print("Could not import hf_hub_download:", e)

# Try translator utilities
Translator = None
LANGUAGES = {}
if googletrans is not None:
    try:
        from googletrans import Translator as _Translator, LANGUAGES as _LANGUAGES
        Translator = _Translator
        LANGUAGES = _LANGUAGES
    except Exception as e:
        print("Could not import googletrans Translator:", e)

# -------------------------
# App setup
# -------------------------
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# -------------------------
# Minimal fallback LLM
# -------------------------
class DummyLLM:
    """Simple fallback LLM that returns a short canned response in English."""
    def __init__(self):
        pass

    def invoke(self, input_dict):
        q = input_dict.get("question") or ""
        # Very short heuristic reply
        return "I don't have the model available here. Please try again later or use the hosted demo."

# -------------------------
# GovInfoHub logic
# -------------------------
class GovInfoHub:
    def __init__(self):
        self.llm_chain = None
        self.system_prompt = "You are a helpful AI assistant who answers questions in short sentences."

    def initialize_llm_chain(self):
        # If chain already initialized, nothing to do
        if self.llm_chain:
            return

        # Try to use LlamaCpp via langchain if available + model download possible
        if LlamaCpp is not None and PromptTemplate is not None and hf_hub_download is not None:
            try:
                (repo_id, model_file_name) = ("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", "mistral-7b-instruct-v0.1.Q4_0.gguf")
                model_path = hf_hub_download(repo_id=repo_id, filename=model_file_name, repo_type="model")
                llm = LlamaCpp(
                    model_path=model_path,
                    temperature=0,
                    max_tokens=512,
                    top_p=1,
                    stop=["[INST]"],
                    verbose=False,
                    streaming=True,
                )
                template = """
                <s>[INST]{}[/INST]</s>

                [INST]{}[/INST]
                """.format(self.system_prompt, "{question}")
                prompt = PromptTemplate(template=template, input_variables=["question"])
                # Using langchain pipes if available
                try:
                    self.llm_chain = prompt | llm
                except Exception:
                    # If pipe operator isn't supported, store callable wrapper
                    self.llm_chain = lambda data: llm.invoke({"input": data.get("question")})
                print("Initialized LlamaCpp-based chain with model:", model_path)
                return
            except Exception as e:
                print("Failed to initialize LlamaCpp chain:", e)

        # If anything fails, fall back to dummy LLM
        print("Falling back to DummyLLM.")
        self.llm_chain = DummyLLM()

    def get_response(self, user_input):
        self.initialize_llm_chain()

        # Detect user input language
        input_lang = self.detect_language(user_input)

        # Translate user input to English (if translator available)
        english_input = self.translate(user_input, src_lang=input_lang, dest_lang="en")

        # Pass English input to AI (llm_chain may be a callable or object with invoke)
        try:
            if hasattr(self.llm_chain, "invoke"):
                raw_response = self.llm_chain.invoke({"question": english_input})
            else:
                # callable
                raw_response = self.llm_chain({"question": english_input})
        except Exception as e:
            print("LLM invocation failed:", e)
            raw_response = "Sorry — the model failed to generate a response."

        # Translate AI response back to user's language if possible
        translated_response = self.translate(raw_response, src_lang="en", dest_lang=input_lang)

        return translated_response

    def translate(self, text, src_lang, dest_lang):
        # If translator is available and languages differ, translate
        if Translator is not None and src_lang and dest_lang and src_lang != dest_lang:
            try:
                translator = Translator()
                translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
                return translated_text
            except Exception as e:
                print("Translation failed:", e)
                return text
        # No translator or no translation needed
        return text

    def detect_language(self, text):
        if Translator is not None:
            try:
                translator = Translator()
                detected_lang = translator.detect(text).lang
                return detected_lang
            except Exception as e:
                print("Language detection failed:", e)
                # fallback to English
                return "en"
        return "en"

gov_info_hub = GovInfoHub()

# -------------------------
# Routes
# -------------------------
@app.get("/")
async def read_root():
    # Change directory to where main.html resides
    directory = os.path.join(os.path.dirname(__file__), "FRONTEND", "src")
    file_path = os.path.join(directory, "main.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    # If frontend not present, return a simple message
    return {"status": "Frontend not found", "path": file_path}

@app.post("/ask/")
async def ask_question(question: str):
    if not question:
        raise HTTPException(status_code=400, detail="Please provide a question.")
    response = gov_info_hub.get_response(question)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
