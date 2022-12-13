def iguales(a,b):
    s=a.upper()
    c=b.upper()
    sonIguales=True
    for i in s:
        if not i in c and len(s)==len(c):
            sonIguales=False
    return sonIguales
            
    
d=("Hola")
e=("hoLa")
print(iguales(d,e))