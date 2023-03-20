# checking for the existence of a file or directory

import os

if os.path.exists('test'):
    print("Plik istnieje")
else:
    print("Plik nie istnieje")
