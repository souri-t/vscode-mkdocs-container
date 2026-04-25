# 共通仕様

## リクエスト共通ルール

| 項目 | 仕様 |
|------|------|
| HTTPメソッド | `GET` `POST` `PUT` `DELETE` |
| Content-Type | `application/json` |
| Accept | `application/json` |
| 日時形式 | ISO 8601（例: `2026-04-25T09:30:00+09:00`） |
| 真偽値 | `true` / `false` |

## 共通ヘッダー

| ヘッダー名 | 必須 | 内容 |
|------------|------|------|
| `Authorization` | Yes | `Bearer <JWT>` |
| `X-Request-Id` | No | トレース用リクエストID |
| `Content-Type` | POST/PUT時にYes | `application/json` |

## ページネーション

一覧取得 API はクエリパラメータでページングを行います。

| パラメータ | 必須 | 説明 | 初期値 |
|------------|------|------|--------|
| `page` | No | 1始まりのページ番号 | `1` |
| `pageSize` | No | 1ページあたりの件数（最大100） | `20` |
| `sort` | No | ソート対象項目 | `updatedAt` |
| `order` | No | `asc` または `desc` | `desc` |

## 命名規則

- JSON のプロパティ名は lower camel case とする
- リソース名は複数形を使用する
- エンドポイントのパスは小文字とハイフンを使用しない

## レスポンス共通方針

- 正常系は HTTP ステータス 2xx を返す
- 異常系は HTTP ステータス 4xx / 5xx を返す
- エラー時は `code` `message` `details` を含む JSON を返す
