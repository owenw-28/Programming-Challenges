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

    rows, cols = (num+1,num+1)
    matrix = [[0 for i in range(rows)]for j in range(cols)] #Initialise matrix
    for i in range(0,num+1):
        for j in range(0,num+1):
            value = ops[symbol](i,j)
            matrix[i][j] = value
            print(matrix[i][j],end=" ")
        print("\n")
        
        
    
main()


