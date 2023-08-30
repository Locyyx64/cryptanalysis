#!/bin/python3

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def shift_alphabet(times):
    new_alphabet = [char for char in alphabet]
    for i in range(times):
        new_alphabet.append(new_alphabet[0])
        new_alphabet.pop(0)
    return new_alphabet

def generate_tabula_recta():
    tabula_recta = []
    for i in range(26):
        tabula_recta.append(shift_alphabet(i))
    return tabula_recta

tabula_recta = generate_tabula_recta()


## Encrypt plaintext using the Vigenere cipher. If the 'autokey' parameter is set to true, the given key will be used as a primer
## for the autokey. NOTE: Neither the plaintext, nor the key can contain ANY numbers.
def encode(plaintext, key, autokey=False):
    assert type(autokey) == bool
    plaintext = plaintext.upper()
    key = key.upper()
    cipher = ""
    if not autokey:
        for i in range(len(plaintext)):
            cipher += tabula_recta[alphabet.index(plaintext[i])][alphabet.index(key[i%len(key)])]
    else:
        full_key = key+plaintext
        for i in range(len(plaintext)):
            cipher += tabula_recta[alphabet.index(plaintext[i])][alphabet.index(full_key[i%len(full_key)])]
    return cipher


## Decrypt the cipher using Vigenere. Again, if the 'autokey' parameter is set to true, the given key will be used as a primer
## for the autokey. Now, algorithmically deciphering the Vigenere autokey cipher is pretty fucking tricky, so the code I wrote
## might not be the best out there.
def decode(cipher, key, autokey=False, known_plaintext="", index=0, verbose=False):
    assert type(autokey) == bool and type(verbose) == bool
    cipher = cipher.upper()
    key = key.upper()
    plaintext = ''.join([char for char in known_plaintext])
    if not autokey:
        for i in range(len(cipher)):
            for j in range(len(tabula_recta)):
                if tabula_recta[j][alphabet.index(key[i%len(key)])] == cipher[i]:
                    plaintext += alphabet[j]
        return plaintext
    else:
        if verbose:
            print(f'Key section: {key}')
        for i in range(index, index+len(key)):
            if verbose:
                print(f'Index: {index}, i: {i}')
            try:
                for j in range(len(tabula_recta)):
                    if tabula_recta[j][alphabet.index(key[i%len(key)])] == cipher[i]:
                        plaintext += alphabet[j]
                        if verbose:
                            print(f'Plaintext: {plaintext}')
            except IndexError:
                if verbose:
                    print(f'Decoding process has finished, climbing down the ladder...')
                return plaintext
        return decode(cipher, plaintext[index::], autokey=True, known_plaintext=plaintext, index=index+len(key), verbose=verbose)

## This is a special function, mainly developed for cryptanalysis. You have to submit a plaintext and a ciphertext, and
## it gives you the key, with which the two can be converted to each other.
def get_key(cipher, plaintext):
    assert len(cipher) == len(plaintext)
    cipher = cipher.upper()
    plaintext = plaintext.upper()
    key = ""
    for i in range(len(plaintext)):
        key += alphabet[tabula_recta[alphabet.index(plaintext[i])].index(cipher[i])]
    return key
