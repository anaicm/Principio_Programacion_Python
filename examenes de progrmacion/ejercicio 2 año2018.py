#En una clínica se tienen unos datos de los usuarios en un fichero
#usuarios.txt de forma que en en cada línea del fichero se tiene el nombre seguido de
#’:’ y dos números reales que son la altura (m) y el peso (kg) del usuario separados
#por espacios. Hacer una función def leeAlturasPesos(...) que reciba en
#su parámetro el nombre de un fichero, y que devuelva una lista estructurada
#con todos los datos del fichero, tal que cada elemento de la lista contenga un
#diccionario con los camp os: ’nombre’, ’altura’ y ’peso’. Una vez devuelta esta lista,
#en el programa principal, guardarla en una variable apropiada para
#usarla en el siguiente programa.
def leeAlturasPesos(nombFich):
    f=open(nombFich)
    lista=[]
    for i in f:
        r={}
        r["nombre"],alturaypeso=i.strip().split(":")
        altura,peso=alturaypeso.split()
        r["altura"]=float(altura)
        r["peso"]=float(peso)
        lista.append(r)
        
    return lista
#imc = p/h**2
def imprimeIMC(lista):
    
    for i in lista:    
        print(i["nombre"]+":"+str (i["peso"]/(i["altura"])**2))
    
        
d=leeAlturasPesos("usuarios.txt")
print(d)
imprimeIMC(d)