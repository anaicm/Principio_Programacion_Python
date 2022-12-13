def iniciales(a):
    s=a.split()
    nombre=s[0]
    apellido1=s[1]
    apellido2=s[2]
    iniciales=apellido2[0],apellido1[0],nombre[0]
    return "".join(iniciales)
    


d=iniciales("Ana Cuellar Maestro")
print(d)