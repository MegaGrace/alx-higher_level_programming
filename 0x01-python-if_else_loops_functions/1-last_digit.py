#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
            last = number % 10
elif number == 0:
            last = "0"
else:
            last = number % -10
if last > 5:
            x = "and is greater than 5"
elif last == 0:
            x = "and is 0"
elif last < 6 and last != 0:
            x = "and is less than 6 and not 0"
            print("Last digit of {:d} is {:d} {:s}".format(number, last, x))
