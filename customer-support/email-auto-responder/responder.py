import os
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("sample_email.txt", "r") as f:
    email_text = f.read()

prompt = f"""
You are an AI customer support assistant.

Your task:
- Draft a professional, polite email reply
- Be clear and concise
- Do not make up information
- If information is missing, acknowledge it politely

Return the response as JSON with:
- reply_text
- tone (one of: polite, apologetic, neutral)
- confidence (0.0 to 1.0)

Incoming email:
{email_text}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

result = response.choices[0].message.content
parsed = json.loads(result)

with open("output.json", "w") as f:
    json.dump(parsed, f, indent=2)

print("Draft reply generated")
