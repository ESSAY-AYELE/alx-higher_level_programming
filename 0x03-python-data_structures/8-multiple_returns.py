#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    result = (len(sentence), sentence[0])
    return result
