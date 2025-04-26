# GPT Idea Generator (Twitter → GPT)


## 構成
```
.
├── fetch_tweets.py
├── aggregate_metrics.py
├── call_openai.py
├── system_prompt.txt
├── user_prompt_template.txt
├── requirements.txt
└── .github/workflows/daily-idea-generator.yml
```

## セットアップ

1. このリポジトリを GitHub に作成し、ファイルを push。
2. **Settings → Secrets and variables → Actions → New repository secret** で以下を登録  
   - `OPENAI_API_KEY`  
   - `TWITTER_BEARER_TOKEN`  
   - `TWITTER_USER_ID` (数値 ID)  
   - `FOLLOWER_COUNT` (任意、なければ 0)
3. Actions タブで `daily-idea-generator` ワークフローがスケジュールされます。手動で `Run workflow` も可能。

> 成功すると `ideas_YYYY-MM-DD.json` がコミットされ、Ideas が Notion 連携や Zapier で他ツールへ飛ばせます。
