def tribonacci(signature, n):
    result = signature
    first = signature[0]
    second = signature[1]
    third = signature[2]
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0],signature[1]]
    elif n == 3:
        return [signature[0],signature[1],signature[2]]
    else:
        for i in range(4,n+1):
            next = first+second+third
            result.append(next)
            first = second
            second = third
            third = next
        return result
        
if __name__ == '__main__':
    print(tribonacci([1,1,1],10))
