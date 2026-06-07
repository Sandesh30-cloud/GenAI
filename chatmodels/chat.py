from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import langchain_mistralai

load_dotenv()

MODEL = "mistralai:mistral-code-latest"
# MODEL = "google_genai:gemini-2.5-flash"
# MODEL = "groq:qwen/qwen3-32b"
# MODEL = "groq:llama-3.3-70b-versatile"
# MODEL = "openai:gpt-4o-mini"

llm = init_chat_model(MODEL)

response = llm.invoke("What is LLM?")

print(response.content)