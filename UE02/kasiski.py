"""
Benjamin Zwettler

"""


from typing import List, Set, Tuple

class Ceaser:

    def __init__(self, key: str = "a"):
        self.key = key.lower()

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """

        :param plaintext: text der zu lowercase gemacht wird
        :return: plaintext in lowercase
        >>>to_lowercase_letter_only("A")
        "a"
        >>>to_lowercase_letter_only("AB")
        "ab"
        """
        return plaintext.lower()


    def encrypt(self, plaintext: str, key:str = None) -> str:
        """

        :param plaintext: text der verschlüsselt werden soll
        :param key: schlüssel der zum verschlüsseln verwendet werden soll
        :return: ein string der plaintext mit key verschlüsselt ist
        >>>encrypt("A", key = "b")
        "b"
        >>>encrypt("ABC", key = "c")
        "CDE"
        """
        if key is None:
            key = self.key

        key = chr(ord(key) - ord('a'))
        plaintext = self.to_lowercase_letter_only(plaintext)
        output = ""
        for char in plaintext:
            output += chr(ord(char) + ord(key))
        return output


    def decrypt(self, ciphertext: str, key:str = None) -> str:
        """

        :param ciphertext: verschlüsserter text der entschlüsselt werden soll
        :param key: schlüssel zum entschlüsseln von ciphertext
        :return: entschlüsselter string
        >>>decrypt("B", key = "b")
        "a"
        >>>decrypt("CDE", key = "c")
        "abc"
        """
        if key is None:
            key = self.key

        key = chr(ord(key) - ord('a'))
        ciphertext = self.to_lowercase_letter_only(ciphertext)
        output = ""
        for char in ciphertext:
            output += chr(ord(char) - ord(key))
        return output

    def crack(self,crypttext:str, elements:int = 1) -> List[str]:
        """

        :param crypttext: verschlüsster text an dem eine häufigkeitsanalyse angewendet werden soll
        :param elements: die länger der auszugebenen liste (kann nciht länger als 26 zeichen sein da es nur 26 schlüssel gibt)
        :return: eine liste die die möglichen schlüssel anhand ihrer häufigkeit ausgibt
        """

        return []

if __name__ == "__main__":
    c = Ceaser("b")
    print(c.key)
    print(c.encrypt("abc"))
    print(c.decrypt("bcd"))




