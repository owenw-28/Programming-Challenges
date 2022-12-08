def bouncing_ball(h, bounce, window):
    count = 1
    if h >0 and bounce >0 and bounce <1 and window < h:
        while h > window:
            h = h*bounce
            if h > window:
                count += 2
        return count
    else:
        return -1

def main():
    h = float(input("Please enter height above ground floor in meters: "))
    bounce = float(input("Please enter the bounce of the ball: "))
    window = float(input("Please enter the height of the window: "))
    if bouncing_ball(h, bounce, window) >0:
        print(f'The ball is seen {bouncing_ball(h, bounce, window)} times through the window')
    else:
        print("Unknown Error")

main()


