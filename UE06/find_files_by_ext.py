__author__ = 'benjamin Zwettler'

import sys
from pathlib import Path

"""ein script das alle files rekursiv vom angegebenen startpunkt mit einer bestimmten ändung findet und deren aabsoluten pfad auf der konsole ausgibt"""
sufix = input("Suffix nach dem zu suchen ist: ")
p = Path(input("Bitte Pfad eingeben: "))
if not p.is_dir():
    print("Invalid directory path!")
    sys.exit()

for file in p.rglob(f'*{sufix}'):
        print(file.resolve())