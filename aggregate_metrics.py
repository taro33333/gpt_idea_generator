import json

with open("tweets.json", encoding="utf-8") as f:
    data = json.load(f)

tweets = data.get("data", [])

def score(t):
    m = t["public_metrics"]
    return m["like_count"] + 2*m["retweet_count"] + 2*m["reply_count"] + 3*m["quote_count"]

top = sorted(tweets, key=score, reverse=True)[:30]

with open("top30.json", "w", encoding="utf-8") as f:
    json.dump(top, f, ensure_ascii=False, indent=2)

print("✓ top30.json saved")
