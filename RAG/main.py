from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-code-latest", temperature=0.7)
data = TextLoader("/Users/sandesh04/Desktop/Projects/Gen AI/RAG/document-loaders/notes.txt")
notes = data.load()

template = ChatPromptTemplate.from_messages([
    ("system", "You are helpful ai that summarizes the following notes."),
    ("human","{notes}")
])

prompt = template.format_prompt(notes=notes[0].page_content)

results = model.invoke(prompt)
print(results.content)