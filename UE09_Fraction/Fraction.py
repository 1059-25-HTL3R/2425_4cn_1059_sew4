__author__ = "Benjamin Zwettler"

from functools import total_ordering
from math import gcd

@total_ordering
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ArithmeticError("denominator cannot be 0")

        if  denominator < 0:
            denominator = -denominator
            numerator = -numerator

        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
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
        :return: a string representation of the Fraction
        """
        self.kuerzen()
        return f"Fraction({self._numerator}/{self._denominator})"

    def kuerzen(self):
        greatestteiler = gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // greatestteiler
        self._denominator = self._denominator // greatestteiler
        return Fraction(self._numerator, self._denominator)

    def __add__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator, self._denominator * other._denominator)
            frac1._numerator = (frac1._numerator * other._denominator) + (other._numerator * self._denominator)
            return frac1.kuerzen()

    def __sub__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator, self._denominator * other._denominator)
            frac1._numerator = (frac1._numerator * other._denominator) - (other._numerator * self._denominator)
            return frac1.kuerzen()

    def __mul__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._numerator, self._denominator * other._denominator)
            return frac1.kuerzen()

    def __truediv__(self, other):
        """wenn / geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
            return frac1.kuerzen()

    def __floordiv__(self, other):
        """wenn // geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self._numerator * other._denominator, self._denominator * other._numerator)
            return frac1.kuerzen()

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self._numerator == other._numerator and self._denominator == other._denominator
        if isinstance(other, int):
            return NotImplemented
        return NotImplemented

    def __lt__(self, other):
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