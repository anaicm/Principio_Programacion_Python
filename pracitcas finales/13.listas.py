def primerDesordenado(a):
    desordenado=0
    for i in range (len(a)-1):
        if a[i]>a[i+1]:
            desordenado=a[i]
    return desordenado
d=[1,4,6,5,8]
print(primerDesordenado(d))