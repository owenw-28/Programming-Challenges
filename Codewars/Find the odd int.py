def find_it(seq):
    for i in range(len(seq)):
        occurences = seq.count(seq[i])
        if occurences % 2 == 1:
            return seq[i]

if __name__ == '__main__':
    print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
