# CLAUDE.md

Claude Code がこのリポジトリで作業するときに守ること。

## このリポジトリ

Python で書く自動化を 1 件 1 フォルダ（`YYYYMMDD_業務名/`）で置くリポジトリ。概要と始め方は [README.md](README.md)。

## 読むドキュメント

作業の前に、該当するものを読んでから進める。

| いつ | 読むもの |
|---|---|
| 業務フォルダを作る・ファイルを足すとき | [docs/structure.md](docs/structure.md) |
| コードを書く・直す・見直すとき | [docs/coding-rules.md](docs/coding-rules.md) |
| `sdk/` を触るとき | [docs/sdk.md](docs/sdk.md) |
| ドキュメント・コメントを書くとき | [docs/writing-docs.md](docs/writing-docs.md) |
| コミットするとき | [docs/git.md](docs/git.md) |

## 作業の進め方

### 新しい業務を作るとき

1. `_template/` をコピーして `YYYYMMDD_業務名/` を作る。日付は今日
2. 業務フォルダの `README.md` に、何をするか・流れ・実行方法・出力を書く
3. usecase の分け方と components のファイル名を決めてから、コードを書く

### 動かして確かめるとき

- 実行はルートの `.venv` を使う（業務フォルダの中で `../.venv/bin/python impl.py`）。業務フォルダに `.venv` を作らない
- お客様のシステムに対して全件を流さない。確かめるときは `--limit` で数件に絞る。全件の実行は、ユーザーが頼んだときだけする
- 相手のシステムで登録・更新・削除をする処理は、ユーザーの了承なしに実行しない
- `.env` の値（ID・パスワード）を会話に出さない・ログに出さない

### sdk を変えるとき

- 2 つ以上の業務で使うかを先に確かめる。1 つの業務でしか使わないなら、その業務の `components/` に置く
- 既存の引数を変える・消す変更はしない（[docs/sdk.md](docs/sdk.md)）

### ルールを足すとき

- ルールは `docs/` の内容に合うファイルに書く。このファイルに書くのは、Claude の作業の進め方だけ
- 同じことを 2 か所に書かない（[docs/writing-docs.md](docs/writing-docs.md#同じことは-1-か所に書く)）

## 回答の書き方

- 日本語で、結論から書く
- 動かして確かめたことと、確かめていないことを分けて書く
