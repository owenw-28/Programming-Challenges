import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    }

def main():
    symbol = input("Please enter an operator: +, -, * or /: ")
    num = int(input("Please enter a natural number: "))
    if symbol not in "+-*/" or num <0:
        raise Exception
    
    matrix = [[0 for x in range(1)] for y in range(num)]
    for i in range(0,num+1):
        print(matrix)
        #for j in range(0,num+1):
        
    
main()
