#Construir un diccionario sups con clave el nombre del país y valor (entero)
#su superficie (en km2) copiando la tabla superficies que se adjunta al reverso
#de esta hoja. Pasar sups como el parámetro a una función def mayorSup(d)
#que nos diga cuál es el país de mayor superficie de los recibidos. Pasar
#sups a otra función def areaTotal(d) que de-vuelva (ojo que las funciones
#devuelven siempre los datos, no los imprimen ellas) la suma de todas las
#superficies. Imprimir los resultados devueltos (o sea:
#print("La mayor superficie corresponde a:", mayorSup(sups)), etc.)
def mayorSup(nombFich):
    f=open(nombFich)
    area=[]
    for i in f:
        r={}
        posUltimoEspacio=i.rfind(" ")
        r["pais"]=i[0:posUltimoEspacio]
        r["superficie"]=int(i[posUltimoEspacio+1:])
        area.append(r)
    mayor=0
    for i in area:
        if i["superficie"]>mayor:
            mayor=i["superficie"]
            
    suma=0
    for i in area:
        suma+=i["superficie"]
    return mayor,suma
    
    
d=mayorSup("superficies.txt")
print(d)