# to convert each word in list to title case

def capitalize(lst):
    res=[]
    if len(lst)==0:
        return res
    else:
        res.append(lst[0].title())
    return res + capitalize(lst[1:])
    
print(capitalize(['python','coding','is','awesome']))