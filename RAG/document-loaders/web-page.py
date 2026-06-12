from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()

url = "https://www.apple.com/in/mac/compare/?modelList=MacBook-Air-M4"
data = WebBaseLoader(url).load()

print(data[0].page_content)