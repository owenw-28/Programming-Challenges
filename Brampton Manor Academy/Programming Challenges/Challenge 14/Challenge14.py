import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '//' : operator.floordiv,
    '%' : operator.mod,
    '**' : operator.xor,
}

def calculate(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)

def main():
    while True:
        string = input("Enter your calculation: ")
        if string == "q":
            return
        try:
            operand1, operand2, operator = string.split()
            print(calculate(operand1, operator, operand2))
            break
        except (ValueError, NameError):
            print("Please enter in format: operand operand operator")
            print()

        

main()
