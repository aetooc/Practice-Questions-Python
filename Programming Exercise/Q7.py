def E_O_Z(integer):
    if integer > 0:
        integer=str(integer)
        E,O,Z=0,0,0
        for i in integer:
            i=int(i)
            if i==0:
                Z+=1
            if i>0:
                if i%2==0:
                    E+=1
                else:
                    O+=1
        print("Even: ",E,"\nZero: ",Z,"\n Odd: ",O)
    else:
        print("\nTry Again, Choose a positive integer")

E_O_Z(-101)
