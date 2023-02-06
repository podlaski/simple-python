# Simple script using OPENAI API for one query

import openai

openai.api_key = 'YOUR-KEY'

input_prompt = input('Add your prompt: ')

response = openai.Completion.create(model="text-davinci-003", prompt=input_prompt, temperature=1, max_tokens=1000)

result = response['choices'][0]['text']

print(result)
