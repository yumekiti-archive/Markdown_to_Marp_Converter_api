from fastapi import FastAPI
from routers import markdown_router, marp_router, post_router
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

DB_PATH = "database.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS posts (uuid TEXT PRIMARY KEY, content TEXT, style TEXT, created_at TEXT, updated_at TEXT)"
    )
    conn.commit()
    conn.close()

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
app.include_router(post_router.router)

create_table()