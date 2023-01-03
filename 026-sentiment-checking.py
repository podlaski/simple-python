import glob

print("The system is learning. Please wait...")


# Positive comments - add sample positive comments to the indicated path (one comment in one txt file)

pos_files = glob.glob('example-pos\\*.txt')
pos_comments = []

for file in pos_files:
    with open(file, 'r', encoding='utf-8') as stream:
        text = stream.read()
        words = text.lower().replace('<br />', ' ').split()
        pos_comments.append(words)


# Negative comments - add sample negative comments to the indicated path (one comment in one txt file)

neg_files = glob.glob('example-neg/*.txt')
neg_comments = []

for file in neg_files:
    with open(file, 'r', encoding='utf-8') as stream:
        text = stream.read()
        words = text.lower().split()
        neg_comments.append(words)


# Sentence

sentence = input('Add sentence: ')
words = sentence.lower().split()

print(f'\n{words}\n')


# Sentiment

sentiment = 0

for word in words:
    positive = 0
    negative = 0
    for comment in pos_comments:
        if word in comment:
            positive += 1
    for comment in neg_comments:
        if word in comment:
            negative += 1
    total = positive + negative
    if total != 0:
        word_sentiment = (positive - negative) / total
    else:
        word_sentiment = 0.0

    print(word, word_sentiment)

    sentiment += word_sentiment

sentiment /= len(words)


# Result

if sentiment > 0:
    check = 'positive'
else:
    check = 'negative'

print('\nThis sentence has a', check, 'sentiment:', sentiment, '\n')
