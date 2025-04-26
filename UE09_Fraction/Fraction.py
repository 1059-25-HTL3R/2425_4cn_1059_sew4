__author__ = "Benjamin Zwettler"

from functools import total_ordering
from math import gcd

@total_ordering
class Fraction:

    """
    Fraction Class to calculate with fractions
        >>> f1 = Fraction(1, 2)
        >>> f1
        Fraction(1/2)
        >>> print(f1)
        1/2
        """

    def __init__(self, numerator=0, denominator=1):
        """
        initializes a Fraction object

        >>> Fraction(3)
        Fraction(3/1)
        >>> Fraction(3,0)
        Traceback (most recent call last):
            ...
        ArithmeticError: denominator cannot be 0

        :param numerator:
        :param denominator:
        """
        if denominator == 0:
            raise ArithmeticError("denominator cannot be 0")

        if  denominator < 0:
            denominator = -denominator
            numerator = -numerator

        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
        """
        Gives a string representation of the Fraction

        >>> str(Fraction(1, 2))
        '1/2'
        >>> str(Fraction(2, 1))
        '2'
        >>> str(Fraction(-3, 5))
        '-3/5'

        :return: the fraction as a string
        """
        self.kuerzen()
        if abs(self._numerator) >= abs(self._denominator):
            ganze = int(self._numerator / self._denominator)
            rest = abs(self._numerator) % self._denominator
            if rest != 0:
                return str(ganze) + " " + str(rest) +"/"+ str(self._denominator)
            else:
                return str(ganze)
        else:
            if self._numerator == 0:
                return str(0)
            return str(self._numerator) + "/" + str(self._denominator)

    def __repr__(self) -> str:
        """
        gives a string representation of the Fraction
        >>> Fraction(1, 2).__repr__()
        'Fraction(1/2)'
        >>> Fraction(-1, 2).__repr__()
        'Fraction(-1/2)'

        :return: a string representation of the Fraction
        """
        self.kuerzen()
        return f"Fraction({self._numerator}/{self._denominator})"

    def kuerzen(self):
        """
        simplyfies a Fraction

        >>> Fraction(10, 2).kuerzen()
        Fraction(5/1)
        >>> Fraction(-10, 2).kuerzen()
        Fraction(-5/1)

        :return:
        """
        greatestteiler = gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // greatestteiler
        self._denominator = self._denominator // greatestteiler
        return Fraction(self._numerator, self._denominator)

    def __add__(self, other):
        """
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 + f2
        Fraction(1/1)

        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(-1, 2)
        >>> f1 + f2
        Fraction(0/1)

        adds another Fraction to itself
        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator, self._denominator * other._denominator)
            frac1._numerator = (frac1._numerator * other._denominator) + (other._numerator * self._denominator)
            return frac1.kuerzen()

    def __sub__(self, other):
        """
        substracts another Fraction from itself
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 - f2
        Fraction(0/1)

        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(-1, 2)
        >>> f1 - f2
        Fraction(1/1)

        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator, self._denominator * other._denominator)
            frac1._numerator = (frac1._numerator * other._denominator) - (other._numerator * self._denominator)
            return frac1.kuerzen()

    def __mul__(self, other):
        """
        multiplies two Fractions
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 * f2
        Fraction(1/4)

        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(-1, 2)
        >>> f1 * f2
        Fraction(-1/4)

        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._numerator, self._denominator * other._denominator)
            return frac1.kuerzen()

    def __truediv__(self, other):
        """
        divides two Fractions
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 / f2
        Fraction(1/1)

        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(-1, 2)
        >>> f1 / f2
        Fraction(-1/1)

        :param other:
        :return:
        """
        """wenn / geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
            return frac1.kuerzen()

    def __floordiv__(self, other):
        """
                divides two Fractions
                >>> f1 = Fraction(1, 2)
                >>> f2 = Fraction(1, 2)
                >>> f1 // f2
                Fraction(1/1)

                >>> f1 = Fraction(1, 2)
                >>> f2 = Fraction(-1, 2)
                >>> f1 // f2
                Fraction(-1/1)

                :param other:
                :return:
                """
        """wenn // geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
            return frac1.kuerzen()

    def __eq__(self, other):
        """
        checks if two Fractions are equal
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 == f2
        True

        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(-1, 2)
        >>> f1 == f2
        False

        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            return self._numerator == other._numerator and self._denominator == other._denominator
        if isinstance(other, int):
            return NotImplemented
        return NotImplemented

    def __lt__(self, other):
        """
        check if two Fractions are less than other
        >>> f1 = Fraction(1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 < f2
        False

        >>> f1 = Fraction(-1, 2)
        >>> f2 = Fraction(1, 2)
        >>> f1 < f2
        True

        :param other:
        :return:
        """
        if isinstance(other, Fraction):
            return self._numerator / self._denominator < other._numerator / other._denominator
        if isinstance(other, int):
            return NotImplemented
        return NotImplemented

    def _numerator(self):
        return self._numerator

    def _denominator(self):
        return self._denominator

    def __float__(self):
        return self._numerator / self._denominator



if __name__ == "__main__":
    fraction1 = Fraction(-1,2 )
    fraction2 = Fraction(1, 2)
    print(fraction1 - fraction2)