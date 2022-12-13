#13.listas
def primerDesordenado(a):
    i=0
    desordenado=0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            desordenado=i
        i+=1
    return desordenado
    
    

d=[1,4,6,5,8]
print(primerDesordenado(d))
    
