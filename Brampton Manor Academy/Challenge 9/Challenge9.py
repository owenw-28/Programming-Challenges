def main():
    x1 = int(input('Enter the x coordinate for the first point: '))
    y1 = int(input('Enter the y coordinate for the first point: '))
    x2 = int(input('Enter the x coordinate for the second point: '))
    y2 = int(input('Enter the y coordinate for the second point: '))
    m1 = gradient(0, 0, x1, y1)
    m2 = gradient(x1, y1, x2, y2)
    print(f'The angle between the two lines is {abs(angle(m2, m1))}')
    turtle(x1, x2, y1, y2, m1, m2)

def turtle(x1, x2, y1, y2, m1, m2):
    import turtle
    turtle.goto(x1, y1)
    turtle.goto(0,0)
    turtle.goto(x2, y2)
    turtle.done()

def gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def angle(m2, m1):
    import math
    tan_angle = abs((m2 - m1)) / (1 + m1*m2)
    radAngle = math.atan(tan_angle)
    degAngle = radAngle*(180 / math.pi)
    return degAngle

main()
