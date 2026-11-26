"""部品。usecases から呼ばれる。1 ファイル 1 役割。

| ファイル | 画面・ファイルの読み書き | 役割 |
|---|---|---|
| login_page.py | あり（画面） | ログインする |
| user_list_page.py | あり（画面） | 一覧の 1 ページからユーザーを読む・次のページへ進む |
| user_detail_page.py | あり（画面） | 詳細ページを開いて値を抜く |
| csv_rows.py | なし | UserDetail を CSV の 1 行にする |

ブラウザ（WebDriverSession）は第 1 引数で受け取り、部品の中で起動しない。
"""
