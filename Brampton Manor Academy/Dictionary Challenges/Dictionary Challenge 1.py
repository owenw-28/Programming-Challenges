def main():
    months = {
        'JAN': 1, 'FEB': 2, 'MAR': 3,
        'APR': 4, 'MAY': 5, 'JUN': 6,
        'JUL': 7, 'AUG': 8, 'SEP': 9,
        'OCT': 10, 'NOV': 11, 'DEC': 12
        }
    date = input(f"Input date in dd-mmm-yy format: ")
    split = date.split('-')
    result = SplitDate(split,months)
    print(result)


def SplitDate(split,months):
    month = months[split[1]]
    return (split[0],month,split[2])

main()

