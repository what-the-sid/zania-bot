import json
from PyPDF2 import PdfReader
from io import BytesIO

from fastapi import UploadFile

async def parse_json_file(file: UploadFile) -> str:
    content = await file.read()
    data = json.loads(content)
    return data 

async def parse_pdf_file(file: UploadFile) -> str:
    content = await file.read()

    pdf_reader = PdfReader(BytesIO(content))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or "" 

    return text
