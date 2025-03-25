# Diffie Hellman
import random
def diffie_hellman(p, g, private_key):
 return pow(g, private_key, p) # Modular exponentiation
# Publicly shared prime number and generator
global_p = 23 # Prime number
global_g = 5 # Generator
# Private keys chosen by both parties
private_key_A = random.randint(1, global_p - 1)
private_key_B = random.randint(1, global_p - 1)
# Public keys computed by each party
public_key_A = diffie_hellman(global_p, global_g, private_key_A)
public_key_B = diffie_hellman(global_p, global_g, private_key_B)
# Shared secret computation
shared_secret_A = pow(public_key_B, private_key_A, global_p)
shared_secret_B = pow(public_key_A, private_key_B, global_p) # Fixed
# Display results
print("Public Key A:", public_key_A)
print("Public Key B:", public_key_B)
print("Shared Secret (computed by A):", shared_secret_A)
print("Shared Secret (computed by B):", shared_secret_B)
# Ensure both computed shared secrets match
assert shared_secret_A == shared_secret_B, "Shared secrets do not 
match!"
print("Key exchange successful!")