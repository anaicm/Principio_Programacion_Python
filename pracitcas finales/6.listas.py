def sumaLista(a):
    suma=0
    for i in range(len(a)):
        suma+=a[i]
    return suma
d=[1,2,2,3,4]
print(sumaLista(d))