from services.marp_converter import MarpConverter

def convert_markdown_to_marp(markdown_content: str):
    marp_content = MarpConverter.convert_to_marp(markdown_content)
    return {"marp_content": marp_content}
