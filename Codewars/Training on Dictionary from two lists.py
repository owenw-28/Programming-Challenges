def createDict(keys, values):
    i = 0 
    add_dict = {}
    for key in keys:
        if i >= len(values):
            values.extend([None])
        add_dict[key] = values[i]
        i += 1
    return add_dict

def main():
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]
    dictionary = createDict(keys, values)
    print(dictionary)
        
main()
