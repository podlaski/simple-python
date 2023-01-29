names = ['smog', 'type', 'nice']

# filenames = []
# for name in names:
#     filenames.append(name + '.txt')
# print(filenames)

# List comprehension
filenames = [name + '.txt' for name in names]
print(filenames)
