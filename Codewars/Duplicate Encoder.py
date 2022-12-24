def duplicate_encode(word):
    result = ""
    for char in word.lower():
        if word.lower().count(char) == 1:
            result += "("
        else:
            result += ")"
    return result

def main():
    word = input("Please enter string: ")
    print(duplicate_encode(word))

main()
