def leefich(nombfich):
    f=open(nombfich)
    g=[]
    for i in f:
        nombre,datos=i.split(":")
        altura,peso=datos.strip().split()
        r={}
        r["nombre"]=nombre
        r["altura"]=float(altura)
        r["peso"]=float(peso)
        g.append(r)
    return g
def imprimeImc(g):
    imc=0
    for i in g:
        imc=i["peso"]/i["altura"]**2
        print(imc)


d=leefich("usuarios.txt")
print(d)
imprimeImc(d)