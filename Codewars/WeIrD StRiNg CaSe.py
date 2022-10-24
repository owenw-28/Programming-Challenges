def to_weird_case(string): #reset at new word
    count = 0
    result = ''
    for letter in string:
        if letter == ' ':
            result += ' '
            count = 0 
        else:
            if count % 2 != 0: 
                letter = letter.lower()
                result += letter
            else: 
                letter = letter.upper()
                result += letter
            count += 1
    return result

def to_weird_case(words): #keep at new word
    newstring = ""
    for i in range(len(words)):
        if i % 2 == 0:
           newstring = newstring + words[i].upper()
        else:
           newstring = newstring + words[i].lower()
    return newstring
    pass

def main():
    words = input("Please enter a string: ")
    print(to_weird_case(words))

main()
