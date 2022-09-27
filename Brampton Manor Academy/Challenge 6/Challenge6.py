def main():
    n = int(input(f"Please input the order of square: "))
    top_left = int(input(f"Please input the top left number: "))
    result = latin_square(n,top_left)
    print(f"The Latin Square is:")
    i = 0
    for i in range(0,len(result)):
        print (result[i])
        i += 1

def latin_square(n,top_left):
    row = [i for i in range(1, n+1)]
    row = row[top_left-1:] + row[:top_left-1]
    return [row[i:] + row[:i] for i in range(n)]

main()
