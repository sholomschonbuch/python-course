alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(t, s):
    cipher_text = []
    alphabet2 = []
    for i in range(s, len(alphabet)):
        alphabet2.append(alphabet[i])
    for i in range(0, s):
        alphabet2.append(alphabet[i])
        
    for letter in t:
        
        i = alphabet.index(letter)
        cipher_text.append(alphabet2[i])
    print(cipher_text)
def decrypt(t, s):
    cipher_text = []
    alphabet2 = []
    for i in range(len(alphabet) - s, len(alphabet)):
        alphabet2.append(alphabet[i])
    for i in range(0, len(alphabet)):
        alphabet2.append(alphabet[i])

        
    for letter in t:
        
        i = alphabet.index(letter)
        cipher_text.append(alphabet2[i])
    print(cipher_text)
if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)