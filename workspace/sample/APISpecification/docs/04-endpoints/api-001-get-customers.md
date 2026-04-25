# API-001 顧客一覧取得

## 概要

- メソッド: `GET`
- パス: `/customers`
- 説明: 顧客一覧を取得する

## リクエスト

`GET /customers?page=1&pageSize=20&sort=updatedAt&order=desc`

### クエリパラメータ

| パラメータ | 必須 | 型 | 説明 |
|------------|------|----|------|
| `page` | No | integer | ページ番号 |
| `pageSize` | No | integer | 取得件数 |
| `companyName` | No | string | 会社名の部分一致検索 |
| `updatedFrom` | No | string | 更新日時開始 |
| `updatedTo` | No | string | 更新日時終了 |

## レスポンス例

```json
{
  "items": [
    {
      "customerId": "CUS-000123",
      "customerName": "山田 太郎",
      "companyName": "サンプル商事株式会社",
      "email": "taro.yamada@example.com",
      "status": "active",
      "updatedAt": "2026-04-25T09:30:00+09:00"
    }
  ],
  "page": 1,
  "pageSize": 20,
  "totalCount": 1
}
```

## 備考

- レスポンス形式は `PagedCustomersResponse` を参照する
- 最大取得件数は `100` 件とする
