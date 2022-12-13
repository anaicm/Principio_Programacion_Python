#Hacer el programa
#pr1.py: dada una lista de
#enteros devolver la suma de todos sus números im-
#pares. Para ello diseñar una función sumaImpares
#que reciba un parámetro de tipo lista lleno de enteros
#y devuelva la s uma de todos aquellos números de la
#lista que sean impares. Si no hay ningún número im-
#par, devolver 0.
#Ejemplo:
#lista 1: 6 4 12 0 4 2 46 18 24 16 Suma impares: 0
#lista 2: 8 11 3 13 2 7 56 13 5 9 Suma impares: 61
def listaDeNumeros(a):
    b=a.split()
    return b
def sumaImpares(a):
    suma=0
    for i in listaDeNumeros(a):
        if int(i)%2!=0:
            suma+=int(i)
    return suma

lista1=("6 4 12 0 4 2 46 18 24 16")
lista2=("8 11 3 13 2 7 56 13 5 9")
print("Suma impares: ",sumaImpares(lista1))
print("Suma impares: ",sumaImpares(lista2))
