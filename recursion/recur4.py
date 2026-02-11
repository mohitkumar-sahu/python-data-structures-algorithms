# program to sum of n natural num.

def natural_sum(num):
    if num==1:
        return 1
    else:
        return num+natural_sum(num-1)


print(natural_sum(10))