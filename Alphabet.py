#HW task for Miss Chandler

def main():
    i = 0
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter = input("Input a letter of the alphabet: ")
    for i in range (0,25):
        if letter != alphabet[i]:
            i = i + 1
        else:
            print("You inputted",letter)
            place = position(i)
            print(letter,"is the",place,"letter of the alphabet")

def position(i):
    i = i + 1
    if i == 1 or i == 21:
        return str(i)+"st"
    elif i == 2 or i == 22:
        return str(i)+"nd"
    elif i == 3 or i == 23:
        return str(i)+"rd"
    else:
        return str(i)+"th"

main()
