#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    idx = 0
    for c in str:
        if idx != n:
            cpy += c
        idx += 1
    return (cpy)
