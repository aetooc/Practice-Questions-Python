def ftn(num,lst):
    if lst[0]<lst[1]:
        for element in lst:
            if element>num:
                a=lst.index(element)
                lst.insert(a,num)
                break
        print(lst)
    else:
        for element in lst:
            if element<num:
                a=lst.index(element)
                lst.insert(a,num)
                break
        print(lst)


num=4
a=[22,9,5,3,1]
ftn(num,a)