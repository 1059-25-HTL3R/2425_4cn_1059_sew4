"""
Benjamin Zwettler

"""


from typing import List, Set, Tuple

class Ceaser:

    def __init__(self, key: str = "a"):
        self.key = key.lower()

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        return plaintext.lower()


    def encrypt(self, plaintext: str, key:str = None) -> str:
        return "no"

    def decrypt(self, ciphertext: str, key:str = None) -> str:
        return "no"

    def crack(self,crypttext:str, elements:int = 1) -> List[str]:
        return []

