def main():
    choice = input("Do you wish to encrypt or decrypt a message?\n")
    message = input("Enter your message:\n")
    key = int(input("Enter the key number (1-26):\n"))
    if choice == "encrypt":
        print(encryption(message, key))
    elif choice == "decrypt":
        print(decryption(message, key))
    else:
        print("Invalid choice entered")

def encryption(message, key):
    result = ""
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                result += chr((ord(message[i]) + key-65) % 26+65)
            else:
                result += chr((ord(message[i]) + key-97) % 26+97)
        else:
            result += message[i]
    return result

def decryption(message, key):
    result = ""
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                result += chr((ord(message[i]) - key-65) % 26+65)
            else:
                result += chr((ord(message[i]) - key-97) % 26+97)
        else:
            result += message[i]
    return result

main()
