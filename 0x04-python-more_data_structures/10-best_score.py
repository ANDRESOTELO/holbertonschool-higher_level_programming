#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and a_dictionary.get:
        return max(a_dictionary.keys())
    else:
        return None
