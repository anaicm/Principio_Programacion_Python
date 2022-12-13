def leeFich(nombFich):
    f=open(nombFich)
    r={}
    for i in f:
        pobl=i.strip().split(":")
        ciudad=pobl[0]
        poblacion=int(pobl[1])
        r[ciudad]=poblacion
    
    return r
    
def MasPobla(ciudad):
    masP=0
    cont=0
    vmasP=0
    for k,j in ciudad.items():
        if j>masP or cont==0:
            masP=j
            vmasP=k
        cont+=1
    return vmasP


d=leeFich("poblacion.txt")
print(d)
print(MasPobla(d))