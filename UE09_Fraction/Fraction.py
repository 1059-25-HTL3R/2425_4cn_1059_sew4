__author__ = "Benjamin Zwettler"

from functools import total_ordering
from math import gcd

@total_ordering
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ArithmeticError("denominator cannot be 0")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        self.kuerzen()
        if self.numerator >= self.denominator:
            ganze = int(self.numerator / self.denominator)
            rest = self.numerator % self.denominator
            if rest != 0:
                return str(ganze) + " " + str(rest) +"/"+ str(self.denominator)
            else:
                return str(ganze)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __repr__(self) -> str:
        """
        :return: a string representation of the Fraction
        """
        self.kuerzen()
        return f"Fraction({self.numerator}/{self.denominator})"

    def kuerzen(self):
        greatestteiler = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // greatestteiler
        self.denominator = self.denominator // greatestteiler
        return Fraction(self.numerator, self.denominator)

    def __add__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self.numerator, self.denominator * other.denominator)
            frac1.numerator = (frac1.numerator * other.denominator) + (other.numerator * self.denominator)
            return frac1.kuerzen()

    def __sub__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self.numerator, self.denominator * other.denominator)
            frac1.numerator = (frac1.numerator * other.denominator) - (other.numerator * self.denominator)
            return frac1.kuerzen()

    def __mul__(self, other):
        if isinstance(other, Fraction):
            frac1 = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
            return frac1.kuerzen()

    def __truediv__(self, other):
        """wenn / geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
            return frac1.kuerzen()

    def __floordiv__(self, other):
        """wenn // geschrieben wird"""
        if isinstance(other, Fraction):
            frac1 = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
            return frac1.kuerzen()

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        if isinstance(other, int):
            return NotImplemented
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator / self.denominator < other.numerator / other.denominator









if __name__ == "__main__":
    fraction1 = Fraction(6, 3)
    fraction2 = Fraction(6, 1)
    print((fraction1 + fraction2))

    print((fraction2 - fraction1))

    print((fraction1 * fraction2))

    print((fraction1 // fraction2))

    print((fraction1 < fraction2))