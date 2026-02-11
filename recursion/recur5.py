def palindrome(str):
    if len(str)==1:
        return str
    else:
        return str[-1]+palindrome(str[:-1])


str='madam'
if str==palindrome(str):
    print(palindrome)
else:
    print('Not palindrome')


