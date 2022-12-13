def suma(a):
    s=a.split(":")
    r=s[1].split()
    suma=0
    for i in range (len(r)):
        suma+=float(r[i])
    return suma
        


d=("Madrid: 0 2.1 1 0 0 3.5 1.1")
print(suma(d))