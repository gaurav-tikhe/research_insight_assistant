from typing import List
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("hf_token")


# def create_faiss_index(chunks: List[str]):
#     embeddings = HuggingFaceEmbeddings(
#         model = "sentence-transformers/all-MiniLM-L6-v2"
#     )
#     vectorstore = FAISS.from_texts(chunks,embeddings)

#     return vectorstore

def create_faiss_index(chunks: List[str]):
    # print(f"Number of chunks: {len(chunks)}")
    # print(f"First chunk: {chunks[0] if chunks else 'EMPTY'}")
    
    embeddings = HuggingFaceEmbeddings(
        model="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore
