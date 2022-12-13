#5.cadenas
def sumaLLuvias(s):
    lluvia=s.split()
    suma=0
    for i in range(1,len(lluvia)):
        suma +=float(lluvia[i])
    
        
    return suma





d="Madrid:   0 2.1 1 0 0 3.5 1"
print(sumaLLuvias(d))