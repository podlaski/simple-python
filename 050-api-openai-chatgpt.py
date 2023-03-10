import openai

openai.api_key = 'YOUR_API_KEY'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {'role': 'user', 'content': 'Napisz jedno zdanie na temat AI.'},
    ]
)

print(response)

print(response['choices'][0]['message']['content'])
