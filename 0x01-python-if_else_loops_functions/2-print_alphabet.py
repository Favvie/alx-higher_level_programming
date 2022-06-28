#!/usr/bin/python3
ascii = 97
str = ''
while ascii != 123:
    str = str + chr(ascii)
    ascii = ascii + 1
print("{}".format(str), end="")
