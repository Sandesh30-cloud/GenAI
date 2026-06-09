from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv


load_dotenv()

data = PyPDFLoader("/Users/sandesh04/Desktop/Projects/Gen AI/RAG/document-loaders/RAG.pdf")

docs = data.load()
print(len(docs))