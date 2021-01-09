def intsum(integer):
    integer=str(integer)
    sum1=0
    for i in integer:
        i=int(i)
        sum1+=i
    print("\nThe sum of ",integer," is = ",sum1)
intsum(972)