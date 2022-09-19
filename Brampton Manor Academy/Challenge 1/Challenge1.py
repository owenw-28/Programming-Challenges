def metres(rods):
    metres = rods*5.0292
    return metres

def feet(rods):
    feet = metres(rods)/(1/0.3048)
    return feet

def miles(rods):
    miles = metres(rods)/1609.34
    return miles

def furlong(rods):
    furlong = rods/40
    return furlong

def time(rods):
    time = miles(rods)/3.1*60
    return time

def print_info(rods):
    f"You input {rods} rods."
    f"Conversions:"
    f"Meters: {metres(rods)}"
    f"Miles: {miles(rods)}"
    f"Feet: {feet(rods)}"
    f"Furlongs: {furlong(rods)}"
    f"Minutes to walk {rods} rods: {time(rods)}"

def main():
    rods = float(input("Input rods: "))
    print_info(rods)
main()

if __name__ == '__main__':
    run()
