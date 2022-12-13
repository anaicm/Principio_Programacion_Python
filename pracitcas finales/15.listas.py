def hayRepes(a):
    hay=False
    for i in range (len(a)-1):
        for j in range(len(a)-1):
            if i!=j and a[j]==a[i]:
                hay=True
    return hay
    
    
    
d=[1,2,5,8,4,8,6,3]
print(hayRepes(d))