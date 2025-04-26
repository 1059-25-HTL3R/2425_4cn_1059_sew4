__author__ = "Benjamin Zwettler"

from functools import total_ordering
from math import gcd

#@total_ordering
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









if __name__ == "__main__":
    fraction1 = Fraction(6, 3)
    fraction2 = Fraction(6, 4)
    print(fraction1.denominator)