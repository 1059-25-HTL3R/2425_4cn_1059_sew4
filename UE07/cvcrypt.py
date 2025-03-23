__author__ = "Benjamin Zwettler"

import argparse
import os
from BetterKasiski import Ceaser, Vigenere

def process_file(input_file: str, output_file: str, chifre: str, key,encrypt: bool, decrypt: bool, verbose: bool):
    if not os.path.exists(input_file):
        raise FileNotFoundError

    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')

    if verbose:
        type: str
        chifrestring: str
        if encrypt:
            type = "encrypting"
        else:
            type = "decrypting"
        if chifre in ["c", "ceaser"]:
            chifrestring = "ceaser"
        else:
            chifrestring = "vigenere"

        print(f"{type} {chifrestring} with key ({key}) form file {input_file} into file {output_file}")


    if chifre in ["ceaser", "c"]:
        if len(key) >1:
            raise ValueError("ceaser does only support key a-z")
        ceaser = Ceaser(key)

        if decrypt:
            outfile.write(ceaser.decrypt(infile.read()))
        elif encrypt:
            outfile.write(ceaser.encrypt(infile.read()))
    elif chifre in ["vigenere", "v"]:
        vigenere = Vigenere(key)

        if decrypt:
            outfile.write(vigenere.decrypt(infile.read()))
        elif encrypt:
            outfile.write(vigenere.encrypt(infile.read()))




def main():
    parser = argparse.ArgumentParser(description="cvcrypt.py parser to encrypt files")

    parser.add_argument("chifre", help="which encrypting algoryth should be used",
                        choices=["ceaser", "c", "vigenere", "v"])
    parser.add_argument("infile", help="Path to the file you want to encrypt.")
    parser.add_argument("outfile", help="Path where the encrypted file should be saved.")
    parser.add_argument("-k", "--key", help="key for encryption", type=str, default="a", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true", help="verschlüsseln")
    group.add_argument("-d", "--decrypt", action="store_true", help="entschlüsseln")
    parser.add_argument("-v", "--verbose", action="store_true", help="Mehr Informationen anzeigen")  # Schalter

    args = parser.parse_args()

    process_file(args.infile, args.outfile, args.chifre, args.key,args.encrypt, args.decrypt, args.verbose)


if __name__ == "__main__":
    main()






