from fastapi import APIRouter
from controllers.markdown_controller import convert_markdown_to_marp
from controllers.markdown_controller import convert_marp_to_markdown
from controllers.marp_controller import get_theme
from models.markdown import Markdown
from models.marp import Marp

router = APIRouter()

@router.post("/markdown-to-marp")
def markdown_to_marp(markdown: Markdown):
    return convert_markdown_to_marp(markdown.content)

@router.post("/marp-to-markdown")
def marp_to_markdown(marp: Markdown):
    return convert_marp_to_markdown(marp.content)

@router.post("/style")
def change_theme(marp: Marp):
    return get_theme(marp.theme)