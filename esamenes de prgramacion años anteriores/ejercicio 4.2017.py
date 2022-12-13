def leePeliculas(nomFich):
    f=open(nomFich)
    l=[]
    dic={}
    for linea in f:
        if linea[0] == "*":
            if "titulo" in dic.keys():
                l.append(dic)
                dic = {}
            dic['titulo'] = linea[1:].strip()
        else:
            if "descripcion" in dic.keys():
                dic['descripcion'] += linea.strip()
            else:
                dic['descripcion'] = linea.strip()
    return l
def buscar(a):
    buscar=input("titulo")
    while buscar!="":
        for i in a:
            if i["titulo"]==buscar:
                print(i)
        buscar=input("titulo")


d=leePeliculas("cine2017.txt")
print(d)
print(buscar(d))