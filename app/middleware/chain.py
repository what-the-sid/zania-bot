import os
import tempfile

import app.settings as settings

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, JSONLoader

from io import BytesIO

from fastapi import Request, HTTPException, UploadFile, Depends

async def get_document(request: Request):
    form = await request.form()
    document = form["document"]
    return document

def get_llm_chain():

    system_template = settings.LLM_TEMPLATE
    prompt_template = ChatPromptTemplate.from_messages([
        ('system', system_template),
        ('user', '{question}')
    ])
    model = ChatOpenAI(model_name=settings.CHAIN_MODEL)
    parser = StrOutputParser()
    llm_chain = prompt_template | model | parser
    return llm_chain

async def get_qa_chain(document = Depends(get_document)):
    if document.content_type == "application/pdf":
        loader_func = PyPDFLoader
    elif document.content_type == "application/json":
        loader_func = JSONLoader
    else:
        raise HTTPException(status_code=400, detail="Unsupported document file format")
    docs = None
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir,document.filename)

        with open(temp_file_path,'wb') as temp_file:
            content = await document.read()
            temp_file.write(content)
        docs = loader_func(temp_file_path).load()

    model = ChatOpenAI(model_name=settings.CHAIN_MODEL)  # Initialize your LLM
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

    retriever = vectorstore.as_retriever()

    # Define system prompt and chain
    system_prompt = settings.QA_TEMPLATE

    prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", system_prompt),
                    ("human", "{input}"),
                ]
            )
    question_answer_chain = create_stuff_documents_chain(model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain
