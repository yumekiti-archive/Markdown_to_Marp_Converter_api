from fastapi import FastAPI
from routers import markdown_router
from routers import marp_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://marplify.yumekiti.net",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(markdown_router.router)
app.include_router(marp_router.router)
