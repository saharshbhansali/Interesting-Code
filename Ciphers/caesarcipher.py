def encrypt():
    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key value: "))
    print("Ciphertext is", translate(plaintext, (key%26), "e"))


def decrypt():
    ciphertext = input("Enter ciphertext: ")
    key = int(input("Enter key value: "))
    print("Plaintext is", translate(ciphertext, (26-key%26), "d"))


def translate(text, key, operation):
    translated = []
    for t in text:
        if t.isupper():
            translated.append(chr((ord(t) + key - 65) % 26 + 65))
        elif t.islower():
            translated.append(chr((ord(t) + key - 97) % 26 + 97))
        else:
            translated.append(t)
    return ("".join(translated))


if __name__ == "__main__":
    encrypt()
    decrypt()
