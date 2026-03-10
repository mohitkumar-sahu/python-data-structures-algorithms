def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

l=[1,3,2,4,5,9,8,7]
print(selection_sort(l))