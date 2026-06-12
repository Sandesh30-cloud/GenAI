from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from langchain_mistralai import ChatMistralAI

load_dotenv()

data = PyPDFLoader("/Users/sandesh04/Desktop/Projects/Gen AI/RAG/document-loaders/RAG.pdf")
docs = data.load()
# print(len(docs))
# print(docs[20])
splitter = TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=1   
)
chunks = splitter.split_documents(docs)
print(chunks[0])