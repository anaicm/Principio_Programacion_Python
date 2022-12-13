n=int(input("número"))
suma=0
cont=0
while n!=0:
    cont+=1
    suma+=n
    n=int(input("número"))
print(suma)    
print(round(suma/cont))