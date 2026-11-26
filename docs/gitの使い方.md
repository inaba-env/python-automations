# git の使い方

## リポジトリの持ち方

公開している python-automations はひな形で、業務フォルダを入れない。使う人は、ここから作った自分の private リポジトリに、業務フォルダもコミットして運用する。

## ひな形の更新を取り込む

`sdk/`・`_template/`・`docs/` の更新は、remote の `template`（ひな形）から取り込む。

```bash
git fetch template
git merge template/main --allow-unrelated-histories   # 初回だけ --allow-unrelated-histories が要る
```

## コミット

- Conventional Commits の形にする: `feat:` / `fix:` / `docs:` / `refactor:` / `chore:`
- コミットメッセージは日本語で書く
- 1 コミットに 1 つの変更にする

## git に入れないもの

private リポジトリでも、次のものは入れない。ルートの `.gitignore` で外している。`git add -f` で入れない。

- `.env`（認証情報）。リポジトリを見られる人に ID・パスワードが渡るため
- `output/`（実行結果。相手のシステムから取ったデータを含む）
- `.venv/`・`*.egg-info`・`__pycache__/`
