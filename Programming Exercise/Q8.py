def reverselst(lst):
    lst2=[]
    count=1
    for i in lst:
        a=lst[-count]
        count+=1
        lst2.append(a)
    return lst2
a=[-1, 5, 7, 35, 1, 100, 15]
print(reverselst(a))