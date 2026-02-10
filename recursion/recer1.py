# factorial of given num using recursion

def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return num * fact(num-1)
    
print(fact(5))
print(fact(4))

