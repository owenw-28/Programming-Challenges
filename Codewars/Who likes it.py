def likes(names):
    num = len(names)
    if num == 0:
        return "no one likes this"
    elif num == 1:
        return(f'{names[0]} likes this')
    elif num == 2:
        return(f'{names[0]} and {names[1]} like this')
    elif num == 3:
        return(f'{names[0]}, {names[1]} and {names[2]} like this')
    elif num >= 4:
        rem = num - 2
        return(f'{names[0]}, {names[1]} and {rem} others like this')

def main():
    names = ["Alex", "Jacob", "Mark", "Max", "Owen"]
    statement = likes(names)
    print(statement)

main()

