import os
import app.settings as settings

from fastapi import FastAPI, Depends

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

from app import routes
from app.middleware import get_llm_chain, get_qa_chain

app = FastAPI(
    title = settings.TITLE,
    description = settings.DESCRIPTION,
    version = settings.VERSION,
)

# Add LangChain routes
add_routes(
    app,
    get_llm_chain(),
    path="/chain",
)

# Include application routes
app.include_router(
    routes.router,
    prefix=settings.URL_PREFIX,
    dependencies=[Depends(lambda: get_qa_chain)])
