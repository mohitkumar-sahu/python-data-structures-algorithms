# sum of list element
def sumoflist(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+sumoflist(lst[1:])

print(sumoflist([1,2,3,4,5]))

# product of list element
def prodoflist(lst):
    if len(lst)==0:
        return 1
    else:
        return lst[0]*prodoflist(lst[1:])

print(prodoflist([1,2,3,4,5]))