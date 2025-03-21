Classical Encryption Ciphers

This repository contains implementations of various classical encryption ciphers. Each cipher has its own encryption and decryption algorithm, along with sample test cases.

1. Caesar Cipher

A shift-based substitution cipher that replaces each letter with another letter a fixed number of places down the alphabet.

Encryption: C = (P + key) mod 26

Decryption: P = (C - key) mod 26


2. Monoalphabetic Cipher

A substitution cipher where each letter in the plaintext is replaced with a fixed, randomly mapped letter.

Encryption: Uses a predefined substitution table.

Decryption: Reverses the substitution table.


3. Playfair Cipher

A digraph substitution cipher that encrypts letter pairs using a 5×5 matrix.

Encryption: Based on matrix rules (same row, column, or forming a rectangle).

Decryption: Reverse of encryption rules.


4. Hill Cipher

A mathematical cipher that uses matrix multiplication for encryption.

Encryption: C = K × P mod 26 (where K is the key matrix, P is the plaintext vector).

Decryption: P = K⁻¹ × C mod 26 (requires key matrix inversion).


5. Feistel Cipher

A structure used in modern block ciphers (e.g., DES).

Encryption: Uses multiple rounds of substitution and permutation.

Decryption: Same process as encryption with reverse round keys.


6. Vigenère Cipher

A polyalphabetic substitution cipher using a repeating keyword.

Encryption: C = (P + K) mod 26 (key cycles through plaintext).

Decryption: P = (C - K) mod 26.


Usage

Each cipher has a Python implementation with functions for encryption and decryption. Run the respective script and input plaintext along with a key.

