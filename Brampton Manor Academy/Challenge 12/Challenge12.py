def main():
    while True:
        print("")
        cardNum = input("Please enter card number: ")
        if not cardNum.isnumeric():
            print("Card number must be just numbers")
            continue
        if len(cardNum) < 16:
            print("too short")
            continue
        elif len(cardNum) > 16:
            print("too long")
            continue
        else:
            print(f'The PAN is {cardNum[7:15]}')
            print(f'The checksum digit is {cardNum[-1]}')
            issuer = issue(cardNum)
            if issuer == None:
                print("There is no issuer")
                continue
            else:
                print(f'The issuer is {issuer}')
            cardVerify = luhnAlgorithm(cardNum)
            if cardVerify:
                print("The card number is real")
            else:
                print("The card number is not real")
            break

def issue(cardNum):
    MCsecondDigits = "12345"
    if cardNum[:2] == "34" or cardNum[:2] == "37":
        return "American Express"
    elif cardNum[:1] == "3" and (cardNum[1] != "4" or cardNum[1] != "7"):
        return "JCB"
    elif cardNum[0] == "4":
        return "Visa"
    elif cardNum[:1] == "5" and (cardNum[1] in MCsecondDigits):
        return "MasterCard"


def luhnAlgorithm(cardNum):
    sum = 0
    num_digits = len(cardNum)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(cardNum[count])

        if not ((count & 1) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ((sum % 10) == 0)
    
main()
