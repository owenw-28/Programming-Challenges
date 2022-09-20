def main():
    i = 0
    months = {
        'JAN': 1, 'FEB': 2, 'MAR': 3,
        'APR': 4, 'MAY': 5, 'JUN': 6,
        'JUL': 7, 'AUG': 8, 'SEP': 9,
        'OCT': 10, 'NOV': 11, 'DEC': 12
        }
    date = input(f"Input date in dd-mmm-yy format: ")
    result = SplitDate(months,date)
    print(result)


def SplitDate(months,date):
    for i in range (0,11):
        if months[i] == date[3,4,5]:
            month = months[i]
        else:
            i = i + 1
    mytuple = tuple(date[0,1],month,date[6,7])
    return mytuple

main()

#Does not work, I do not know what to do
