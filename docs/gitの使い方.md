# git の使い方

## リポジトリの持ち方

公開している python-automations はひな形で、業務フォルダを入れない。使う人は、ここから作った自分の private リポジトリに、業務フォルダもコミットして運用する。

## ひな形の更新を取り込む

`sdk/`・`_template/`・`docs/` の更新は、remote の `template`（ひな形）から取り込む。

```bash
git fetch template
git merge template/main --allow-unrelated-histories   # 初回だけ --allow-unrelated-histories が要る
```

取り込んだかどうかは、`template/main` のコミットが自分のブランチの履歴に入っているかで判断する。ファイルを手でコピーしたり squash でマージしたりすると、取り込んでいないと判断される。`git merge` で取り込む。

`.githooks/` のフックが、次のときに知らせる（有効にするには `git config core.hooksPath .githooks`）。

| いつ | フック | すること |
|---|---|---|
| `git push` の前 | `pre-push` | `template` を fetch し、取り込んでいない更新があれば一覧を出して push を止める |
| `git pull` のあと | `post-merge` | 取り込んでいない更新があれば一覧を出す。止めはしない |

急ぎで取り込まずに push するときは `git push --no-verify` を使う。

ひな形を更新する人は、取り込んだあとにメンバーがすることを、コミットメッセージに書く（例: `pip install -e .` をやり直す）。フックが出す一覧は、このコミットメッセージ。

## コミット

- Conventional Commits の形にする: `feat:` / `fix:` / `docs:` / `refactor:` / `chore:`
- コミットメッセージは日本語で書く
- 1 コミットに 1 つの変更にする

## git に入れないもの

private リポジトリでも、次のものは入れない。ルートの `.gitignore` で外している。`git add -f` で入れない。

- `.env`（認証情報）。リポジトリを見られる人に ID・パスワードが渡るため
- `output/`（実行結果。相手のシステムから取ったデータを含む）
- `.venv/`・`*.egg-info`・`__pycache__/`
