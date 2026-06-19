from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def create_memory(docs):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(docs, embeddings)
    return db