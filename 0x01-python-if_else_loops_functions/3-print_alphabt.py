#!/usr/bin/python3
ascii = 97
str = ''

for i in range(97, 123):
    if i != 113 and i != 101:
        str = str + chr(i)
print("{}".format(str), end="")
