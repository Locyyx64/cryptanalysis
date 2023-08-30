#!/usr/bin/python3

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def get_pos(text):
    positions = []
    for char in text:
        positions.append(alphabet.index(char))
    return positions

def shift(text, times):
    char_positions = get_pos(text.upper())
    new_string = ""
    for pos in char_positions:
        new_string += alphabet[(pos+times)%26]
    return new_string
