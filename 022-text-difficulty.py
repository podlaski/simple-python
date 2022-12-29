# Text difficulty index

SPECIAL = '.,:;\'\"!@#$%^&*()?'

text = input('Add your text: ')

for char in SPECIAL:
    text = text.replace(char, ' ')

words = text.split()
numbers = 0

for word in words:
    if word.isnumeric():
        numbers += 1

word_counter = len(words)
text_difficulty = numbers / word_counter * 100

print(f'Your text has {word_counter} words. {numbers} of them are numbers. The text difficulty index is {text_difficulty} %.')
