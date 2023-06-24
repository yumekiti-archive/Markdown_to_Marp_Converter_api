import re
import mdformat

class MarkdownConverter:
    @staticmethod
    def convert_to_markdown(marp_content: str) -> str:
        marp_content = re.sub(r'<!--[\s\S]*?-->', '', marp_content)
        marp_content = re.sub(r'<br>', '', marp_content)

        lines = marp_content.split("\n")
        markdown_lines = []

        metadata_prefixes = ["---", "marp:", "paginate:", "theme:", "size:"]
        comment_prefixes = ["<!--", "-->"]
        header_prefixes = ["_class", "_header", "backgroundColor", "backgroundImage"]

        for line in lines:
            if any(line.startswith(prefix) for prefix in metadata_prefixes):
                # ドキュメントのメタデータ部分を削除します
                continue
            elif any(line.startswith(prefix) for prefix in comment_prefixes):
                # Marpのコメント部分を削除します
                continue
            elif any(line.startswith(prefix) for prefix in header_prefixes):
                # ヘッダー部分の指定を削除します
                continue
            elif line.strip() == "":
                # 空行を削除します
                continue
            else:
                # そのままの行を追加します
                markdown_lines.append(line)

        markdown_content = "\n\n".join(markdown_lines)

        formatted_content = mdformat.text(markdown_content)

        formatted_content = '\n'.join([line for line in formatted_content.splitlines() if line.strip()])
        
        indention_prefixes = ["# ", "## ", "### ", "#### ", "##### ", "###### "]

        lines = formatted_content.split("\n")
        for line in lines:
            if any(line.startswith(prefix) for prefix in indention_prefixes):
                formatted_content = formatted_content.replace(line, "\n" + line)

        return formatted_content
