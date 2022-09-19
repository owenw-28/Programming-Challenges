def calculate(slayer,layers):
    layers = str(layers)
    slayer = str(slayer)
    if slayer[0] == layers[5] and slayer[1] == layers[0] and slayer[2] == layers[1] and slayer[3] == layers[2] and slayer[4] == layers[3] and slayer[5] == layers[4]:
        result = True
    else:
        result = False
    return result


def main():
    print(f"Guess a six-digit number SLAYER so that following equation is true, where each 1 letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS")
    slayer = int(input(f"Enter your guess for SLAYER: "))
    layers = slayer + slayer + slayer
    result = calculate(slayer,layers)
    if result == True:
        print(f"Your guess is correct: ")
        print(f"SLAYER + SLAYER + SLAYER = {layers}")
        print(f"LAYERS = {layers}")
        print(f"Thanks for playing.")
    else:
        print(f"Your guess is incorrect: ")
        print(f"SLAYER + SLAYER + SLAYER = {layers}")
        print(f"LAYERS = {layers}")
        print(f"Thanks for playing.")
        
main()
