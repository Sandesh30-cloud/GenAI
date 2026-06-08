# Basic Chatbot

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import langchain_mistralai
import langchain_google_genai 
from langchain.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

MODEL = "mistralai:mistral-code-latest"
# MODEL = "google_genai:gemini-2.5-flash-lite"
# MODEL = "groq:qwen/qwen3-32b"
# MODEL = "groq:llama-3.3-70b-versatile"
# MODEL = "openai:gpt-4o-mini"

print("Enter AI Mode:")
Ai_mode = input()
message = [
    SystemMessage(content=Ai_mode),
]

llm = init_chat_model(MODEL, temperature=0.3)

while True:
    prompt = input("You: ")
    message.append(HumanMessage(content=prompt))
    response = llm.invoke(message)
    message.append(AIMessage(content=response.content))
    print("AI: ", response.content)









