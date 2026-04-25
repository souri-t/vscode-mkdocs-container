# API-004 顧客更新

## 概要

| 項目 | 内容 |
|------|------|
| メソッド | `PUT` |
| パス | `/customers/{customerId}` |
| 説明 | 顧客情報を更新する |

## パスパラメータ

| パラメータ | 必須 | 型 | 説明 |
|------------|------|----|------|
| `customerId` | Yes | string | 更新対象の顧客ID |

## リクエスト例

`PUT /customers/CUS-000123`

```json
{
  "customerName": "山田 太郎",
  "companyName": "サンプル商事株式会社",
  "email": "taro.yamada+updated@example.com",
  "status": "active"
}
```

## 更新ルール

- 未指定項目は既存値を維持する
- `status` は `active` `inactive` のみ指定可能

## レスポンス例

```json
{
  "customerId": "CUS-000123",
  "message": "Customer updated successfully."
}
```

## エラー

| ステータス | 条件 |
|------------|------|
| `409 Conflict` | メールアドレスが重複している場合 |
