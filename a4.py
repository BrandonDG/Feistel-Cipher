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

# Encrypt plaintext (pt) with the key (k) for a specified set of rounds (r).
# Encryption is done using the Feistel Cipher.
def encrypt(pt, k, r):
    leftside, rightside = int(pt[:int(len(pt) / 2)], 2), int(pt[int(len(pt) / 2):], 2)

    print("Pre Encrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    for i in range(int(r)):
        xor_value = cipher_function(rightside, int(k), i + 1)
        left_xor = xor_value ^ leftside
        leftside = rightside
        rightside = left_xor

    print("Post Encrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    format_string = "{:0" + str(len(pt) // 2) + "b}"
    result = format_string.format(leftside)
    result += format_string.format(rightside)
    return result

# Decrypt ciphertext (pt) with the key (k) for a specified set of rounds (r).
# Decryption is done using the Feistel Cipher.
def decrypt(pt, k, r):
    leftside, rightside = int(pt[:int(len(pt) / 2)], 2), int(pt[int(len(pt) / 2):], 2)

    print("Pre Decrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    i = int(r)
    while i > 0:
        xor_value = cipher_function(leftside, int(k), i)
        right_xor = xor_value ^ rightside
        rightside = leftside
        leftside = right_xor
        i -= 1

    print("Post Decrypt = Left side: " + str(leftside) + " -- Right Side: " + str(rightside))

    format_string = "{:0" + str(len(pt) // 2) + "b}"
    result = format_string.format(leftside)
    result += format_string.format(rightside)
    return result


# Main
def main():
    plaintext = ""
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

    encrypt_result = encrypt(plaintext, key, rounds)
    print("Ciphertext: " + encrypt_result)

    decrypt_result = decrypt(encrypt_result, key, rounds)
    print("Plaintext: " + decrypt_result)


# Main
if __name__ == "__main__":
    main()
