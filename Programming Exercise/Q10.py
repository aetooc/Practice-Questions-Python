def s_maxL(lst):
    lst.sort()              # Sorting List
    length=len(lst)-2       # Length-2 because start by 0 index
    return lst[length]      # Returning second max value
    
a=[22, 5, 7, 35, 1, 21, 15]
print(s_maxL(a))