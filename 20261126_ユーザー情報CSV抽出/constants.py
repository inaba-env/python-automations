"""固定の値。画面の XPath と CSV の形式はここだけに書く。

XPath は対象システムの画面を見て書き換える。
"""

from datetime import timedelta, timezone

JST = timezone(timedelta(hours=9))

# --- 画面 -------------------------------------------------------------
# 一覧・詳細の URL は、.env の LOGIN_URL と同じサイトの中のパス
USER_LIST_PATH = "/users"

# ログイン画面
LOGIN_ID_INPUT = "//input[@name='login_id']"
LOGIN_PASSWORD_INPUT = "//input[@name='password']"
LOGIN_SUBMIT_BUTTON = "//button[@type='submit']"
LOGGED_IN_MARK = "//a[contains(@href, 'logout')]"  # これが出たらログインできている

# 一覧画面
USER_LIST_ROW_LINK = "//table[@id='user-list']//tbody/tr/td[1]/a"
NEXT_PAGE_BUTTON = "//a[@rel='next']"

# 詳細画面（CSV の各列に入れる値の場所）
DETAIL_FIELDS = {
    "name": "//dt[text()='氏名']/following-sibling::dd[1]",
    "email": "//dt[text()='メールアドレス']/following-sibling::dd[1]",
    "department": "//dt[text()='所属']/following-sibling::dd[1]",
}

# 詳細ページを開くたびに待つ秒数。短くすると相手のシステムに負荷がかかる
WAIT_SECONDS = 1.0

# --- CSV --------------------------------------------------------------
# 見出し → UserDetail の項目名。並びがそのまま CSV の列順になる
CSV_COLUMNS = {
    "ユーザーID": "user_id",
    "氏名": "name",
    "メールアドレス": "email",
    "所属": "department",
}
CSV_ENCODING = "cp932"
