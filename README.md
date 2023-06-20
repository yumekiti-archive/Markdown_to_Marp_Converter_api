# Markdown_to_Marp_Converter_api

このアプリケーションは、FastAPIとMarpを使用してMarkdownをMarp形式に変換するためのシンプルなWebサービスです。

## 概要

FastAPIを使用してRESTfulなエンドポイントを作成し、Markdownコンテンツを受け取り、それをMarpに変換して返します。Marpは、プレゼンテーション用のMarkdown形式を変換するためのパッケージです。

アプリケーションは、MVC（Model-View-Controller）パターンを採用しています。モデルはMarkdownデータ、コントローラはリクエストを処理しレスポンスを返し、サービスはMarkdownをMarpに変換します。

## インストールと実行

```bash
# リポジトリをクローンします
git clone https://github.com/your-username/fastapi-markdown-to-marp.git

# プロジェクトディレクトリに移動します
cd fastapi-markdown-to-marp

# 依存関係をインストールします
pip install -r requirements.txt

# アプリケーションを実行します
uvicorn main:app --reload
```

アプリケーションは、`http://localhost:8000`で実行されます。

## APIドキュメント

APIのエンドポイントとペイロードの詳細については、Swagger UIを使用してAPIドキュメントを参照してください。アプリケーションを実行している状態で、`http://localhost:8000/docs`にアクセスしてください。

## 使用例

以下は、cURLを使用してAPIエンドポイントにリクエストを送信する例です。

```
curl -X POST -H "Content-Type: application/json" -d '{"content": "# Hello, Marp!"}' http://localhost:8000/markdown-to-marp
```

レスポンス:

```
{
  "marp_content": "<h1>Hello, Marp!</h1>"
}
```

## ライセンス

このプロジェクトは、MITライセンスのもとで提供されています。詳細については、[LICENSE](https://chat.openai.com/c/LICENSE)ファイルを参照してください。