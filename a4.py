#!/usr/bin/python3.5

# Name:           Brandom Gillespie
# Student Number: A00966847
# Class:          COMP7402
# Assignment:     A4
# Purpose:

# Main
def main():
    plaintext = ""
    while (True):
        where_is_plain = input("Is the plaintext given via stdin or file? ")
        if where_is_plain == "file":
            print("File selected")
            plain = input("File name please: ")
            plaintext += open(plain, 'rU').read()
            break
        elif where_is_plain == "stdin":
            print("stdin selected")
            plain = input("Plaintext please: ")
            plaintext = plain
            break
        else:
            print("Need to select a valid option ('file' or 'stdin')")
    print("Plaintext: " + plaintext)

# Main
if __name__ == "__main__":
    main()
