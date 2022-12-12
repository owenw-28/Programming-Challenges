def find_outlier(integers):
    listEven = []
    listOdd = []
    for n in integers:
        if n % 2 == 0:
            listEven.append(n)
        else:
            listOdd.append(n)
            
    if len(listEven) == 1:
    	return listEven[0]
    else:
    	return listOdd[0]

if __name__ == '__main__':
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
