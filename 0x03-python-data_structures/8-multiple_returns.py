#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        lenght = len(sentence)
        first = sentence[0]
    else:
        first = None

    return lenght, first
