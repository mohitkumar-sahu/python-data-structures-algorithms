def merge_sort(l1):
    if len(l1)>1:
        mid=len(l1)//2
        left_half=l1[:mid]
        right_half=l1[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        #start merging
        i,j,k=0,0,0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                l1[k]=left_half[i]
                i+=1
            else:
                l1[k]=right_half[j]
                j+=1
            k+=1
            # check any of elem remaining in both list
            while i<len(left_half):
                l1[k]=left_half[i]
                i+=1
                k+=1
            while j<len(right_half):
                l1[k]=right_half[j]
                j+=1
                k+=1
                
l1=[4,8,1,6,7,3,5,9]
print('Befour sorting ->',l1)
merge_sort(l1)
print('After sorting ->',l1)