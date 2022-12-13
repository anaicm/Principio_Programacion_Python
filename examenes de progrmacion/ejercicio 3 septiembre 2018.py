#Hacer el programa pr3.py: hacer un programa que llame al procedimiento
#def sumaListas(a, b). Llamaremos a esta función pasándole las listas
#[1, 4, 2, 5, 9] y [3, -1, 2, 0, 0], y la función debe sumar cada elemento de ellas
#devolviendo una tercera lista resultado [4, 3, 4, 5, 9]. Después de llamar a la
#función con los ejemplos anteriores, imprimir en pantalla el resultado para verlo.
#Nótese que las listas que le lleguen a la función pudieran no tener la misma longitud,
#con lo cual no se podrían sumar. Así que antes de sumar los elementos
#de las listas, comprobar que ambas listas tienen la misma longitud.
#Si no tuviesen la misma longitud, el resultado a devolver podría ser una lista vacía,
#sin números.
def sumaListas(a, b):
    resultado=[]
    suma=0
    if len(a)==len(b):
        for i in range(len(a)):
            suma =a[i]+b[i]
            resultado.append(suma)
    return resultado
    
    
d=[1, 4, 2, 5, 9]
e=[3, -1, 2, 0, 0]
print(sumaListas(d,e))