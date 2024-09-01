import json
from PyPDF2 import PdfReader
from io import BytesIO

from fastapi import UploadFile

async def parse_json_file(file: UploadFile) -> str:
    # Implement JSON file parsing
    content = await file.read()
    data = json.loads(content)
    return data  # Adjust as needed to extract text

async def parse_pdf_file(file: UploadFile) -> str:
    # Read the file content
    content = await file.read()

    # Use PdfReader to extract text from PDF
    pdf_reader = PdfReader(BytesIO(content))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""  # Handle None cases if no text is extracted

    return text
