# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:13:46 2024

@author: camtr
"""

def decrypt_message():
    """Decrypt the message using the private key."""
    try:
        # Load the private key (d, n) from file
        with open("private_key.txt", "r") as priv_file:
            d, n = map(int, priv_file.read().strip().split(","))
    except FileNotFoundError:
        print("Error: private_key.txt not found.")
        return
    except ValueError:
        print("Error: private_key.txt format is incorrect. Expected format: d,n")
        return

    print(f"Loaded private key: d = {d}, n = {n}")

    try:
        # Load the ciphertext from .txt file
        with open("ciphertext.txt", "r") as cipher_file:
            ciphertext = list(map(int, cipher_file.read().strip().split()))
    except FileNotFoundError:
        print("Error: ciphertext.txt not found.")
        return
    except ValueError:
        print("Error: ciphertext.txt format is incorrect. Expected space-separated integers.")
        return

    print(f"Loaded ciphertext: {ciphertext}")

    # Decrypt each number in the ciphertext using the formula M = C^d % n
    try:
        decrypted_chars = [chr(pow(c, d, n)) for c in ciphertext]
    except ValueError as ve:
        print(f"Error during decryption: {ve}")
        return

    # Join the characters to form the plaintext
    decrypted_message = ''.join(decrypted_chars)

    # Display the decrypted message
    print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    print("RSA Decryption")
    decrypt_message()
    
# Final format
