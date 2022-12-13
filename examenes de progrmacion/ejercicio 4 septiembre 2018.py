#Hacer el programa pr4.py: hacer una función def statFich(nomFich)
#que devuelva los valores mínimo, máximo y media de un fichero lleno de números.
#Los números en el fichero estarán separados por espacios y/o saltos de línea.
#Llamar a la función con el fichero "nums.txt" que se da a la vuelta de este
#folio. Imprimir los resultados (deben ser: (14.31,979.8, 439.3402500000001))
def statFich(nomFich):
    f=open(nomFich)
    valores=[]
    for i in f:
        for j in i.split():            
            valores.append(j)
    mayor=valores[0]
    for i in range (len(valores)):
        if valores[i]>mayor:
            mayor=valores[i]
    minimo=valores[0]
    for i in range(len(valores)):
        if valores[i]<minimo:
            minimo=valores[i]
    suma=0
    for i in valores:
        suma +=float(i)
    
    return mayor,minimo,suma/len(valores)   

#-----------------------------------------------------
d=statFich("nums.txt")
print(d)