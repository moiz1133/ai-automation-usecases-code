import os
import json
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("sample_invoice.txt", "r") as f:
    invoice_text = f.read()

prompt = f"""
You are an AI system that extracts structured data from invoices.

Extract the following fields:
- vendor
- invoice_number
- invoice_date
- currency
- subtotal
- tax
- total

Rules:
- Return valid JSON only
- If a field is missing, set it to null

Invoice text:
{invoice_text}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

data = response.choices[0].message.content

parsed = json.loads(data)

with open("output.json", "w") as f:
    json.dump(parsed, f, indent=2)

print("Invoice processed successfully")