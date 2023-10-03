#!/usr/bin/python3
for i in range(0, 100):
    print("{:02d}".format(i), end="")
    if i is not 99:
        print(",", end=" ")
print('\n')
