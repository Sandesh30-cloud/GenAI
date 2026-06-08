from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
# vector = embeddings.embed_query("What is Hugging Face?")
# print(vector)

text = [
    "Hello, this is a test.",
    "What is Hugging Face?",
    "How does the Gemini model work?",
    "What are the benefits of using embeddings?",
    "Can you explain the concept of embeddings?"
]

vectors = embeddings.embed_documents(text)
print(vectors)
