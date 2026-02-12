from fastapi import APIRouter
from pydantic import BaseModel

from app.document_rag.services.vector_store import load_index, search
from app.common.llm_client import ask_llm


router = APIRouter()


# ===============================
# REQUEST MODEL
# ===============================
class QueryRequest(BaseModel):
    question: str


# ===============================
# QUERY ENDPOINT
# ===============================
@router.post("/query")
def ask_question(request: QueryRequest):

    # load index
    index, documents = load_index()

    # retrieval
    contexts = search(index, documents, request.question, k=3)
    context_text = "\n".join(contexts)

    # ask LLM
    answer = ask_llm(context_text, request.question)

    return {
        "question": request.question,
        "answer": answer
    }
