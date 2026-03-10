# bucket_sort.py

import math
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def bucket_sort(arr):
    total_bucket=round(math.sqrt(len(arr)))
    print(total_bucket)

    buckets=[]
    for _ in range(total_bucket):
        buckets.append([])
    print(buckets)

    max_ele=max(arr)
    for i in range(len(arr)):
        idx=math.ceil((arr[i]*total_bucket)/max_ele)
        buckets[idx-1].append(arr[i])
    print(buckets)

    for i in range(total_bucket):
        buckets[i]=bubble_sort(buckets[i])
    print(buckets)

    k=0
    for i in range(total_bucket):
        for j in range(len(buckets[i])):
            arr[k]=buckets[i][j]
            k+=1



l=[1,2,3,4,5,8,7,6]
bucket_sort(l)
print(l)