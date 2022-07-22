alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesor(ed, t, s):
    cipher_string = ""
    alphabet2 = []
    if ed == "encode":
        for i in range(s, len(alphabet)):
            alphabet2.append(alphabet[i])
        for i in range(0, s):
            alphabet2.append(alphabet[i])
        for letter in t:
            i = alphabet.index(letter)
            cipher_string += alphabet2[i]
    elif ed == "decode":
        for i in range(len(alphabet) - s, len(alphabet)):
            alphabet2.append(alphabet[i])
        for i in range(0, len(alphabet)):
            alphabet2.append(alphabet[i])
        for letter in t:
            i = alphabet.index(letter)
            cipher_string += alphabet2[i]
    
    print(cipher_string)
caesor(ed = direction, t = text, s = shift)