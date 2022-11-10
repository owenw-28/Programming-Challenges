import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

def main():
    s = input("Please enter a string: ")
    if is_pangram(s) == True:
        print(f'"{s}" is a pangram')
    else:
        print(f'"{s}" is not a pangram')

main()
