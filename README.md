Classical Encryption Ciphers

This repository contains implementations of various classical encryption ciphers. Each cipher has its own encryption and decryption algorithm, along with sample test cases.

Caesar Cipher

A shift-based substitution cipher that replaces each letter with another letter a fixed number of places down the alphabet.

Encryption: C = (P + key) mod 26

Decryption: P = (C - key) mod 26


Monoalphabetic Cipher

A substitution cipher where each letter in the plaintext is replaced with a fixed, randomly mapped letter.

Encryption: Uses a predefined substitution table.

Decryption: Reverses the substitution table.


Playfair Cipher

A digraph substitution cipher that encrypts letter pairs using a 5×5 matrix.

Encryption: Based on matrix rules (same row, column, or forming a rectangle).

Decryption: Reverse of encryption rules.


Hill Cipher

A mathematical cipher that uses matrix multiplication for encryption.

Encryption: C = K × P mod 26 (where K is the key matrix, P is the plaintext vector).

Decryption: P = K⁻¹ × C mod 26 (requires key matrix inversion).


Feistel Cipher

A structure used in modern block ciphers (e.g., DES) that performs multiple rounds of encryption.

Encryption: Repeated rounds of substitution and permutation functions with different round keys.

Decryption: Same process as encryption, but with reversed round keys.


Vigenère Cipher

A polyalphabetic substitution cipher using a repeating keyword.

Encryption: C = (P + K) mod 26 (key cycles through plaintext).

Decryption: P = (C - K) mod 26.


RSA (Rivest-Shamir-Adleman)

A widely used asymmetric encryption algorithm based on the difficulty of prime factorization.

Key Generation: Select two large prime numbers, compute modulus (n = p × q), and generate public/private keys.

Encryption: C = P^e mod n (where e is the public exponent).

Decryption: P = C^d mod n (where d is the private exponent).


Diffie-Hellman Key Exchange

A cryptographic protocol for securely exchanging cryptographic keys over a public channel.

Key Exchange Steps:

1. Two parties agree on a prime number (p) and a base (g).


2. Each party selects a private key and computes a public value (A = g^a mod p, B = g^b mod p).


3. They exchange public values and compute the shared secret (S = B^a mod p = A^b mod p).




DES (Data Encryption Standard)

A symmetric key block cipher that encrypts 64-bit blocks using a 56-bit key.

Encryption:

1. Initial Permutation (IP).


2. 16 rounds of Feistel structure (substitution, permutation, and key mixing).


3. Final Permutation (IP⁻¹).



Decryption: Follows the same process with reversed subkeys.


Usage

Each cipher has a Python implementation with functions for encryption and decryption. Run the respective script and input plaintext along with a key.



