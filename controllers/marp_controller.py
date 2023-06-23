import os
from fastapi import HTTPException
from services.get_theme import GetTheme

def get_theme(theme: str):
    style = GetTheme.get_theme(markdown_content)
    return {"style": style, "theme": theme}