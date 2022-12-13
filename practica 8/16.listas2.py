#16.listas
def primerCima(a):
    i=0
    while i<len(a):
        if a[i-1]<a[i] and a[i+1]<a[i]:
            return i
        i+=1
    return -1
    
    
d=[1,4,6,5,8]
print(primerCima(d))