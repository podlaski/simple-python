# Open and read file example.txt

path = r'example.txt'
stream = open(path)
text = stream.read()
stream.close()

print(text)
