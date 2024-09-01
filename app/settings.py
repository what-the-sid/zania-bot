VERSION = "1.0.0"
TITLE = "Zania QA Bot"
DESCRIPTION = "API for answering questions based on a document using LangChain."
URL_PREFIX = "/api/v1"

CHAIN_MODEL = "gpt-4o-mini"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
LLM_TEMPLATE = "Answer the following question in a concise manner:"
QA_TEMPLATE = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "Answer the question as precise as possible using the provided context"
    "If you don't know the answer or If the answer is not contained in the context, say Data Not Available. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
    )
HTTP_ORIGINS = ["*"]
HTTP_HEADERS = ["*"]
HTTP_METHODS = ["*"]
