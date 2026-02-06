from fastapi import APIRouter
from app.document_rag.services.vector_store import load_index, search
from app.common.llm_client import ask_llm

router = APIRouter()

@router.post("/query")
def ask_question(question: str):
    index, documents = load_index()
    contexts = search(index, documents, question, k=3)
    context_text = "\n".join(contexts)

    answer = ask_llm(context_text, question)

    return {
        "question": question,
        "answer": answer
    }
