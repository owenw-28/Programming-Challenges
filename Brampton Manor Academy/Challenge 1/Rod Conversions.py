"""
def convert(rods):
    metres = rods*5.0292
    feet = (rods*5.0292)/(1/0.3048)
    miles = ((rods*5.0292)/1609.34)
    furlong = rods/40
    time = (miles/3.1)*60
    return metres, feet, miles, furlong, time
    

rods = float(input("Input rods: "))
print("You input",rods,"rods.")
metres, feet, miles, furlong, time = convert(rods)
print("Conversions")
print("Meters: ",metres)
print("Miles: ",miles
print("Feet: ",miles)
print("Furlongs: ",furlong)
print("Minutes to walk ",rods,"rods: ",time)
"""

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
    print("You input",rods,"rods.") 
    print("Conversions")
    print("Meters: ",metres(rods))
    print("Miles: ",miles(rods))
    print("Feet: ",feet(rods))
    print("Furlongs: ",furlong(rods))
    print("Minutes to walk ",rods,"rods: ",time(rods))

def main():
    rods = float(input("Input rods: "))
    print_info(rods)
main()
