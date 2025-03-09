__author__ = 'Benjamin Zwettler'

import os
import pathlib
import shutil
import sys
from pathlib import Path

"""ein adminscript das jpg files aus einen src ordner in eine ordnerstrucktur in dest überträgt"""

p_src = Path(input("Bitte src Pfad eingeben: "))
p_des = Path(input("Bitte des Pfad eingeben: "))
if not p_des.is_dir() or not p_src.is_dir():
    print("Invalid directory path!")
    sys.exit()

for file in p_src.glob(f'*{"jpg"}'):
    if file.name.split('_')[0].__len__() != 8 or not file.name.split('_')[0].isdigit():
        print("is not a real file" + str(file))
        continue
    print(file)
    year = file.name.split('_')[0][:4]
    month = file.name.split('_')[0][4:6]
    day = file.name.split('_')[0][6:]

    path = p_des / year / month / day
    os.makedirs(path, exist_ok=True)
    shutil.copy((file), (path / file.name))



