# API概要

**API名:** 顧客管理API  
**バージョン:** v1  
**改訂日:** 2026-04-25  
**作成者:** システム開発株式会社

---

## 目的

本書は、顧客管理システムで利用する公開 API の仕様を定義し、フロントエンド開発者、バックエンド開発者、テスト担当者の共通理解を形成することを目的とする。

## 対象範囲

本仕様書で扱う機能は以下の通りです。

- 顧客情報の一覧取得
- 顧客情報の詳細取得
- 顧客情報の新規登録
- 顧客情報の更新
- 顧客情報の削除

## 基本情報

| 項目 | 内容 |
|------|------|
| プロトコル | HTTPS |
| データ形式 | JSON |
| 文字コード | UTF-8 |
| ベースURL | `https://api.example.com/v1` |
| 認証方式 | Bearer Token（JWT） |

## 利用者

- Webフロントエンド
- 管理者向け運用画面
- バッチ連携プログラム

## API構成

```plantuml
@startuml
actor Client as "API利用クライアント"
rectangle "顧客管理API" as API
database "Customer DB" as DB
rectangle "認証基盤" as Auth

Client --> API : HTTPS / JSON
API --> Auth : JWT検証
API --> DB : 顧客データ参照・更新
@enduml
```
