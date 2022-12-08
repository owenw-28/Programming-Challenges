def solution(number):
    total = 0
    for i in range(0,number):
        if i % 3 ==0 or i % 5 ==0:
            total+=i
    return total
    pass

def main():
    number = int(input("Please enter a natural number: "))
    print(f'The sum of multiples of 3 or 5 up to this number is: {solution(number)}')

main()
