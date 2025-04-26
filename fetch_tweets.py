import os, httpx, json, datetime

BEARER = os.getenv("TWITTER_BEARER_TOKEN")
USER_ID = os.getenv("TWITTER_USER_ID")
if not BEARER or not USER_ID:
    raise RuntimeError("Environment variables TWITTER_BEARER_TOKEN and TWITTER_USER_ID are required.")

since = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
url = f"https://api.twitter.com/2/users/{USER_ID}/tweets"
params = {
    "max_results": 100,
    "start_time": since,
    "tweet.fields": "created_at,public_metrics,text"
}
headers = {"Authorization": f"Bearer {BEARER}"}

resp = httpx.get(url, params=params, headers=headers, timeout=30)
if resp.status_code != 200:
    print(resp.text)
resp.raise_for_status()

with open("tweets.json", "w", encoding="utf-8") as f:
    json.dump(resp.json(), f, ensure_ascii=False, indent=2)

print("✓ tweets.json saved")
