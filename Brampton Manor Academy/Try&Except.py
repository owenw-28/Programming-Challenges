import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    }

def main():
    try:
        symbol = input("Please enter an operator: +, -, * or /: ")
        num = int(input("Please enter a natural number: "))
        if symbol not in "+-*/":
            raise TypeError
        elif num <0:
            raise ValueError
    except TypeError:
        print("You did not input a valid operation")
    except ValueError:
        print("Please do not enter a number below 1")
    
        

    rows, cols = (num+1,num+1)
    matrix = [[0 for i in range(rows)]for j in range(cols)] #Initialise matrix
    firstln = [x for x in range(num+1)]
    firstln = [str(i) for i in firstln]
    print(f"{symbol} {' '.rjust(1,' ').join(firstln)}")
    print("----------------")
    for i in range(0,num+1):
        for j in range(0,num+1):
            try:
                value = ops[symbol](i,j)
                matrix[i][j] = value
            except ZeroDivisionError:
                value = "-"
                matrix[i][j] = value
            finally:
                try:
                    print(round(matrix[i][j],1),end=" ")
                except:
                    print(matrix[i][j],end=" ")
        print("\n")
    
main()



