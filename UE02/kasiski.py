"""
Benjamin Zwettler

"""
import math
import re
from typing import List, Set, Tuple
from collections import Counter

class Ceaser:

    def __init__(self, key: str = "a"):
        self.key = key.lower()

    def to_lowercase_letter_only(self, plaintext: str) -> str:
        """

        :param plaintext: text der zu lowercase gemacht wird
        :return: plaintext in lowercase
        >>>TEST= Ceaser()
        >>>TEST.to_lowercase_letter_only("A")
        "a"
        >>>TEST= Ceaser()
        >>>TEST.to_lowercase_letter_only("AB")
        "ab"
        """
        return plaintext.lower()


    def encrypt(self, plaintext: str, key:str = None) -> str:
        """

        :param plaintext: text der verschlüsselt werden soll
        :param key: schlüssel der zum verschlüsseln verwendet werden soll
        :return: ein string der plaintext mit key verschlüsselt ist
        >>>TEST= Ceaser()
        >>>TEST.encrypt("A", key = "b")
        "b"
        >>>TEST= Ceaser()
        >>>TEST.encrypt("ABC", key = "c")
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
        >>>TEST= Ceaser()
        >>>TEST.decrypt("B", key = "b")
        "a"
        >>>TEST= Ceaser()
        >>>TEST.decrypt("CDE", key = "c")
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


class Vigenere:
    def __init__(self, key: str):
        self.key = key.lower()

    def encrypt(self, plaintext: str, key:str = None) -> str:
        """

        :param plaintext: zu verschlüsselnder text
        :param key: key zum verschlüsseln der mehr als ein zeichen lang sein kan naber kürzer als plaintext sein sollte
        :return: string der plaintext mit key verschlüsselt ist
        """
        if key is None:
            key = self.key

        c = Ceaser()
        plaintext = c.to_lowercase_letter_only(plaintext)
        output = ""
        for index, char in enumerate(plaintext):
            output += c.encrypt(char, key[index%len(self.key)])
        return output

    def decrypt(self, crypttext: str, key:str = None) -> str:
        """

        :param crypttext: verschlüsslter text
        :param key: key zum entschlüsseln des texts
        :return: entschlüsselter string der cryptext mit key entschlusselt ist
        """
        if key is None:
            key = self.key

        c = Ceaser()
        crypttext = c.to_lowercase_letter_only(crypttext)
        output = ""
        for index, char in enumerate(crypttext):
            output += c.decrypt(char, key[index % len(self.key)])
        return output

    def crack(self) -> List[str]:
        return []





class Kasiski:
    def __init__(self, crypttext: str = ""):
        self.crypttext = crypttext

    def allpos(self, text:str, teilstring:str) -> List[int]:
        matches = re.finditer(teilstring, text)
        positions = []

        for m in matches:
            positions.append(m.start())
        return positions

    def alldist(self, text:str, teilstring:str) -> Set[int]:
        allposs: List[int] = self.allpos(text, teilstring)
        differences = []

        for i in range(len(allposs)):
            for j in range(i + 1, len(allposs)):
                differences.append(allposs[j] - allposs[i])

        return set(sorted(differences))

    def dist_n_tuple(self, text:str, laenge:int) -> Set[Tuple[str, int]]:
        result = set()

        for i in range(len(text) - laenge):
            substring = text[i: i + laenge]
            distances = self.alldist(text, substring)

            for j in distances:
                result.add((substring, j))

        return result

    def dist_n_list(self, text:str, laenge:int) -> List[int]:
        unique_distances = set()

        for i in range(len(text) - laenge):
            substring = text[i: i + laenge]
            distances = self.alldist(text, substring)

            for j in distances:
                unique_distances.add(j)

        return sorted(list(unique_distances))

    def ggt(self, x:int, y:int) -> int:
        return  math.gcd(x,y)

    def ggt_count(self, zahlen:List[int]) -> Counter:
        return Counter({})





if __name__ == "__main__":
    c = Ceaser("b")
    print(c.key)
    print(c.encrypt("abc"))
    print(c.decrypt("bcd"))

    print("vigi")
    v = Vigenere("abc")
    print(v.key)
    print(v.encrypt("abc"))
    print(v.decrypt("ace"))

    print("---")
    k = Kasiski("cbd")
    text = "abcabcabcabcabc"
    print(k.allpos(")abca", "a"))
    print(k.alldist("abca", "a"))
    print(k.dist_n_tuple(text, 3))

    print("---")




