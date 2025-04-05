__author__ = 'Benjamin Zwettler'

import sys
from typing import Set, List, Tuple


def read_all_words(filename:str) -> Set[str]:
    with open(filename, 'r') as f:
        return set(f.read().split())

def split_word(word:str) -> list[tuple[str, str]]:
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]




if __name__ == '__main__':
    print(read_all_words("de-en.txt"))
    print("goat:")
    print(split_word("goat"))