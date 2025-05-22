from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain_cohere import CohereEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

def create_vectorstore():
    with open("data/doubts.txt") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_text(text)
    documents = [Document(page_content=chunk) for chunk in chunks]

    embeddings = CohereEmbeddings(
    model="embed-english-v3.0", # or another supported model
    cohere_api_key=os.getenv("COHERE_API_KEY")
    )
        
    db = FAISS.from_documents(documents, embeddings)
    return db
