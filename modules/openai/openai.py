import os
import openai

openai_key = os.environ.get("OPENAI_KEY")
openai.api_key = openai_key

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=100)

print(response)

print(response["choices"][0]["text"])
