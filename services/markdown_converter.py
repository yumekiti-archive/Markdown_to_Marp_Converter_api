import subprocess
import re

class MarkdownConverter:
    @staticmethod
    def convert_to_markdown(marp_content: str) -> str:
        marp_content = re.sub(r'<!--[\s\S]*?-->', '', marp_content)

        lines = marp_content.split("\n")
        markdown_lines = []

        for line in lines:
            if line.startswith("---"):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif line.startswith("marp:"):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif line.startswith("paginate:"):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif line.startswith("theme:"):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif line.startswith("size:"):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif line.startswith("<!--"):
                # Marpのコメント部分を削除します
                continue
            elif line.startswith("-->"):
                # Marpのコメント部分を削除します
                continue
            elif line.startswith("_class"):
                # ヘッダー部分のクラス指定を削除します
                continue
            elif line.startswith("_header"):
                # ヘッダー部分のヘッダー指定を削除します
                continue
            elif line.strip() == "":
                # 空行を削除します
                continue
            else:
                # そのままの行を追加します
                markdown_lines.append(line)

        markdown_content = "\n".join(markdown_lines)

        prettier_command = "npx --yes prettier --parser=markdown --prose-wrap always --write"
        formatted_content = subprocess.check_output(f"echo '{markdown_content}' | {prettier_command}", shell=True).decode("utf-8")

        return formatted_content
