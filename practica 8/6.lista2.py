#6.listas
def sumaListas(a):
    suma=0
    for i in range(len(a)):
        suma+=a[i]
    return suma
    
    
    
d=[3,2,6,7,8,1,9,10]
print(sumaListas(d))