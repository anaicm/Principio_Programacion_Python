#3.cadenas
def quitaHora(s):
    a=s.split("-")
    return a[1]
 
 
 
 
d="02/03/16, 21:03 - Leonard: ¿Deberíamos haberla invitado a almorzar?"
e="02/03/16, 21:17 - Sheldon: No. Vamos a comenzar la segunda temporada de Battlestar Galactica."
print(quitaHora(d))
print(quitaHora(e))