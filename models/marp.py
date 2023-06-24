from pydantic import BaseModel

class Marp(BaseModel):
    content: str
    style: str
