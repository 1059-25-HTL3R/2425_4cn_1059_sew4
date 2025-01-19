




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




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(is_palindrom('1231'))
    print(is_palindrom_sentence('hallo ollah'))
    print(palindrom_product(1552234))