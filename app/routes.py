from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.schema import QARequest, QAResponse
from app.handlers import analyze_file
from app.middleware import get_qa_chain

router = APIRouter()

@router.post("/analyze-file", response_model=QAResponse)
async def question_answering(
    questions: UploadFile = File(...),
    document: UploadFile = File(...),
    chain=Depends(get_qa_chain)
):
    try:
        results = await analyze_file.handler(questions, chain)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
