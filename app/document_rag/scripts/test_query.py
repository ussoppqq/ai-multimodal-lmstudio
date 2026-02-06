from app.document_rag.services.vector_store import load_index, search
from app.common.llm_client import ask_llm

QUESTION = "Apa topik utama dari dokumen ini?"

index, documents = load_index()

contexts = search(index, documents, QUESTION, k=3)
context_text = "\n".join(contexts)

print("=== CONTEXT ===")
print(context_text)

answer = ask_llm(context_text, QUESTION)

print("\n=== LLM ANSWER ===")
print(answer)
