"""
author: BENJAMIN ZWETTLER
"""


def is_palindrom(input):
    """
    checks if a single word is a palindrom

    :param input:
        a single word in a string
    :return:
        true if the word is a palindrom,
        false otherwise

    examples:
        >>> is_palindrom("hello")
        False
        >>> is_palindrom("abba")
        True
    """
    input = str(input)
    if input == input[::-1]:
        return True
    else :
        return False

def is_palindrom_sentence(input):
    """
    checks if the input is a palindrom sentence (letter by letter)

    :param input:
        a string
    :return:
        true if its a palindrom
        False otherwise

    examples:
        >>> is_palindrom_sentence('hello')
        False
        >>> is_palindrom_sentence('hallo ollah')
        True
    """
    import re
    input = re.sub("[ !?,.]","",input)
    if input == input[::-1]:
        return True
    else:
        return False

def palindrom_product(x):
    """
        generates the highest palindrome that can be calculated by multiplying two 3 digit numbers with each other has to be below x
    :param x:
        the generated palindrome cannot exceed this number
    :return:
        the highest (below input x) palindrome made by multiplying two 3 digit numbers with each other

    examples:
        >>> palindrom_product(100)
        -1
        >>> palindrom_product(1234567)
        906609
    """
    largest_palindrome = -1

    # Beginne mit der größten möglichen Palindromzahl
    for num in range(x - 1, 10000, -1):
        if is_palindrom(num):
            for i in range(999, 99, -1):
                if num % i == 0:
                    j = num // i
                    if 100 <= j <= 999:
                        largest_palindrome = num
                        return largest_palindrome

    return largest_palindrome

def to_base(number:int, base:int)->str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    """

    if base < 2 or base > 36:
        raise ValueError("base has to be between 2 and 36")
    is_negative = number < 0
    number = abs(number)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""

    if number == 0:
        return 0

    while number > 0 :
        rest = number % base
        output = digits[rest] + output
        number = number // base

    if is_negative:
        output = -output

    return output

def get_dec_hex_palindrom(x):
    """
    get the biggest number below x that is a palindrome in decimal notation as well as in hexadecimal notation

    :param x: the palindrom cant be bigger than x
    :return: the biggest palindrome that is below x

    examples:
        >>> get_dec_hex_palindrom(100)
        11
        >>> get_dec_hex_palindrom(1234567)
        845548
    """
    for num in range(x, 0, -1):
        if is_palindrom(num):
            if is_palindrom(to_base(num, 16)):
                return num
    return -1



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(is_palindrom('1231'))
    print(is_palindrom_sentence('hallo ollah'))
    print(palindrom_product(1552234))
    print(to_base(1234,16))
    print(to_base(1234,36))
    print(get_dec_hex_palindrom(1234))