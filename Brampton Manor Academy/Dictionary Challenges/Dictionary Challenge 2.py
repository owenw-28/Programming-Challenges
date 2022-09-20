def main():
    string = input("Input string: ")
    hist = histogram(string)
    print(str(hist))
"""
    end = len(hist)-1
    while end >= 0:
        value = string[end]
        print(f"The letter {string[end]} appears {dict.get(hist[end])} times")
        end = end - 1
"""

def histogram(string):
    hist = {}
      
    for i in string:
        if i in hist:
            hist[i] += 1
        else:
            hist[i] = 1
    return hist

main()

#Creating dictionary works, but cannot output
