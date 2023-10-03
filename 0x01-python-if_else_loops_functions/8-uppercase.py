#!/usr/bin/python3
def islower(c):
    d = ord(c)
    if d >= 97 and d <= 123:
        return (True)
    return (False)


def uppercase(s):
    for c in s:
        if islower(c):
            c = chr(ord(c) - 32)
        print(c, end='')
    print('')
