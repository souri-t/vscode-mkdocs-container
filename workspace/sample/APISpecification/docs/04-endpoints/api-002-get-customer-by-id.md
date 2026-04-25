# API-002 顧客詳細取得

## 概要

- メソッド: `GET`
- パス: `/customers/{customerId}`
- 説明: 顧客詳細を取得する

## パスパラメータ

| パラメータ | 必須 | 型 | 説明 |
|------------|------|----|------|
| `customerId` | Yes | string | 顧客ID |

## リクエスト例

`GET /customers/CUS-000123`

## レスポンス例

```json
{
  "customerId": "CUS-000123",
  "customerName": "山田 太郎",
  "companyName": "サンプル商事株式会社",
  "email": "taro.yamada@example.com",
  "phoneNumber": "03-1234-5678",
  "status": "active",
  "address": {
    "postalCode": "1000001",
    "prefecture": "東京都",
    "city": "千代田区",
    "addressLine1": "千代田1-1-1",
    "addressLine2": "サンプルビル5F"
  },
  "createdAt": "2026-04-01T10:00:00+09:00",
  "updatedAt": "2026-04-25T09:30:00+09:00"
}
```

## エラー

- 該当顧客が存在しない場合は `404 Not Found`
