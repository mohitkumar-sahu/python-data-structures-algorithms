# Coin change Problem using Greedy approch
l=[1,2,5,10,20,50,100,200,500,1000]
amount=4532
def min_num_of_coin(l1,amount):
    count=0
    for i in range(len(l1)-1,-1,-1):
        if l1[i]<=amount:
            div=amount//l1[i]
            print(f"{l1[i]} * {div}")
            count+=div
            amount-=div*l1[i]
    return count

# using for loop
def min_num_of_coin2(coins,amount):
    coins.sort()
    idx=len(coins)-1
    n=amount
    cnt=0
    while True:
        coinvalue=coins[idx]
        if amount>=coinvalue:
            cnt+=1
            print(coinvalue)
            amount-=coinvalue
        if amount<coinvalue:
            idx-=1
        if amount==0:
            print(f'Mininum no of coin',{cnt})
            break

min_num_of_coin2(l,4837)
# print(f"Total coin : {min_num_of_coin(l,amount)}")