def binary_search(l1,val):
    start=0
    end=len(l1)-1
    while(start<=end):
        mid=(start+end)//2
        if l1[mid]==val:
            return mid
        elif l1[mid]>val:
            end=mid-1
        else:
            start=mid+1
    return -1

l1=[1,2,3,4,5,7,9,10,12,13]
print(binary_search(l1,13))