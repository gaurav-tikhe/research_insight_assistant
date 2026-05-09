from typing import Dict, List
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_texts(pdf_dict:Dict[str,str]) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )
    chunks = []
    for filename, text in pdf_dict.items():
        split_chunks = splitter.split_text(text)
        chunks.extend(split_chunks)

    return chunks