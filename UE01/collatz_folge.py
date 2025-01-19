from typing import List


def collatz(n,numbers: List[int]):
    """
    returns a list of the collatz algorythm starting with n

    :param n: starting number
    :param numbers: empty initial list
    :return: a list of all the collatz numbers

    examples:
        >>> collatz(3,[])
        [10, 5, 16, 8, 4, 2, 1]
        >>> collatz(11,[])
        [34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    if n == 1:
        return numbers
    if n % 2 == 0:
        numbers.append(n // 2)
        return collatz(n // 2,numbers)
    if n % 2 == 1:
        numbers.append(3 * n + 1)
        return collatz(3 * n + 1,numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(collatz(11,[]))
