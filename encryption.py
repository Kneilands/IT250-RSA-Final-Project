# -*- coding: utf-8 -*-
"""
RSA Key Generation and Encryption Program

Created on Tue Nov 19 13:12:44 2024

@author: camtr
"""

import math

def is_prime(num):
    """Check if inputs are prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate the GCD of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Calculate the modular inverse of e modulo phi using the Extended Euclidean Algorithm."""
    original_phi = phi
    x0, x1 = 0, 1
    while e > 1:
        if phi == 0:
            raise ValueError("e and phi are not coprime, modular inverse does not exist")
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += original_phi
    return x1

def generate_keys():
    """Generate public and private keys."""
    while True:
        try:
            p = int(input("Enter a prime number (p): "))
            q = int(input("Enter another prime number (q): "))
            if is_prime(p) and is_prime(q) and p != q:
                break
            print("Both numbers must be prime and different.")
        except ValueError:
            print("Please enter valid integers.")

    # Compute n and phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find a suitable e (1 < e < phi(n))
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Ensure a valid 'e' was found
    if gcd(e, phi) != 1:
        print("Error: Failed to find a valid 'e'. Please try again.")
        return None

    # Calculate d as the modular inverse of e modulo phi
    try:
        d = mod_inverse(e, phi)
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

    # Ensure d is valid (1 < d < phi)
    if d <= 1 or d >= phi:
        print("Error: Failed to compute a valid 'd'. Please try again.")
        return None

    # Saves the keys to separate files
    with open("public_key.txt", "w") as pub:
        pub.write(f"{e},{n}")
    with open("private_key.txt", "w") as priv:
        priv.write(f"{d},{n}")

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    return e, n

def encrypt_message(e, n):
    """Encrypt a message using the RSA public key."""
    message = input("Enter the message to encrypt: ")
    encrypted = [pow(ord(char), e, n) for char in message]

    # Saves the encrypted message to a .txt file
    with open("ciphertext.txt", "w") as cipher_file:
        cipher_file.write(" ".join(map(str, encrypted)))

    print("Message encrypted and saved to ciphertext.txt.")
    print(f"Ciphertext: {encrypted}")

def main():
    """Main function to generate keys and encrypt a message."""
    print("RSA Key Generation and Encryption")
    keys = generate_keys()
    if keys is None:
        print("Key generation failed. Exiting...")
        return
    e, n = keys
    encrypt_message(e, n)

if __name__ == "__main__":
    main()

# Final format