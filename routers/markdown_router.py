from fastapi import APIRouter
from controllers.markdown_controller import convert_markdown_to_marp
from models.markdown import Markdown

router = APIRouter()

@router.post("/markdown-to-marp")
def markdown_to_marp(markdown: Markdown):
    return convert_markdown_to_marp(markdown.content)
