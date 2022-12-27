# Anonymization of digits from the file example.txt

path = r'example.txt'
stream = open(path)
text = stream.read()
stream.close()

print('Text without anonimization: ', text)

for digit in '0123456789':
  text = text.replace(digit, '-')

print('Text with anonimization: ', text)
