from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma 
from dotenv import load_dotenv

load_dotenv()

data = PyPDFLoader("/Users/sandesh04/Desktop/Projects/Gen AI/RAG/document-loaders/RAG.pdf")
docs = data.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

embedding_model = HuggingFaceEmbeddings()

vector_store = Chroma.from_documents(chunks, embedding_model, persist_directory="chroma_db")