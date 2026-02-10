# sum of given num

def num_sum(num):
    if num==0:
        return 0
    else:
        return num%10+num_sum(num//10)

print(num_sum(1234))
    

