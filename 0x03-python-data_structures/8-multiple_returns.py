#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        lenght = len(sentence)
        first = sentence[0]
    else:
        lenght = len(sentence)
        first = None

    return lenght, first
