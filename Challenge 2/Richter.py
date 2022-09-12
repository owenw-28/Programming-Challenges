def display():
    display1 = ['Richter', 'Joules', 'TNT']
    display2 = ['1', '1995262.3149688789', '0.00047687913837688307']
    display3 = ['5', '1995262314968.8828', '476.87913837688404']
    display4 = ['9.1', '2.818382931264449e+18', '673609687.2046962']
    display5 = ['9.2', '3.981071705534953e+18', '951498973.5982201']
    display6 = ['9.5', '1.1220184543019653e+19', '2681688466.3048882']

    for display in [display1, display2, display3, display4, display5, display6]:
        for entry in display:
            print(entry.ljust(25), end='')
        print()

def energy(richter):
    return 10**((1.5*richter)+4.8)

def TNT(joules):
    return joules/(4.184*10**9)

def main():
    print("")
    richter = float(input("Please enter a Richter scale value: "))
    joules = energy(richter)
    tons = TNT(joules)
    print("Richter value :",richter)
    print("Equivalence in joules: ",joules)
    print("Equivalence in tons of TNT: ",tons)


display()
main()
