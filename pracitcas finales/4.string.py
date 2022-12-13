def mismasLetras(a,b):
    son=True
    for i in range(len(a)):
        if a[i] not in b:
            son=False
    return son


d=("romana")
e=("marano")
print(mismasLetras(d,e))