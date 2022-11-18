def camel_case(string):
    arr = string.split()
    result = ""
    for i in range(len(arr)):
        newWord = arr[i][0].upper() + arr[i][1::]
        result = result + newWord
    return result

def main():
    string = input("Please enter string: ")
    print(camel_case(string))

main()
