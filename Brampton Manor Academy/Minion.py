def main():
    string = input("Enter a word: ")
    valid = validate(string)
    if valid == True:
        string = string.upper()
        constanants(string)
    else:
        raise Exception
    
    
def validate(string):
    return string.isalpha()

def constanants(string):
    const_list = []
    const = "BCDFGHJKLMNPQRSTVWXYZ"
    for i in range(0,len(string)):
        if string[i] in const:
            const_list.append(string[i])
    print(const_list)
       
main()
            
            
        
        
