import string
alphabet = list(string.ascii_uppercase)

ciphertext = list(input())
key = list(input())
message = ""

while len(ciphertext) != 0:
    letter = alphabet[alphabet.index(ciphertext.pop(0)) - alphabet.index(key.pop(0))]
    message = message + letter
    key.append(letter)

print(message)