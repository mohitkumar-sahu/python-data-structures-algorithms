def linear_search(l1,val):
    for i in range(len(l1)):
        if l1[i]==val:
            return i
    else:
        return -1
    
l1=[1,3,5,7,9,10,8,2,22]
print(linear_search(l1,22))