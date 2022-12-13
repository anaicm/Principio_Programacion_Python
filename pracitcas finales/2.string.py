def nombreApell(a):
    s=a.split()
    nombre=s[0]
    apellidos=s[1:]
    return nombre,"".join(apellidos)
    
    
    
d=("Ana Cuellar Maestro")
print(nombreApell(d))