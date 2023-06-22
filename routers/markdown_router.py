from pathlib import Path
from datetime import datetime

from fastapi.responses import FileResponse 
from fastapi import APIRouter

from controllers.markdown_controller import convert_markdown_to_marp
from controllers.markdown_controller import convert_marp_to_markdown
from controllers.marp_controller import get_theme
from models.markdown import Markdown
from models.marp import Marp
from services.data_export import md_export
from services.data_export import marp_export

router = APIRouter()

@router.post("/markdown-to-marp")
def markdown_to_marp(markdown: Markdown):
    return convert_markdown_to_marp(markdown.content)

@router.post("/marp-to-markdown")
def marp_to_markdown(marp: Markdown):
    return convert_marp_to_markdown(marp.content)

@router.post("/markdown-to-html")
def markdown_to_html(markdown: Markdown):
    md_export(markdown.content)
    current = Path()
    filename = 'md_export.html'
    file_path =f'{current}/{filename}'
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
 
    return response

@router.post("/marp-to-html")
def marp_to_html(marp: Markdown):
    marp_export(marp.content)
    current = Path()
    filename = 'marp_export.html'
    file_path =f'{current}/{filename}'
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
 
    return response

@router.post("/style")
def change_theme(marp: Marp):
    return get_theme(marp.theme)
