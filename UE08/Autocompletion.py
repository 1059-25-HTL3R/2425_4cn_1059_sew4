__author__ = 'Benjamin Zwettler'

from typing import Set, List
import Levenshtein

def read_all_words(filename:str) -> Set[str]:
    """
    alle wörter aus einer liste in ein set speichern
    :param filename: name der file mir den einzulesenden wörtern in jeder zeile darf nur ein wort stehen
    :return: eine liste mit allen wörtern in der file mir filename angeben
    """
    with open(filename, 'r') as f:
        return set(x.lower() for x in  f.read().split())

def split_word(word:str) -> list[tuple[str, str]]:
    """
    splits ein wort in ein set mit JEDER möglichen position BSP: abc ("", abc),(a,bc) usw. bis (abc, "")
    :param word: das wort das gesplitet werden soll
    :return: [("", abc),(a,bc) usw. bis (abc, "")]
    """
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]


def get_words_edit_distance0(word:str,alle_woerter: Set[str]) -> set[str]:
    out = []
    for listword in alle_woerter:
        if Levenshtein.distance(word, listword) == 0:
            out.append(listword)
    return set(out)


def get_words_edit_distance1(word:str,alle_woerter: Set[str]) -> set[str]:
    out = []
    for listword in alle_woerter:
        if Levenshtein.distance(word, listword) == 1:
            out.append(listword)
    return set(out)

def get_words_edit_distance2(word:str,alle_woerter: Set[str]) -> set[str]:
    out = []
    for listword in alle_woerter:
        if Levenshtein.distance(word, listword) == 2:
            out.append(listword)
    return set(out)


def correct(word:str, alle_woerter: set[str]) ->Set[str]:
    if get_words_edit_distance0(word,alle_woerter):
        return get_words_edit_distance0(word,alle_woerter)
    elif get_words_edit_distance1(word,alle_woerter):
        return get_words_edit_distance1(word,alle_woerter)
    elif get_words_edit_distance2(word,alle_woerter):
        return get_words_edit_distance2(word,alle_woerter)
    else:
        return set()



if __name__ == '__main__':
    words = read_all_words('de-en.txt')
    print(correct('apf', words))