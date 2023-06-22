import os
from fastapi import HTTPException
from services.get_theme import Theme

def get_theme(theme: str):
    if f"{theme}.css" not in os.listdir("styles") and theme not in ["default", "gaia", "uncover"]:
        return HTTPException(status_code=404, detail=f"This theme ({theme}) does not exist. You can choose from {', '.join([file.split('.')[0] for file in os.listdir('styles')])} and default, gaia, uncover.")
    theme_content = Theme.get_theme(theme)
    return {"content": theme_content}