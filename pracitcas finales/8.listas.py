def posMayor(a):
    mayor=0
    for i in range(len(a)):
        if a[i]>a[mayor]:
            mayor=i
    return mayor

d=[1,5,9,4,6,7]
print(posMayor(d))