from typing import List
import ollama

def generate_answer(query: str, retrieved_chunks: List[str]) -> str:
    context = "\n\n".join(retrieved_chunks)
    
    prompt = f"""
    You are a research assistant.
    Use only the following context to answer the question. 

    Context:
    {context}

    Question:
    {query}

    Instructions:
    - Answer clearly
    - Cite sources like [Chunk 1], [Chunk 2] etc.

    Answer:
"""
    response = ollama.chat(
        model="llama3:8b",
        messages=[{"role": "user", "content": prompt}],
    )
    
    answer = response["message"]["content"]

    sources = [f"[Chunk {i}] {doc[:200]}" for i, doc in enumerate(retrieved_chunks)]
    
    answer_json = {"answer": answer, "sources": sources}
    print(f"Answer: {answer_json}")
    return answer_json