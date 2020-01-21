# From:
# https://inventwithpython.com/chapter14.html

MAX_KEY_SIZE = 26


def getMode():
    while True:
        print("Do you wish to encrypt or decrypt a message?")
        mode = input().lower()
        if mode in "encrypt e decrypt d".split():
            return mode
        else:
            print("Please type \"encrypt/e\" or \"decrypt/d\" to continue")


def getMessage():
    print("Enter your message: ")
    return input()


def getKey():
    key = 0
    while True:
        print("Enter a key from 1 to " + str(MAX_KEY_SIZE))
        key = int(input())
        if key >= 1 and key <= MAX_KEY_SIZE:
            return key


def translateMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ""

    for letter in message:
        if letter.isalpha():
            unicode = ord(letter)
            unicode += key

            if letter.isupper():
                if unicode > ord("Z"):
                    unicode -= 26
                elif unicode < ord("A"):
                    unicode += 26
            elif letter.islower():
                if unicode > ord("z"):
                    unicode -= 26
                elif unicode < ord("a"):
                    unicode += 26

            translated += chr(unicode)
        else:
            translated += letter

    return translated


mode = getMode()
message = getMessage()
key = getKey()

print("The text has been translated to:")
print(translateMessage(mode, message, key))
