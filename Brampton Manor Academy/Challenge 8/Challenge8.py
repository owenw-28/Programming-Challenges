def main():
    roman1 = input("Enter First Roman Number (no spaces): ")
    print(f'Value of {roman1} : {romanToDig(roman1)}')
    num1 = romanToDig(roman1)
    roman2 = input("Enter Second Roman Number (no spaces): ")
    print(f'Value of {roman2} : {romanToDig(roman2)}')
    num2 = romanToDig(roman2)
    digSum = num1 + num2
    print(f'Digital sum is: {digSum}')
    print("Roman sum is:")
    digToRoman(digSum)

def romanToDig(num):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    value = 0
    while i < len(num):
        if i+1<len(num) and num[i:i+2] in roman:
            value = value + roman[num[i:i+2]]
            i+=2
        else:
            value = value + roman[num[i]]
            i+=1
    return value

def digToRoman(digSum):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while digSum:
        div = digSum // num[i]
        digSum %= num[i]
  
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1

main()
            
