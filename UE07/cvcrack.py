__author__ = "Benjamin Zwettler"

import argparse
import os
from BetterKasiski import Ceaser, Kasinski

def process_file(input_file: str, output_file: str, chifre: str, verbose: bool, n:int):
    """"
    Processes the args
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError

    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')

    if verbose:
        print()



    if chifre in ["ceaser", "c"]:
        ceaser = Ceaser()
        outfile.write(str(ceaser.crack(infile.read())))
    elif chifre in ["vigenere", "v"]:
        kasinski = Kasinski(infile.read())
        outfile.write(kasinski.crack_key())




def main():
    parser = argparse.ArgumentParser(description="cvcrypt.py parser to encrypt files")

    parser.add_argument("chifre", help="which encrypting algorythm should be used",
                        choices=["ceaser", "c", "vigenere", "v"])
    parser.add_argument("infile", help="Path to the file you want to encrypt.")
    parser.add_argument("outfile", help="Path where the encrypted file should be saved.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Mehr Informationen anzeigen")  # Schalter
    parser.add_argument("-n", "--number", help="how many possible keys are to be calculated",type=int)  # Schalter

    args = parser.parse_args()

    process_file(args.infile, args.outfile, args.chifre, args.verbose, args.number)


if __name__ == "__main__":
    main()






