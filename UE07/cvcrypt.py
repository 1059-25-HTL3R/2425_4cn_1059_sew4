__author__ = "Benjamin Zwettler"

import argparse
import os

def process_file(input_file: str, output_file: str, cipher: str, key, decrypt: bool, verbose: bool):
    if not os.path.exists(input_file):
        raise FileNotFoundError


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

    if args.verbose:
        print(f"Verbose-Modus: {args.verbose}")
        print(f"chifre: {args.chifre}")
        print(f"srcPath: {args.infile}")
        print(f"destPath: {args.outfile}")
        print(f"key: {args.key}")
        print(f"decrypt: {args.decrypt}")
        print(f"encrypt: {args.encrypt}")
    process_file(args.infile, args.outfile, args.cipher, args.key, args.decrypt, args.verbose)


if __name__ == "__main__":
    main()






