from typing import Dict, List
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re

def clean_text(text: str) -> str:
    # Fix merged words (basic)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    # Optional: add space between lowercase-uppercase (PDF issue)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)

    return text

def chunk_texts(pdf_dict:Dict[str,str]) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 150
    )
    chunks = []
    for filename, text in pdf_dict.items():
        clean_texts = clean_text(text)
        split_chunks = splitter.split_text(clean_texts)
        chunks.extend(split_chunks)

    return chunks