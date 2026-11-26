# python-automations

Python で書く自動化（単発の依頼・社内の作業）を、1 件 1 フォルダで置くリポジトリ。

## 使い方

このリポジトリはひな形。「Use this template」で自分の private リポジトリを作り、業務フォルダもそこで管理する（[docs/gitの使い方.md](docs/gitの使い方.md#リポジトリの持ち方)）。

## 環境を作る

`.venv` はルートに 1 つだけ作り、全業務で使う。

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
```

## 新しい業務を始める

```bash
cp -R _template 20261201_業務名
cd 20261201_業務名
cp .env.example .env    # 値を入れる
../.venv/bin/python impl.py
```

## ルール

| ドキュメント | 内容 |
|---|---|
| [docs/構成とファイルの役割.md](docs/構成とファイルの役割.md) | 構成・業務フォルダの名前の付け方・各ファイルの役割 |
| [docs/コードの書き方.md](docs/コードの書き方.md) | コードの書き方 |
| [docs/sdkの決まり.md](docs/sdkの決まり.md) | `sdk/` に置くもの・変えるときに守ること |
| [docs/ドキュメントの書き方.md](docs/ドキュメントの書き方.md) | ドキュメントとコメントの書き方 |
| [docs/gitの使い方.md](docs/gitの使い方.md) | リポジトリの持ち方・コミットの書き方・git に入れないもの |
