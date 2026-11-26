# ユーザー情報CSV抽出

対象のシステムにログインし、ユーザー一覧から全ユーザー（約 2000 人）の詳細ページを開いて情報を抜き出し、決まった形式の CSV にする。

## 流れ

1. 一覧をページ送りして、全ユーザーの ID と詳細ページの URL を集める
2. 詳細ページを 1 件ずつ開いて情報を抜く
3. 決まった形式で CSV に書き出す → `output/users_YYYYMMDD.csv`

詳細を抜けなかったユーザーは CSV に入らない。終わりに、件数と ID をログに出す。

## 実行方法

環境はルートの `.venv` を使う（作り方はルートの README）。

```bash
cp .env.example .env    # ログイン先・ID・パスワードを入れる

../.venv/bin/python impl.py --limit 5 --no-headless   # 試しに 5 件、画面を見ながら
../.venv/bin/python impl.py                           # 全件
```

| 引数 | 意味 |
|---|---|
| `--limit N` | 詳細を抜くのを N 件で止める |
| `--no-headless` | Chrome の画面を出して動かす |

## 直すところ

画面の XPath・CSV の列は `constants.py` にまとめている。画面や CSV の形式が変わったら、まずここを直す。
