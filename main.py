from fastapi import FastAPI
from routers import markdown_router

app = FastAPI()

app.include_router(markdown_router.router)
