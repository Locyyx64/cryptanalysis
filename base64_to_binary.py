#!/bin/python3

base64_table = {"A": "000000",
                "B": "000001",
                "C": "000010",
                "D": "000011",
                "E": "000100",
                "F": "000101",
                "G": "000110",
                "H": "000111",
                "I": "001000",
                "J": "001001",
                "K": "001010",
                "L": "001011",
                "M": "001100",
                "N": "001101",
                "O": "001110",
                "P": "001111",
                "Q": "010000",
                "R": "010001",
                "S": "010010",
                "T": "010011",
                "U": "010100",
                "V": "010101",
                "W": "010110",
                "X": "010111",
                "Y": "011000",
                "Z": "011001",
                "a": "011010",
                "b": "011011",
                "c": "011100",
                "d": "011101",
                "e": "011110",
                "f": "011111",
                "g": "100000",
                "h": "100001",
                "i": "100010",
                "j": "100011",
                "k": "100100",
                "l": "100101",
                "m": "100110",
                "n": "100111",
                "o": "101000",
                "p": "101001",
                "q": "101010",
                "r": "101011",
                "s": "101100",
                "t": "101101",
                "u": "101110",
                "v": "101111",
                "w": "110000",
                "x": "110001",
                "y": "110010",
                "z": "110011",
                "0": "110100",
                "1": "110101",
                "2": "110110",
                "3": "110111",
                "4": "111000",
                "5": "111001",
                "6": "111010",
                "7": "111011",
                "8": "111100",
                "9": "111101",
                "+": "111110",
                "/": "111111"}

def base64_to_binary(b64_text):
    binary_stream = ""
    for char in b64_text:
        if char in base64_table.keys():
            binary_stream += base64_table[char]
        elif char == "=":
            continue
        else:
            raise Exception(f"Invalid character '{char}'!")
    binary = [binary_stream[n-8:n] for n in range(8, len(binary_stream)+8, 8)]
    if len(binary[len(binary)-1]) != 8:   ## DELETING EXTENSION
        binary.pop()
    return binary

def binary_to_base64(binary: list):
    b64_text = ""
    binary_stream = "".join(binary)
    six_bit_binary = [binary_stream[n-6:n] for n in range(6, len(binary_stream)+6, 6)]
    last_sextet = six_bit_binary[len(six_bit_binary)-1]
    if len(last_sextet) != 6:
        six_bit_binary[len(six_bit_binary)-1] += "0"*(6-len(last_sextet)) ## EXTENDING
    for byte in six_bit_binary:
        b64_text += list(base64_table.keys())[list(base64_table.values()).index(byte)]
    if len(six_bit_binary) % 4:
        b64_text += "="*(len(six_bit_binary)%4) ## PADDING
    return b64_text

##print(base64_to_binary("QW1iYXR1a2Ftb21haWdvdA=="))
##print(binary_to_base64("01000001 01101101 01100010 01100001 01110100 01110101 01101011 01100001 01101101 01101111 01101101 01100001 01101001 01100111 01101111 01110100".split(" ")))
