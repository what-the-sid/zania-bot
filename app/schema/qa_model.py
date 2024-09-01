from pydantic import BaseModel
from typing import List

class QARequest(BaseModel):
    questions: List[str]
    document_text: str

class QAResponse(BaseModel):
    results: List[dict]
