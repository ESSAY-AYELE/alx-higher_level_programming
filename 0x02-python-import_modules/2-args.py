#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        tok = 's.'
    elif length == 2:
        tok = ':'
    else:
        tok = 's:'
    print("{} argument{}".format(length - 1, tok))
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
