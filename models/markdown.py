from pydantic import BaseModel

class Markdown(BaseModel):
    content: str
