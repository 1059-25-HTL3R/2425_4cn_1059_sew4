__author__ = "Benjamin Zwettler"

import argparse
import pathlib
import UE02.BetterKasiski as Kasiski


parser = argparse.ArgumentParser(description="cvcrypt.py parser to encrypt files")


parser.add_argument("chifre", help="which encrypting algoryth should be used", type=str)
parser.add_argument("src", "srcPath", help="Path to the file you want to encrypt.")
parser.add_argument("dest","destPath", help="Path where the encrypted file should be saved.")
parser.add_argument("-k", "--key", help="key for encryption", type=str, default="a")
parser.add_argument("-a", "--alter", type=int, help="Dein Alter")  # Optionales Argument
parser.add_argument("-v", "--verbose", action="store_true", help="Mehr Informationen anzeigen")  # Schalter

args = parser.parse_args()







