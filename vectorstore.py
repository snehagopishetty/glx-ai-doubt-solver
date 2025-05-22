# from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAI
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()

def create_vectorstore():
    with open("data/doubts.txt") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_text(text)
    documents = [Document(page_content=chunk) for chunk in chunks]

    embeddings = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    db = FAISS.from_documents(documents, embeddings)

    return db
