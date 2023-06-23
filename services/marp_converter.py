import subprocess
import mdformat

class MarpConverter:
    @staticmethod
    def convert_to_marp(markdown_content: str) -> str:
        marp_content = "---\nmarp: true\npaginate: true\nsize: 16:9\ntheme: default\n---\n"

        code_block_started = False
        header = ""

        formatted_markdown_content = mdformat.text(markdown_content)

        lines = formatted_markdown_content.split("\n")
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                header = title
                marp_content += f'\n---\n\n<!--\n_class: headline\n-->\n\n# {title}\n'
            elif line.startswith("## "):
                subtitle = line[3:].strip()
                marp_content += f'\n---\n\n<!--\n_class: general\n_header: {header}\n-->\n\n## {subtitle}\n'
            elif line.startswith("```"):
                if code_block_started:
                    marp_content += line + "\n"
                else:
                    marp_content += "---\n" + line + "\n"
                code_block_started = not code_block_started
            else:
                marp_content += f"{line}\n"

        marp_content = marp_content.replace("---\n\n---\n\n", "---\n\n")
        marp_content = marp_content.replace("。", "。<br>")
        marp_content = marp_content.replace("．", "．<br>")
        marp_content = marp_content.replace("？", "？<br>")
        marp_content = marp_content.replace("！", "！<br>")

        return marp_content
