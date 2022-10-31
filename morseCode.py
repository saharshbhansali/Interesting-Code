# fmt: off
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  # Exclamation mark is not in ITU-R recommendation
# fmt: on
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encrypt(message: str) -> str:
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())


def decrypt(message: str) -> str:
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(REVERSE_DICT[char] for char in message.split())


def main() -> None:
    
    print("Enter your choice:\n1 Get Morse code from text\n2 Get text from Morse Code")
    choice = int(input())
    if(choice==1):
        print("Enter text: ")
        message = input()
        print("Original message: " + message)
        message = encrypt(message)
        print("Morse Code: " + message)
    elif(choice==2):
        print("Enter Morse Code: ")
        message = input()
        print("Original Morse Code: " + message)
        message = decrypt(message)
        print("Text: " + message)
    else:
        print("Enter valid choice")


if __name__ == "__main__":
    main()
