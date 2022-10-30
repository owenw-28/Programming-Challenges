def calculation(interest, repayment):
    debt = 100
    total = 0
    count = 0
    while debt > 0:
        debt = debt + (debt * (interest / 100))
        paid = debt * (repayment / 100)
        if paid > 50:
            debt = debt - paid
            total = total + paid
        else:
            debt = debt - 50
            if debt < 0:
                total = total + debt + 50
            else:
                total = total + 50
        count += 1
    return round(total, 2), count


def main():
    interest = int(input("Please enter interest rate: "))
    repayment = int(input("Please enter repayment rate: "))
    total, count = calculation(interest, repayment)
    print(f'Total amount paid off: {total}')
    print(f'Number of payments: {count}')

main()
