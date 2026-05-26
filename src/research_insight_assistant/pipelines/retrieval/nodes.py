from typing import List

def retrieve_chunks(query: str, vectorstore, k: int = 3) -> List[str]:
    docs = vectorstore.similarity_search(query,k=6)
    # print(f"Retrieved Chunks :- {docs}")
    return [doc.page_content for doc in docs]