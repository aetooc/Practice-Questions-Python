def prime(num):
    for j in range (1,num+1):

        for i in range(2,j):
            if j%i == 0:
                break
        else:
            print(j,"is a prime number")
prime(23)