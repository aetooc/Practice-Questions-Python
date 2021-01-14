def ftn(limit):
    sum=0
    for i in range(1,limit+1):
        if i%3==0 or i%5==0:
            sum+=i
            print(i)
    print("Total sum is =",sum)
ftn(20)
    