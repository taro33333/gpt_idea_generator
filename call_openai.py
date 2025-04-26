import os, json, datetime, openai

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise RuntimeError("Please set OPENAI_API_KEY environment variable.")

with open("system_prompt.txt", encoding="utf-8") as f:
    system_prompt = f.read()
with open("user_prompt_template.txt", encoding="utf-8") as f:
    template = f.read()
with open("top30.json", encoding="utf-8") as f:
    tweets_json = f.read()

followers = os.getenv("FOLLOWER_COUNT", "0")
user_prompt = template.format(followers=followers, tweets_json=tweets_json)

resp = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": system_prompt},
              {"role": "user", "content": user_prompt}],
    temperature=0.9,
    max_tokens=800
)

ideas_json = resp.choices[0].message.content
ts = datetime.datetime.now().strftime("%Y-%m-%d")
out_path = f"ideas_{ts}.json"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(ideas_json)

print(f"✓ {out_path} saved")
