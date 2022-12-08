def count_bits(n):
    binary = format(n, 'b')
    return binary.count('1')

def main():
    n = int(input("Please enter an integer: "))
    print(f'There are {count_bits(n)} occurences of 1s in the binary representation of this number')

main()
