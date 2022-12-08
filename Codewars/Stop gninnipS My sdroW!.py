def spin_words(sentence):
    arr = sentence.split()
    result = []
    for i in range(len(arr)):
        if len(arr[i]) >= 5:
            arr[i] = arr[i][::-1]
            result.append(arr[i])
        else:
            result.append(arr[i])
    x = " ".join(result)
    return x

def main():
    sentence = input("Please enter a sentence: ")
    print(spin_words(sentence))

main()
