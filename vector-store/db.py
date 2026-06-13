from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.documents import Document

chroma = Chroma()
docs = [
    Document(page_content="Python is widely used in Artificial Intelligence."),
    Document(page_content="Pandas is used for data analysis in Python.", metadata={}),
    Document(page_content="Neural networks are used in deep learning.", metadata={})
]

embedding_model = HuggingFaceEmbeddings()

vector_store = Chroma.from_documents(docs, embedding_model, persist_directory="chroma_db")
res = vector_store.similarity_search("networks are")

print(res[0].page_content)

retriever = vector_store.as_retriever()
docs = retriever.invoke("networks are")