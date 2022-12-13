def mismoConjuntoLetras(s1,s2):
    coincide=True
    for i in range(len(s1)):
        if s1[i] not in s2:
            coincide=False
    return coincide
    
    
    
d=("mirarrama")
e=("amorio")
print(mismoConjuntoLetras(d,e))