#!/usr/bin/python3
for y in range(9):
    for z in range(1, 10):
        if (z < y or z == y):
            continue
        if (y != 8):
            print("{:d}{:d}\n".format(y, z), end=', ')
        else:
            print("{:d}{:d}\n".format(y, z))
