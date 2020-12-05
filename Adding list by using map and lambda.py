num1= [1,2,3]
num2= [4,5,6]
num3= [7,8,9]
print('Original list: ')
print(num1)
print(num2)
print(num3)
result=map(lambda x, y, z: x + y + z, num1, num2, num3)
print('\nNew list after adding above three lists:')
print(list(result))

# When you will run this program then the output will look like this

#Output:

Original list: 
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

New list after adding above three lists:
[12, 15, 18]
