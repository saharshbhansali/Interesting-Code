LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key value: ")
    print("Ciphertext is", translate(plaintext, key, "e"))


def decrypt():
    plaintext = input("Enter ciphertext: ")
    key = input("Enter key value: ")
    print("Plaintext is", translate(plaintext, key, "d"))


def translate(text, key, operation):
    translated = []
    key_index = 0
    key = key.upper()

    for t in text:
        num = LETTERS.find(t.upper())
        if num != -1:
            if operation == "e":
                num += LETTERS.find(key[key_index])
            elif operation == "d":
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)

            if t.isupper():
                translated.append(LETTERS[num])
            elif t.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(t)

    return ("".join(translated))

if __name__ == "__main__":
    encrypt()
    decrypt()
