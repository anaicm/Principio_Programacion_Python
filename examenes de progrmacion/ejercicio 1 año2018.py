#Se tiene en un fichero gastos.txt las canti-
#dades gastadas en una larga serie de compras. Se
#quiere saber cuál es la cantidad media de lo gas-
#tado, lo máximo y lo mínimo. Para ello desarrollar
#una función capaz de leer cualquier fichero de nom-
#bre recibido en un único parámetro con el nombre
#del fichero, y que devuelva los tres números reales:
#media, mínimo y máximo. El fichero de ejemplo,
#gastos.txt, se dará al final de las preguntas. Definir
#la función
#def leeGastos(..) que reciba el nombre
#del fichero en un parámetro, y que devuelva los tres
#valores anteriores, para que fuera de la función se
#puedan imprimir al final del programa. Los gastos
#son números reales que están separados por espacios
#en varias líneas.
#Saldría: (439.3402500000001, 14.31, 979.8)
def leeGastos(nombFich):
    f=open(nombFich)
    lista=[]
    suma=0
    
    
    for gastos in f:
        g = gastos.split()
        for i in g:
            lista.append(float(i))       
    for k in range(len(lista)):
        suma += lista[k]
    mayor=lista[0]
    for j in range(len(lista)):
        if lista[j]>mayor:
            mayor=lista[j]
    menor=lista[0]#para el menor en numeros positivos siempre el primero de lista
    for x in range(len(lista)):
        if lista[x]<menor:
            menor=lista[x]
    return suma/len(lista),mayor,menor
        
    
    
    
    
d=leeGastos("gastos.txt")
print(d)







