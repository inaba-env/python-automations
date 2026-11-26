# コードの書き方

## 層ごとに守ること

### impl.py

- `.env` を読むのは `impl.py` だけにする。usecases・components には値を引数で渡す。どこで認証情報を読んでいるかを 1 か所で追えるようにするため
- ブラウザ（`WebDriverSession`）・HTTP クライアントなど外とつなぐものは `impl.py` で作り、usecases に渡す。usecases・components の中で作らない
- 実行時刻は `datetime.now(JST)` で 1 回だけ取り、出力ファイル名などで使い回す。`JST` は `constants.py` に置く。タイムゾーンなしの `datetime.now()` は実行する PC の設定で値が変わる
- 入口の関数名は `execute`

### usecases/

- 1 つの流れを `{流れの名前}UseCase` クラスにし、公開するメソッドは `execute` だけにする
- クラスは `usecases/__init__.py` で公開し、`impl.py` はクラス名で import する
- ブラウザ・保存先・logger はコンストラクタで受け取る
- 画面やファイルを直接読み書きしない。components の関数を呼ぶ

### components/

- 1 ファイル 1 役割
- 画面やファイルを読み書きする部品は、ファイル名で分かるようにする（`*_page.py`・`*_store.py`・`*_writer.py`）。読み書きしない部品（変換・判定）と見分けられるようにするため
- ブラウザなどは第 1 引数で受け取る
- 「ログインは 1 回だけ」のような流れの決まりは、components ではなく usecases が持つ

### constants.py

- 画面の XPath・URL・出力の列順と文字コードは `constants.py` に集める。画面や出力の形式が変わったときに直す場所を 1 か所にするため

## 名前

- 変数・関数・クラス・ファイル・フォルダの名前は英語にする。業務フォルダ名だけは日本語でよい（[structure.md](structure.md#名前の付け方)）
- CSV の列名・画面の項目名など業務の日本語は、名前にせず、文字列のデータとして持つ。英語の名前との対応は `constants.py` に 1 か所で置く

```python
# 良い例
CSV_COLUMNS = {"氏名": "name", "メールアドレス": "email"}

# 悪い例
@dataclass
class UserDetail:
    氏名: str
```

## 失敗の扱い

- 例外を握り潰さない。`except` で受けたら、続けるか止めるかを決め、続けるときは logger の `warning` で何が失敗したかを出す
- 件数の多い処理で 1 件の失敗のたびに全体を止めないときは、失敗した件を記録して続け、最後に件数と対象を `warning` で出す
- ただし続けて何件も失敗したら止める。ログインが切れたときなど、残り全件を失敗のまま流さないため
- `except Exception` は `KeyboardInterrupt`（Ctrl+C）を受けないので、手で止める操作は妨げない。`except BaseException` や裸の `except:` は使わない

## 件数の多い処理

- 1 件済むごとに結果をファイルに追記し、もう一度実行したら済んだ件を飛ばして続きから進める。途中で止まっても最初からやり直さないため
- `--limit N` で件数を絞って試せるようにする
- 相手のシステムに続けてアクセスするときは、1 件ごとに待ち時間を入れる。待ち時間は `constants.py` に置く

## コメントと docstring

- 日本語で書く
- 今の動きとその理由を書く。前の動きや変えた経緯は書かない（[writing-docs.md](writing-docs.md)）
