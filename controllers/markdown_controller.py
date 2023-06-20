from services.marp_converter import MarpConverter
from services.markdown_converter import MarkdownConverter

def convert_markdown_to_marp(markdown_content: str):
    marp_content = MarpConverter.convert_to_marp(markdown_content)
    return {"content": marp_content}

def convert_marp_to_markdown(marp_content: str):
    markdown_content = MarkdownConverter.convert_to_markdown(marp_content)
    return {"content": markdown_content}