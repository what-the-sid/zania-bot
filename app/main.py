import app.settings as settings

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from langserve import add_routes

from app import routes
from app.middleware import get_llm_chain, get_qa_chain

app = FastAPI(
    title = settings.TITLE,
    description = settings.DESCRIPTION,
    version = settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.HTTP_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.HTTP_METHODS,
    allow_headers=settings.HTTP_HEADERS,
)

add_routes(
    app,
    get_llm_chain(),
    path="/chain",
)

app.include_router(
    routes.router,
    prefix=settings.URL_PREFIX,
    dependencies=[Depends(lambda: get_qa_chain)])
