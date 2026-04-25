# API-003 顧客新規登録

## 概要

| 項目 | 内容 |
|------|------|
| メソッド | `POST` |
| パス | `/customers` |
| 説明 | 顧客を新規登録する |

## リクエストボディ

```json
{
  "customerName": "山田 太郎",
  "companyName": "サンプル商事株式会社",
  "email": "taro.yamada@example.com",
  "phoneNumber": "03-1234-5678",
  "status": "active",
  "address": {
    "postalCode": "1000001",
    "prefecture": "東京都",
    "city": "千代田区",
    "addressLine1": "千代田1-1-1"
  }
}
```

## バリデーション

- `customerName` は必須
- `companyName` は必須
- `email` はメールアドレス形式で必須
- `status` は `active` `inactive` のみ指定可能

## レスポンス例

```json
{
  "customerId": "CUS-000123",
  "message": "Customer created successfully."
}
```

## エラー

| ステータス | 条件 |
|------------|------|
| `409 Conflict` | メールアドレスが重複している場合 |
