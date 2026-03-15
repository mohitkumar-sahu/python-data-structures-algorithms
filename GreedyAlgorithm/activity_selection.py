activities=[
    ['A1',0,6],
    ['A2',3,4],
    ['A3',1,2],
    ['A4',5,8],
    ['A5',5,7],
    ['A6',8,9]
]

def activity_selection(l1):
    l1.sort(key=lambda x:x[2])
    print(l1)
    ans_lst=[]
    ans_lst.append(l1[0])
    for i in range(len(l1)-1):
        if l1[i][2]<=l1[i+1][1]:
            ans_lst.append(l1[i+1])
    print(ans_lst)


activity_selection(activities)

