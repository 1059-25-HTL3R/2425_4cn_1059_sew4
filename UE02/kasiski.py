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
        if key is None:
            key = self.key

        key = chr(ord(key) - ord('a'))
        plaintext = self.to_lowercase_letter_only(plaintext)
        output = ""
        for char in plaintext:
            output += chr(ord(char) + ord(key))
        return output


    def decrypt(self, ciphertext: str, key:str = None) -> str:
        if key is None:
            key = self.key

        key = chr(ord(key) - ord('a'))
        ciphertext = self.to_lowercase_letter_only(ciphertext)
        output = ""
        for char in ciphertext:
            output += chr(ord(char) - ord(key))
        return output

    def crack(self,crypttext:str, elements:int = 1) -> List[str]:
        return []

if __name__ == "__main__":
    c = Ceaser("b")
    print(c.key)
    print(c.encrypt("abc"))
    print(c.decrypt("bcd"))




