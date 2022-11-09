def wave(people):
    result = []
    for i, val in enumerate(people[:]):
        if people[i] == " ":
            i += 1
        else:
            up = people[i].upper()
            c = people[:i] + up + people[i+1:]
            result.append(c)
    return result

def main():
    people = input("Please enter string: ")
    print(wave(people))

main()
