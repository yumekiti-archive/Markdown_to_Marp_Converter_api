from pathlib import Path
from datetime import datetime

from fastapi.responses import FileResponse 

from services.data_export import MarkdownExport, MarpExport

def md_export(markdown_content: str):
    MarkdownExport.md_export(markdown_content)
    current = Path()
    filename = 'md_export.html'
    file_path =f'{current}/{filename}'
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
 
    return response

def marp_export(marp_content: str, data_format='html'):
    MarpExport.marp_export(marp_content, data_format)
    current = Path()
    filename = f'marp_export.{data_format}'
    file_path =f'{current}/{filename}'
    
    now = datetime.now()
    
    response = FileResponse(
                            path=file_path,
                            filename=f"download_{now.strftime('%Y%m%d%H%M%S')}_{filename}"
                            )
 
    return response