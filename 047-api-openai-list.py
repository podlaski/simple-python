# Simple script using OPENAI API for many queries

import openai

openai.api_key = 'YOUR-API'

queries = ['Who is the president of Poland?', 'Who is the president of USA?']

def answer_generate(query):
    response = openai.Completion.create(model="text-davinci-003", prompt=query, temperature=0, max_tokens=500)
    return response

answers = []

for query in queries:
    answer = answer_generate(query)
    answer_text = answer['choices'][0]['text'].strip()
    answers.append(answer_text)

for answer in answers:
    print(answer)
