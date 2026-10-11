# MkDocs + PlantUML / Mermaid 日本語執筆環境

この README では、ドキュメントの「プレビューを開始」と「静的 HTML の出力（配布用）」の方法のみを説明します。

## サンプルプロジェクト

以下の 4 つの MkDocs サンプルプロジェクトを用意しています。

- `sample/APISpecification`: 顧客管理 API の仕様書
- `sample/ExternalDesignDocument`: 顧客管理システムの外部設計書
- `ToDoAppSample/APISpecification`: ToDo API の仕様書
- `ToDoAppSample/ExternalDesignDocument`: ToDo アプリの外部設計書

## 新しいプロジェクトを開始する場合

```bash
mkdocs new my-project
cd my-project
```

### 構成

- `mkdocs.yml`: MkDocsの設定（PlantUML・Mermaid対応済み）
- `docs/`: ドキュメントのソースファイル（Markdown）


## ビルド方法

### プレビューを開始

```bash
cd my-project
mkdocs serve -a 0.0.0.0:8000
```

ブラウザで `http://localhost:8000` にアクセスしてプレビューを確認する。

### 静的HTMLの出力方法（配布用）

```bash
cd my-project
mkdocs build
```

実行後に `site/` ディレクトリが生成されます。生成された `site/` ディレクトリをそのまま配布してください。PlantUML と Mermaid の図はビルド時に生成され、SVGファイルとして保存されます。

## 使用可能なプラグイン

- **Material for MkDocs**: 美しいテーマ
- **PlantUML Markdown**: ` ```plantuml ` ブロックで図を描画
- **Mermaid Markdown**: ` ```mermaid ` ブロックで図を描画。Docker 内のローカル Kroki/Mermaid コンテナで SVG 化するため、外部の描画サービスには接続しません。
- **i18n**: 日本語対応設定

> **オフライン利用**: 初回に Docker イメージを取得した後は、必要なイメージがローカルにあればネットワークを切断した状態でも Mermaid のプレビューと `mkdocs build` を実行できます。

## 大きな図を別タブで表示

4つのサンプルでは、Mermaid・PlantUMLの各図の下に「図を別タブで開く」リンクが自動で表示されます。Markdownへのリンクの追記は不要です。リンク先はSVG画像で、ブラウザーのズーム操作で拡大できます。初期表示の倍率はブラウザーによって異なります。

SVGはビルド時に `site/assets/diagrams/` に保存されます。配布時は `site/` 全体を含めてください。閲覧時に描画サーバーへ接続する必要はありません。
