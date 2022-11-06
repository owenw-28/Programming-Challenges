def main():
    num1 = int(input("Integer 1: "))
    num2 = int(input("Integer 2: "))
    calculate(num1,num2)

def calculate(num1,num2):
    numPalindrome = 0
    notLychrel = 0
    numLychrel = 0
    for i in range(num1,(num2)+1):
        number = str(i)
        reversal = number[::-1] #counts from end to beginning by -1
        count = 0
        while number != reversal and count <= 60:
            number = str(int(number) + int(reversal))
            reversal = number[::-1]
            count +=1
        if count > 60:
            print(i,'is probably lychrel')
            numLychrel +=1
        elif count == 0:
            numPalindrome +=1
        else:
            notLychrel +=1
    print()
    print(f'Palindrome numbers: {numPalindrome}')
    print(f'Not Lychrel numbers: {notLychrel}')
    print(f'Lychrel: {numLychrel}')

main()
