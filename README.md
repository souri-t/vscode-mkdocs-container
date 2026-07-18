# MkDocs 日本語執筆環境

このプロジェクトは、VS CodeのDevContainerを使用して、日本語対応のMkDocsドキュメント執筆環境を即座に構築するためのテンプレートです。

## セットアップ方法

1.  このディレクトリをVS Codeで開きます。
2.  「Reopen in Container」のポップアップが表示されたら選択するか、コマンドパレットから `Dev Containers: Reopen in Container` を実行します。
3.  コンテナの起動完了後、ターミナルで以下のコマンドを実行してプレビューを開始します。
    ```bash
    mkdocs serve -a 0.0.0.0:8000
    ```
4.  ブラウザで `http://localhost:8000` にアクセスします。

## 構成

- `.devcontainer/`: VS Codeの開発コンテナ設定
- `mkdocs.yml`: MkDocsの設定（PlantUML・Mermaid対応済み）
- `docs/`: ドキュメントのソースファイル（Markdown）

## サンプル

`workspace/` には、以下の 4 つの MkDocs サンプルがあります。

- `sample/APISpecification`: 顧客管理 API の仕様書
- `sample/ExternalDesignDocument`: 顧客管理システムの外部設計書
- `ToDoAppSample/APISpecification`: ToDo API の仕様書
- `ToDoAppSample/ExternalDesignDocument`: ToDo アプリの外部設計書

## 使用可能なプラグイン

- **Material for MkDocs**: 美しいテーマ
- **PlantUML Markdown**: ` ```plantuml ` ブロックで図を描画
- **Mermaid Markdown**: ` ```mermaid ` ブロックで図を描画（ローカルコンテナでSVG化）
- **Drawio**: Draw.ioの図をMarkdown内で描画
- **MathJax**: 数式の描画
- **i18n**: 日本語対応設定

## 静的HTMLの出力方法（配布用）

サーバーを起動せずに、配布用の静的HTMLファイル一式を出力するには以下のコマンドを実行します。

```bash
mkdocs build
```

実行後、プロジェクト直下に `site/` ディレクトリが生成されます。このディレクトリ内のファイル一式をWebサーバーにアップロードするか、そのまま配布することで閲覧が可能です。

> **注意**: PlantUML と Mermaid の図はビルド時に生成・埋め込みされるため、`site/` ディレクトリをそのまま配布するだけで図も表示されます。Mermaid の描画は Docker 内のローカル Kroki/Mermaid コンテナだけを使用し、外部の描画サービスには接続しません。初回にイメージを取得した後は、必要なイメージがローカルにあればオフラインでも利用できます。
