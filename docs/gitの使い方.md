# git の使い方

## コミット

- Conventional Commits の形にする: `feat:` / `fix:` / `docs:` / `refactor:` / `chore:`
- コミットメッセージは日本語で書く
- 1 コミットに 1 つの変更にする。sdk の変更とテンプレートの変更は、別のコミットに分ける

## git に入れないもの

このリポジトリは公開している。次のものは入れない。

- 業務フォルダ（`YYYYMMDD_業務名/`）。依頼先のシステムの URL・画面の作り・依頼元が入る
- `.env`（認証情報）
- `output/`（実行結果。相手のシステムから取ったデータを含む）
- `.venv/`・`*.egg-info`・`__pycache__/`

どれもルートの `.gitignore` で外している。`git add -f` で入れない。

`sdk/`・`_template/`・`docs/` にも、依頼先の会社名・システムの URL・画面の XPath を書かない。例は `example.com` のような架空のものにする。
