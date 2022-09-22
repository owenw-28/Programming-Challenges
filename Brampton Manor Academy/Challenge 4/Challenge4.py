def main():
        print(f"Temperature of 10 and speed of 15 gives windchill of: {calculate(10,15)}")
        print(f"Temperature of 0 and speed of 25 gives windchill of: {calculate(0,25)}")
        print(f"Temperature of -10 and speed of 35 gives windchill of: {calculate(-10,35)}")
        temp = float(input("Temperature: "))
        speed = float(input("Speed: "))
        windchill = calculate(temp,speed)
        print(f"Windchill: {windchill}")

def calculate(temp,speed):
    return 35.74 + 0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16

main()


