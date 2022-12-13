#21.lista
def comunes(a,b):
    lista=[]
    i=0
    while i<len(a):
        if a[i] in b and a[i] not in lista:
            lista.append(a[i])
        i+=1
    return lista


d=[22,1,1,2,3,5,8,13,21,34,55,89]
e=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(comunes(d,e))