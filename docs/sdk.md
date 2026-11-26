# sdk の決まり

`sdk/` は、2 つ以上の業務で使う部品の置き場。業務フォルダからは `from sdk.webdriver import WebDriverSession` のように import する。

## 置くもの・置かないもの

- 置くのは、2 つ以上の業務で使う部品だけ。1 つの業務でしか使わないものは、その業務の `components/` に置く
- 業務に固有の値（URL・XPath・列名）は置かない
- 新しい部品が要るライブラリは、ルートの `pyproject.toml` の `dependencies` に足す

## 変えるときに守ること

- 引数を変えたり消したりしない。足すだけにする。古い業務フォルダも同じ sdk を使っており、変えると動かなくなるため
- 業務フォルダの使い方を壊す変更がどうしても要るときは、新しい関数・クラスとして足す

## WebDriverSession

- 要素は既定で XPath で指定する
- 操作のメソッド（`click`・`send_keys`・`get_text` など）は、要素が現れるまで待ってから操作する。業務側で `time.sleep` を入れて待たない
