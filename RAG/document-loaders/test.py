from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from dotenv import load_dotenv

load_dotenv()
data = TextLoader("/Users/sandesh04/Desktop/Projects/Gen AI/RAG/document-loaders/notes.txt")
notes = data.load()

# print(notes)
# print(notes[0].page_content)
print(len(notes))

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1   
)
chunks = splitter.split_documents(notes)
print(chunks)