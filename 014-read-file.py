# Open and read file example.txt

path = r'test\example.txt'
stream = open(path)
text = stream.read()
stream.close()

print(text)
