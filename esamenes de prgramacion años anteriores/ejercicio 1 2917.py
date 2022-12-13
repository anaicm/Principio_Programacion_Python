def leefich(nombFich):
    f=open(nombFich)
    lista=[]
    for i in f:
        for j in i.strip().split():
            lista.append(float(j))
    return lista
def mayor(lista):
    maxim=lista[0]
    for i in range(len(lista)):
        if lista[i]>maxim:
            maxim=lista[i]
    return maxim
def minimo(lista):
    min=lista[0]
    for i in range(len(lista)):
        if lista[i]<min:
            min=lista[i]
    return min
def media(lista):
    suma=lista[0]
    for i in range(len(lista)):
        suma+=lista[i]
    return suma/len(lista)     

d=leefich("gastos.txt")
e=mayor(d)
print(d)
print(e)
print(minimo(d))
print(media(d))