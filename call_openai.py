import os, json, datetime, openai

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Please set OPENAI_API_KEY environment variable.")

# 直接プロンプトを組み立てる
system_prompt = """
あなたはSNSグロースの専門家です。エンジニア向けに、次にバズりそうなツイート・スレッド・note・YouTube Shortsのネタを考えてください。
出力はJSON配列で10件、各要素は以下形式にしてください。
- "idea_title": 35字以内のフックタイトル
- "outline": 120字以内の要約
- "recommended_format": "tweet" | "thread" | "note" | "shorts"
- "hooks": 3つの短いキャッチコピー
- "hashtags": 2-4個 (ハッシュタグ記号込み)
"""

user_prompt = """
対象ジャンル: エンジニア、プログラミング、副業、AI活用、キャリア
読者層: 20代後半〜30代前半のエンジニア志望または現役エンジニア
トーン: ポジティブ、実用的、具体的
日本語で出力してください。
"""

# GPT呼び出し
resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.9,
    max_tokens=1000,
)

# 結果を保存
ideas_json = resp.choices[0].message.content
ts = datetime.datetime.now().strftime("%Y-%m-%d")
out_path = f"ideas_{ts}.json"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(ideas_json)

print(f"✓ {out_path} saved")
