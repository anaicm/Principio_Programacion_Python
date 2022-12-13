#18.lista
def masAlto(a):
    masA=a[0]
    for i in range(len(a)):
        if a[i]>masA:
            masA=a[i]
    return masA
def masBajo(a):
    masB=a[0]
    for i in range(len(a)):
        if a[i]<masB:
            masB=a[i]
    return masB
def media(a):
    suma=0
    for i in range(len(a)):
        suma +=a[i]
    return suma/len(a)
def masAltosMedia(a):
    masAltos=0
    masBajos=0
    for i in range(len(a)):
        if a[i]>media(a):
            masAltos +=1
        if a[i]<media(a):
            masBajos +=1
    return masAltos,masBajos
d=[1.60,1.55,1.45,1.70,]
print(masAlto(d))
print(masBajo(d))
print(media(d))
print(masAltosMedia(d))