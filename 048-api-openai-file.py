# Simple script using OPENAI API for many queries (saving in txt file)

import openai

openai.api_key = 'YOUR-API'

queries = ['Who is the president of Poland?', 'Who is the president of USA?']

def answer_generate(query):
    response = openai.Completion.create(model="text-ada-001", prompt=query, temperature=0, max_tokens=500)
    return response

answers = []
number = 0

for query in queries:
    answer = answer_generate(query)
    answer_text = answer['choices'][0]['text'].strip()
    answers.append(answer_text)
    number += 1
    with open(f'ai-{number}.txt', 'w') as ai_file:
        ai_file.write(answer_text)


for answer in answers:
    print(answer)
