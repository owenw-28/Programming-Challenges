def main():
    string = input("Input string: ")
    hist = histogram(string)
    print(str(hist))
    
    for key, value in sorted(hist.items() ):
print(f'The letter {key} appears {value} time.')


def histogram(string):
    hist = {}
      
    for i in string:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    return hist

main()


