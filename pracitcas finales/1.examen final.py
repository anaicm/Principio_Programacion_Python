def purga(a):
    c=[]
    for i in range(len(a)):
        if a[i] not in c:
            c.append(i)
    return c
    
    
d=[2,1,2,3,1,2]
print(purga(d))