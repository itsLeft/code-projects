"""
Josh S
Input
Ask the user for the secret message they want to encrypt.
Then ask how many positions in the alphabet to shift each character.

Output
Print the encrypted messaged (the ciphertext).
Decrypt the ciphertext and print the original message (the plaintext).
"""

secretMessage = input("Please enter your secret message: ")
shiftIndex = int(input("How many characters do you want to shift by (1-26): "))
while shiftIndex < 1 or shiftIndex > 26:
    shiftIndex = int(input("How many characters do you want to shift by (1-26): "))

def encode(message, shifter):
    encoded = []
    fix = message.lower()
    encodedMsg = ""
    for i in range(len(fix)):
        x = ord(fix[i])
        y = fix[i]
        if x == 32:
            encoded.insert(i, " ")
        else:
            x += shifter
            if x > 122:
                x = 96 + (x - 122)
            b = chr(x)
            encoded.insert(i, b)
    for letter in encoded:
        encodedMsg += letter
    return encodedMsg

print(f"Encrypted: {encode(secretMessage, shiftIndex)}")

