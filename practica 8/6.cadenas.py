#6.cadenas
def iniciales(a):
    
    d=a.split()
    nombre=d[0]
    apell1=d[1]
    apell2=d[2]
    return apell1[0]+apell2[0]+nombre[0]



d="Ana Cuellar Maestro"
print(iniciales(d))