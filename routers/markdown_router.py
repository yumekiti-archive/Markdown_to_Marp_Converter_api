from fastapi.responses import FileResponse 
from fastapi import APIRouter

from controllers.markdown_controller import convert_markdown_to_marp
from controllers.markdown_controller import convert_marp_to_markdown
from controllers.marp_controller import get_theme
from controllers.export_controller import md_export, marp_export
from models.markdown import Markdown
from models.marp import Marp

router = APIRouter()

@router.post("/markdown-to-marp")
def markdown_to_marp(markdown: Markdown):
    return convert_markdown_to_marp(markdown.content)

@router.post("/marp-to-markdown")
def marp_to_markdown(marp: Markdown):
    return convert_marp_to_markdown(marp.content)

@router.post("/markdown-to-html")
def markdown_to_html(markdown: Markdown):
    return md_export(markdown.content)

@router.post("/marp-to-html")
def marp_to_html(marp: Markdown):
    return marp_export(marp.content)

@router.post("/marp-to-pdf")
def marp_to_html(marp: Markdown):
    return marp_export(marp.content, "pdf")

@router.post("/style")
def change_theme(marp: Marp):
    return get_theme(marp.theme)
