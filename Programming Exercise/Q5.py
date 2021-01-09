def check(lst,lst1):
    for i in lst:
        for j in lst1:
            if i ==j:
                return True
    

a=[1,2,3,4,5]
b=[2,7,2,9,0]
print(check(a,b))