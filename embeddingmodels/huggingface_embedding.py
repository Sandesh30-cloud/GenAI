from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model="all-MiniLM-L6-v2"
)

vector = embeddings.embed_query("What is Hugging Face?")
print(vector)
