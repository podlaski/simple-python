# checking the existence of a file

import os

if os.path.isfile('test.xls'):
    print("Plik istnieje")
else:
    print("Plik nie istnieje")
