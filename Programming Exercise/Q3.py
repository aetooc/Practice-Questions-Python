def check(lst):
    emp_lst=[]
    count=0
    for element in lst:

        if element == 1:
            count+=1
            k=lst.index(element)
            emp_lst.append(k)

        # Here if element is > 1 then we will check if it is completly divisible then we'll just break the loop but
        # if it is not divisible in his domain then it is prime so we'll go to else statement

        if element >1:
            for i in range(2,element):
                if element%i==0:
                    break

            else:
                count+=1
                k=lst.index(element)
                emp_lst.append(k)

    print("There are ",count," Prime Numbers at indexes ", emp_lst)
    
a=[1,2,3,9,5,11,8]
check(a)