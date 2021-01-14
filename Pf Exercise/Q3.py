def speed_check(speed):
    if speed <= 70:
        print("OK")
    else:
        speedo= (speed-70)//5

        if speedo < 13:
            print("Points:",speedo)
        else:
            print("License Suspended")

speed_check(135)