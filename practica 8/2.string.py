#2.string
def iniciales(nom):
    
    a=nom.split()
    nom=a[0]
    apell1=a[1]
    apell2=a[2]
    
    
    return nom,apell1+" "+apell2
    
d=("Ana Cuellar Maestro")
print(iniciales(d))
