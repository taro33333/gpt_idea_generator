import os
import datetime
import httpx
import time

# --- 事前にここを設定 ---
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")  # API認証用
POST_TEXT = "おはようございます☀️\n今日もコツコツやっていきましょう！ #エンジニア #朝活"

# --- ユーザーIDをセット（自分の数値ID） ---
USER_ID = os.getenv("TWITTER_USER_ID")  # 例: "1653145423919589376"

# --- 投稿処理 ---
def post_tweet(text):
    if not BEARER_TOKEN or not USER_ID:
        raise RuntimeError("TWITTER_BEARER_TOKENとTWITTER_USER_IDを環境変数に設定してください。")

    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"text": text}

    resp = httpx.post(url, headers=headers, json=payload, timeout=30)
    if resp.status_code == 201:
        print("✅ 投稿成功:", resp.json()["data"]["id"])
    else:
        print("❌ 投稿失敗:", resp.text)
        resp.raise_for_status()

if __name__ == "__main__":
    try:
        post_tweet(POST_TEXT)
    except Exception as e:
        print("エラー:", e)
