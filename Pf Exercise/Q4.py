def showNumbers(limit):
    for i in range(limit+1):
        if i == 0:
            print(i, "Zero")
        elif i % 2 == 1:
            print(i, "Odd")
        else:
            print(i,"Even")
showNumbers(3)