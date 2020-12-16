#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_return = (0, )
    length = len(sentence)
    first = sentence[0]
    tuple_return = (tuple_return[0] + length, first)
    return tuple_return
