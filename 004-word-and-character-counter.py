# Counter (characters, words, averages) 

text = input('Add text: ')
characters = len(text) # with whitespaces
characters2 = len(text.replace(' ','').replace('\t','').replace('\n','')) # without whitespaces
words = len(text.split())
average = characters/words # with whitespaces
average2 = characters2/words # without whitespaces

print(f"YOUR TEXT HAS\nCharacters with whitespaces: {characters}\nCharacters without whitespaces: {characters2} \nNumber of words: {words}\nAverage of characters per word (with whitespaces): {average}\nAverage of characters per word (without whitespaces): {average2}")
