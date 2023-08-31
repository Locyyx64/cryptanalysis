#!/bin/python3

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def shift(text) -> str:
    new_string = ""
    for char in text.upper():
        new_string += alphabet[len(alphabet)-1-alphabet.index(char)]
    return new_string
