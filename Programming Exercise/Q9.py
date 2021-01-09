def op(lst):
    lst2=[]

    for i in lst:
        indx=lst.index(i)

        if indx%2==1:
            lst2.append(i)

    return lst2
a=[22, 5, 7, 35, 1, 100, 15]
print(op(a))