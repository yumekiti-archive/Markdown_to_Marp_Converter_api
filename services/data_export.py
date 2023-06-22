import markdown
# import pdfkit # wkhtmltopdfのインストールが必要 https://wkhtmltopdf.org/downloads.html
import subprocess

# md_text: markdown形式のテキスト
# data_format: エクスポートするデータの形式（html,pdf)
class MarkdownExport:
    def md_export(md_text,data_format='html'):
        md = markdown.Markdown()
        html_body = md.convert(md_text)
        # print(html_body)
        html_text = '<html lang="ja"><meta charset="utf-8"><body>'
        # html_text += '<style> body { font-size: 8em; } </style>'
        html_text += html_body + '</body></html>'
        if data_format == 'html':
            with open('md_export.html','w') as f:
                f.write(html_text)
            # return html_text
        
        options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8"
        }
        if data_format == 'pdf':
            pdfkit.from_string(html_text, "md_export.pdf",options=options)

# Marpからhtml,pdfに変換
# https://www.npmjs.com/package/@marp-team/marp-cli を使用
# marp_text: marp形式のテキスト
# data_format: エクスポートするデータの形式（html,pdf)
# 動作にNode.jsが必要
class MarpExport:
    def marp_export(marp_text,data_format='html'):
        marp_file = 'marp_export.md'
        # print(marp_file[:-2]+'html')
        with open(marp_file,'w',encoding='utf-8') as f:
            f.write(marp_text)
        if data_format == 'html':
            
            subprocess.run('npx --yes @marp-team/marp-cli@latest '+ marp_file,shell=True)
            
        if data_format == 'pdf':
            subprocess.run('npx --yes @marp-team/marp-cli@latest '+ marp_file+' --pdf',shell=True)
    
