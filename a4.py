#!/usr/bin/python3.5

# Name:           Brandom Gillespie
# Student Number: A00966847
# Class:          COMP7402
# Assignment:     A4
# Purpose:        Encrypt and decrypt plaintext in the Feistel Cipher method.
#                 Plaintext is to be given in an binary string of even length,
#                 The program also requires an amount of rounds for the cipher,
#                 as well as a key.

import sys

# Cipher function that is used before xor.
def cipher_function(i, k, r):
    return (((2 * r * k)**i) % 15)

# Put the given message through the Feistel cipher process. This function can be
# used to encrypt or decrypt. Pt is the message, k is the key, and r is the rounds
# function input.
def feistel_cipher(pt, k, r):
    leftside, rightside = int(pt[:int(len(pt) / 2)], 2), int(pt[int(len(pt) / 2):], 2)

    print("Pre Encrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    for i in range(len(r)):
        xor_value = cipher_function(rightside, int(k), r[i])
        left_xor = xor_value ^ leftside
        leftside = rightside
        rightside = left_xor

    print("Post Encrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    format_string = "{:0" + str(len(pt) // 2) + "b}"
    result = format_string.format(rightside)
    result += format_string.format(leftside)
    return result

# Main
def main():
    plaintext = ""
    round_inputs = []
    while (True):
        where_is_plain = input("Is the plaintext given via stdin or file? ")
        if where_is_plain == "file":
            print("File selected")
            plain = input("File name please: ")
            plaintext += open(plain, 'rU').read()
            plaintext = plaintext.strip('\n')
            break
        elif where_is_plain == "stdin":
            print("stdin selected")
            plain = input("Plaintext please: ")
            plaintext = plain
            break
        else:
            print("Need to select a valid option ('file' or 'stdin')")

    if (len(plaintext) % 2) != 0:
        print("Please give plaintext of even length")
        sys.exit(0)

    key = input("Key please: ")
    rounds = input("Amount of rounds please: ")

    print("")
    print("Plaintext: " + plaintext)
    print("Key: " + key)
    print("Amount of rounds: " + rounds)
    print("")

    for i in range(int(rounds)):
        round_inputs.append(i + 1)

    encrypt_result = feistel_cipher(plaintext, key, round_inputs)
    print("Ciphertext: " + encrypt_result)

    round_inputs.reverse()

    decrypt_result = feistel_cipher(encrypt_result, key, round_inputs)
    print("Plaintext: " + decrypt_result)


# Main
if __name__ == "__main__":
    main()
