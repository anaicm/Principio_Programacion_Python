def primeraCima (a):
    
    for i in range(len(a)):
        if a[i-1]<a[i] and a[i-1]<a[i]:
    
            return a[i]
    return -1
            
    
d=[1,4,6,5,8]
print(primeraCima(d))