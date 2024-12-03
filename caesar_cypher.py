"""
********************************************************************************
* Project Name:  Caesar Cypher Encryptor and Decryptor
* Description:   It encrypt and decrypt the user input
* Author:        ziqkimi308
* Created:       2024-12-03
* Updated:       2024-12-03
* Version:       1.0
********************************************************************************
"""

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define a function
def caesar(direction, message, shift):
    if direction == "decode":
        shift *= -1

    cipher_text = ""
    for i in message:
        if i in alphabet:
            shift_index = alphabet.index(i) + shift
            cipher_text += alphabet[shift_index]
        else:
            cipher_text += i
    print(f"{direction} text : {cipher_text}")

# Opening
print(logo)

# Continuous loop
should_continue = True
while should_continue:
    direction = input("Enter 'encode' to encrypt or 'decode' to decrypt : ").lower()
    if direction != 'encode' and direction != 'decode':
        print("Invalid input!")
        continue
    message = input("Enter your message : ").lower()
    shift = int(input("Type shift number : "))

    shift %= 26

    caesar(direction, message, shift)

    result = input("Type 'yes' to continue or 'no' to quit : ").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye!")