import glob
import os

print(glob.glob('*'))
os.rename('example.txt', 'example.bak')
print('-')
print(glob.glob('*'))
