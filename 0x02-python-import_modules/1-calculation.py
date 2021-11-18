#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculate(func, sign):
    a = 10
    b = 5
    x = func(a, b)
    print("{:d}".format(a), sign, "{:d} = {:d}".format(b, x))


if __name__ == "__main__":
    calculate(add, "+")
    calculate(sub, "-")
    calculate(mul, "*")
    calculate(div, "/")
