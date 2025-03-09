__author__ = 'Benjamin Zwettler'

import pathlib

import os
from pathlib import Path

p = Path(input("Bitte Pfad eingeben: "))
print(p.name)
print(p.stem)
print(p.suffix)
print(p.anchor)
if p.parent:
    print(p.parent)
else:
    print("es gibt keinen übergeordneten")

if p.parent.parent:
    print(p.parent.parent)
else:
    print("es gibt keinen übergeordneten ordner")
