def move_zeros(lst):
    res = []
    count = 0
    for val in lst:
        if val != 0:
            res.append(val)
        else:
            count += 1
    for i in range(count):
        res.append(0)
    return res

if __name__=='__main__':
    print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
