"""
Benjamin Zwettler
"""
import math
import re
from collections import Counter
from typing import List, Set, Tuple
import string

class Ceaser:
    def __init__(self, key: str = "a"):
        self.key = key.lower()
    @staticmethod
    def to_lowercase_letter_only(plaintext: str) -> str:
        """
        :param plaintext: Input Text
        :return: String der nur aus kleinbuchstaben besteht alles andere wird gelöscht
        >>> c = Ceaser("a")
        >>> c.to_lowercase_letter_only("Hallo!")
        'hallo'
        """
        return re.sub('[^a-z]',"",plaintext.lower())

    def encrypt(self, plaintext: str, key:str = None) -> str:
        """

        :param plaintext: Input Text
        :param key: key zum verschlüsseln
        :return: plaintext mit key in ceaser verschlüsselt
        >>> c = Ceaser("b")
        >>> c.encrypt("abc!")
        'bcd'
        """
        if key is None:
            key = self.key
        alphabet = string.ascii_lowercase
        index_key = alphabet.index(key)
        plaintext = self.to_lowercase_letter_only(plaintext)
        output = ""
        for char in plaintext:
            index_char = alphabet.index(char)
            output += alphabet[(index_key + index_char) % 26]
        return output


    def decrypt(self, ciphertext: str, key:str = None) -> str:
        """

        :param ciphertext: verschlüselter text
        :param key: zum entschlüsseln
        :return: cipherstring entschlüsselt
        """
        if key is None:
            key = self.key
        alphabet = string.ascii_lowercase
        index_key = alphabet.index(key)
        ciphertext = self.to_lowercase_letter_only(ciphertext)
        output = ""
        for char in ciphertext:
            index_char = alphabet.index(char)
            output += alphabet[(index_char - index_key) % 26]
        return output

    def crack(self, crypttext:str, elements:int = 1) -> List[str]:
        """

        :param crypttext: verschlüsselter text
        :param elements: wie lang output sein kann
        :return: eine liste an möglichen keys die anhand von häufigkeit des E's in der deutschen sprache ermittelt werden
        """
        crypttext = Ceaser.to_lowercase_letter_only(crypttext)
        char_count = {}
        for char in crypttext:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        sorted_dict = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
        return [string.ascii_lowercase[string.ascii_lowercase.index(key) - string.ascii_lowercase.index("e")]  for  key in sorted_dict.keys()]
        # return list(sorted_dict.keys())[:elements]



class Vigenere:
    def __init__(self, key: str = "test"):
        self.key = key.lower()

    def encrypt(self, plaintext:str, key:str = None) -> str:
        """

        :param plaintext: zu verschlüsselner text
        :param key: key wort zum entschlüsseln
        :return: plaintext mit keywort verschlüsselt
        """
        if key is None:
            key = self.key

        c = Ceaser()
        plaintext = Ceaser.to_lowercase_letter_only(plaintext)
        output = ""
        for index, char in enumerate(plaintext):
            output += c.encrypt(char, key[index%len(key)])
        return output

    def decrypt(self, ciphertext: str, key:str = None) -> str:
        """

        :param ciphertext: verschlüsselter text
        :param key: keywort zum entschlüsseln
        :return: entschlüsselter text
        """
        if key is None:
            key = self.key

        c = Ceaser()
        ciphertext = Ceaser.to_lowercase_letter_only(ciphertext)
        output = ""
        for index, char in enumerate(ciphertext):
            output += c.decrypt(char, key[index%len(key)])
        return output


class Kasinski:
    def __init__(self, crypttext: str = "test"):
        self.crypttext = Ceaser.to_lowercase_letter_only(crypttext)

    def allpos(self,text:str,teilstring:str) -> List[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasinski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []"""
        matcher = re.finditer(teilstring, text)
        positionen = []

        for m in matcher:
            positionen.append(m.start())
        return positionen

    def alldist(self, text:str, teilstring:str) -> Set[int]:
        """Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text.
        Usage examples:
        >>> k = Kasinski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()"""
        positionen = self.allpos(text,teilstring)
        distances = []

        for i in range(1,len(positionen)):
            distances.append(positionen[i] -positionen[i-1])
        return set(distances)

    def dist_n_tuple(self,text:str, laenge:int) -> Set[Tuple[str,int]]:
        """Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasinski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        result = set()

        for i in range(len(text) - laenge):
            substring = text[i: i + laenge]
            distances = self.alldist(text, substring)

            for j in distances:
                result.add((substring,j))
        return result

    def dist_n_list(self,text:str, laenge:int) -> List[int]:
        """Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasinski()
        >>> Kasinski.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> Kasinski.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> Kasinski.dist_n_list("heissajucheieinei", 4)
        []"""
        result = {}

        for i in range(len(text) - laenge):
            substring = text[i: i + laenge]
            distances = self.alldist(text, substring)

            for j in distances:
                result[substring] = j
        sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return list(sorted(set(sorted_result.values())))

    def ggt(self, x: int, y: int) -> int:
        """Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasinski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 25)
        5"""
        return math.gcd(x, y)

    def ggt_count(self, zahlen:list[int]) -> Counter:
        pairs = []
        for i in range(len(zahlen)):
            for j in range(i+1,len(zahlen)):
                pairs.append(self.ggt(zahlen[i], zahlen[j]))
        return Counter(pairs)

    def crack_key(self, len:int = 3) -> str:

        output = ""
        k = Kasinski(self.crypttext)
        ggt_counter = k.ggt_count(k.dist_n_list(k.crypttext,3))
        key_length = list(ggt_counter)[0]
        templist = {}
        for index, char in enumerate(self.crypttext) :
            if index%key_length in templist:
                templist[index%key_length] += str(char)
            else:
                templist[index%key_length] = "" + str(char)

        ceas = Ceaser()
        for index, currlist in enumerate(templist):
            output += ceas.crack(templist[index],1)[0]
        return output



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    c = Ceaser("b")
    print(c.encrypt("abc!"))
    c.encrypt("abc!")

