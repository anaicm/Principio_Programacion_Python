def leePeliculas(nombFich):
    f=open(nombFich)
    listaLineas=[]
    for i in f:    
        datos=i.split("\n")
        listaLineas.append(i)
    peliculas=[]
    
    l={}
    l['titulo']=""
    l['descripcion'] = ""
    for j in listaLineas:
        if j[0]=="*":
            if l["descripcion"] != "":
                peliculas.append(l)
                l={}
                l['descripcion'] = ""
            l['titulo']=j[1:len(j)-2]
        else:
            l["descripcion"]+=j[:len(j)-2]        
    
    return peliculas
  
d=leePeliculas("cine2017.txt")
print(d)