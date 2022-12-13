def quitarHora(a):
    s=a.split("-")
    return s[1]
    




d=("01/03/16. 21:03-Leonard:¿deberíamos haberla invitado a almorzar?")
e=("01/03/16. 21:17-Sheldon:no,vamos a comenzar la seugnda temporada de battlestar Galactica")
print(quitarHora(d))
print(quitarHora(e))