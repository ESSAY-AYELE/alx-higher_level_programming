#!/usr/bin/python3
for i in range(97, 123):
    f = chr(i)
    if f == q or f == e:
        continue
    print("{0}".format(f), end='')
