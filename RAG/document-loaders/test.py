from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()
data = TextLoader("./notes.txt")
notes = data.load()

# print(notes)
# print(notes[0].page_content)
print(len(notes))
