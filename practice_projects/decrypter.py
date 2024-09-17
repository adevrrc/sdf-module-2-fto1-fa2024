"""
Description: The script decrypts an encrypted message entered the user in the
             terminal.
Author: Damien Altenburg
Date: 2024-9-16
Usage: python decrypter.py
"""
STEP = 2
MAXIMUM_DECRYPT_CHARACTERS = 10
STOP = STEP * MAXIMUM_DECRYPT_CHARACTERS - 1

encrypted_phrase = input("Enter the encrypted phrase: ")

# Decrypt phrase
decrypted_phrase = encrypted_phrase[0:STOP:STEP]

print(f"Decrypted: {decrypted_phrase}")
