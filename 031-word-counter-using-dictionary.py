# word counter using dictionary

SPECIAL = '.,:;\'\"!@#$%^&*()?'

text = input('Add text: ')

for char in SPECIAL:
    text = text.lower().replace(char, ' ')

words = text.split()


# COUNTER - OPTION 1
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 0
    counter[word] += 1

# COUNTER - OPTION 2
# counter = {}
# for word in words:
#     if word in counter:
#         counter[word] += 1
#     else:
#         counter[word] = 1

# COUNTER - OPTION 3
# counter = {}
# for word in words:
#     counter[word] = counter.get(word, 0) + 1

for x, y in counter.items():
    print(x, y)
