import subprocess

class MarpConverter:
    @staticmethod
    def convert_to_marp(markdown_content: str) -> str:
        marp_content = "---\nmarp: true\npaginate: true\nsize: 16:9\ntheme: default\n---\n\n"

        code_block_started = False

        lines = markdown_content.split("\n")
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                marp_content += f'\n---\n\n<!--\n_class: headline\n-->\n\n# {title}\n'
            elif line.startswith("## "):
                subtitle = line[3:].strip()
                marp_content += f'\n---\n\n<!--\n_class: general\n-->\n\n## {subtitle}\n'
            elif line.startswith("```"):
                if code_block_started:
                    marp_content += line + "\n"
                else:
                    marp_content += "---\n" + line + "\n"
                code_block_started = not code_block_started
            else:
                marp_content += f"{line}\n"

        prettier_command = "npx --yes prettier --parser=markdown --print-width 120 --prose-wrap always --write"
        formatted_content = subprocess.check_output(f"echo '{marp_content}' | {prettier_command}", shell=True).decode("utf-8")

        formatted_content = formatted_content.replace("---\n\n---\n\n", "---\n\n")

        return formatted_content
