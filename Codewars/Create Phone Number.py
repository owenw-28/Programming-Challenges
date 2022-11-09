def create_phone_number(n):
    first_three_digits = ""
    middle_three_digits = ""
    last_four_digits = ""
    for i in range(0,3):
        first_three_digits = first_three_digits + str(n[i])
        middle_three_digits = middle_three_digits + str(n[i+3])
    for j in range(6,10):
        last_four_digits = last_four_digits + str(n[j])
    return f'({first_three_digits}) {middle_three_digits}-{last_four_digits}'
                                                        

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
