small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big_letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V','B', 'N', 'M']

#Encoding
def encode(plain_text):
    encrypted_code = ""
    for i in plain_text:
        if i < 'a' or i > 'z':
            continue
        for j in range(26):
            if i == small_letters[j]:
                encrypted_code += big_letters[j]
                break
    return encrypted_code

#Decoding
def decode(cipher_text):
    decrypted_code = ""
    for i in cipher_text:
        if i < 'A' or i > 'Z':
            decrypted_code += i
            continue
        for j in range(26):
            if i == big_letters[j]:
                decrypted_code += small_letters[j]
                break
    return decrypted_code

plain_text = input("Enter plain text: ")
print(encode(plain_text))
cipher_text = input("Enter the cipher text: ")
print(decode(cipher_text))