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
    i = 0
    matrix = [[0 for i in range(rows)]for j in range(cols)] #Initialise matrix
    for row in matrix:
        j = 0
        matrix[i][j] = i
        for col in matrix:
            while j <= cols and symbol == "+":
                j+=1
                matrix[i][j] = i+j #Gets index error
               
        print(row)
        
        
    
main()

