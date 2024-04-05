class Integer:
    def __init__(self, integer):
        self.integer = integer
        assert type(integer) == int

    def __str__(self):
        return f"Integer: {self.integer}"

    def __add__(self, other):
        return Integer(self.integer + other.integer)


i = Integer(7) + Integer(15)
print(i)


class Rational(Integer):
    def __init__(self, integer, denominator):
        super().__init__(integer)
        self.den = denominator
        assert denominator != 0 and type(denominator) == int

    def __str__(self):
        return f"Rational: {self.integer}/{self.den}"

    def __add__(self, other):
        if type(other) == Integer:
            return Rational(self.integer + other.integer, self.den)
        elif type(other) == Rational:
            num = self.integer * other.den + other.integer * self.den
            den = self.den * other.den
            return Rational(num, den)


r = Rational(2, 3) + Integer(7) + Rational(15, 2)
print(r)