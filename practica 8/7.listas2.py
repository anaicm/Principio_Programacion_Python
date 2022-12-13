#7.listas
def posMayor(a):
    mayor=a[0]
    for i in range(len(a)):
        if a[i]>mayor:
            mayor=a[i]
    return mayor
    
    
d=[3,2,6,7,8,1,9,10]
print(posMayor(d))