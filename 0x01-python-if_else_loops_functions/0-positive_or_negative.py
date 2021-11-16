#!/usr/bin/python3
# a program that returns a random signed no.
#to the variable number each time it is executed.

import random
number = random.randint(-10, 10)
if (number > 0):
    print("{:d} is positive\n".format(number))

elif (number < 0):
    print("{:d} is negative\n".format(number))

else:
    print("{:d} is zero\n".format(number))
