# データモデル

## Customer

| 項目名 | 型 | 必須 | 説明 |
|--------|----|------|------|
| `customerId` | string | Yes | 顧客ID |
| `customerName` | string | Yes | 顧客名 |
| `companyName` | string | Yes | 会社名 |
| `email` | string | Yes | メールアドレス |
| `phoneNumber` | string | No | 電話番号 |
| `status` | string | Yes | `active` / `inactive` |
| `address` | object | No | 住所情報 |
| `createdAt` | string | Yes | 作成日時 |
| `updatedAt` | string | Yes | 更新日時 |

## Address

| 項目名 | 型 | 必須 | 説明 |
|--------|----|------|------|
| `postalCode` | string | No | 郵便番号 |
| `prefecture` | string | No | 都道府県 |
| `city` | string | No | 市区町村 |
| `addressLine1` | string | No | 番地 |
| `addressLine2` | string | No | 建物名など |

## PagedCustomersResponse

| 項目名 | 型 | 必須 | 説明 |
|--------|----|------|------|
| `items` | array | Yes | 顧客一覧 |
| `page` | integer | Yes | 現在ページ |
| `pageSize` | integer | Yes | ページサイズ |
| `totalCount` | integer | Yes | 総件数 |

## ステータス値

| 値 | 説明 |
|----|------|
| `active` | 利用中 |
| `inactive` | 停止中 |
