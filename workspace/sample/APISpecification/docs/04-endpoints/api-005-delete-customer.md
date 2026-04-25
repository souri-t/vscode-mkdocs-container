# API-005 顧客削除

## 概要

- メソッド: `DELETE`
- パス: `/customers/{customerId}`
- 説明: 顧客を削除する

## パスパラメータ

| パラメータ | 必須 | 型 | 説明 |
|------------|------|----|------|
| `customerId` | Yes | string | 削除対象の顧客ID |

## リクエスト例

`DELETE /customers/CUS-000123`

## レスポンス

- ステータスコード: `204 No Content`
- レスポンスボディ: なし

## エラー

- 該当顧客が存在しない場合は `404 Not Found`
- 削除権限がない場合は `403 Forbidden`
