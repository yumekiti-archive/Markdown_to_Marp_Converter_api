from fastapi.responses import FileResponse 
from fastapi import APIRouter

from controllers.markdown_controller import convert_marp_to_markdown
from controllers.marp_controller import get_theme
from controllers.export_controller import md_export, marp_export
from models.markdown import Markdown
from models.marp import Marp

router = APIRouter()

@router.post("/marp-to-markdown")
def marp_to_markdown(marp: Markdown):
    return convert_marp_to_markdown(marp.content)

@router.post("/markdown-to-html")
def markdown_to_html(markdown: Markdown):
    return md_export(markdown.content)
