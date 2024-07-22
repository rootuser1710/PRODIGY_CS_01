import string

def check():
    notice = input("press 'e' to encrypt, 'd' to decrypt and 'q' to quit:  ")
    if notice.lower() == 'e':
        return encrypt()
    elif notice.lower() == 'd':
        return decrypt()
    elif notice.lower() == 'q':
        return exit()
    else:
        print('Invalid Choice, Try Again')
        return check()

def caesar(text, shift, alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def encrypt():
    phrase = input("what would you want to Encrypt? ")
    print(caesar(phrase, 3, [string.ascii_lowercase, string.ascii_uppercase,string.digits, string.punctuation]))
    check()

def decrypt():
    phrase = input("what would you want to Decrypt? ")
    print(caesar(phrase, -3, [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]))
    check()

if __name__ == '__main__':
    print("CAESAR CIPHER ENCRYPTION/DECRYPTION PROGRAM")
    print()
    check()
