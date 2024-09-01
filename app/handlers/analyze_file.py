import json
from fastapi import UploadFile, HTTPException

from app.utils import parse_json_file  # Assume these functions are implemented
from app.schema import QAResponse

from langchain.chains import QAGenerationChain
from langchain.llms import OpenAI

async def handler(questions_file: UploadFile, chain) -> QAResponse:
    results = []
    questions = await parse_json_file(questions_file)

    print(questions)
    for question in questions:
        try:
            response = chain.invoke({"input": question })
            results.append({"question": question, "answer": response["answer"]})
        except Exception as e:
            results.append({"question": question, "answer": str(e)})

    return QAResponse(results=results)
