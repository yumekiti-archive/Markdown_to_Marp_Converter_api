import sqlite3
from datetime import datetime
import pytz

DB_PATH = "database.db"

class Post:
    def __init__(self, uuid: str, content: str, style: str, created_at: str = None, updated_at: str = None):
        self.uuid = uuid
        self.content = content
        self.style = style
        self.created_at = created_at or datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = updated_at or datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")

    def save(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (uuid, content, style, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
            (self.uuid, self.content, self.style, self.created_at, self.updated_at)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_uuid(uuid: str):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT content, style, created_at FROM posts WHERE uuid=?",
            (uuid,)
        )
        result = cursor.fetchone()
        conn.close()
        if result:
            return Post(uuid=uuid, content=result[0], style=result[1], created_at=result[2])
        else:
            return None
