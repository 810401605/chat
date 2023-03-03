import openai
import json

with open('api_credentials.json') as f:
    credentials = json.load(f)

openai.api_key = credentials["openai"]["api_key"]

def generate_response(prompt, model, max_tokens):
