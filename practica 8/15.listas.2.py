#15.listas
def hayRepes(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j and a[i]==a[j]:
                return True
    return False
    
    
d=[3,2,8,7,6,1,9,10]
print(hayRepes(d))
