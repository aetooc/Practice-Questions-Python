def op(lst,num):
    emp_list=[]
    for element in lst:
        if num%element==0:
            emp_list.append(element)
    if emp_list== []:
        print("No Divisors Found")
    else:
        print("Here are the Divisors of Number:",num)
        for element in emp_list:
            print(element)
a=[1,2,3,4,5,6]
num=6
op(a,num)
