n=int(input("número"))
suma=0
coin=False
cont=0
while n!=0:
    suma+=n
    cont+=1
    n=int(input("número"))
    if suma==n and cont!=1:
        coin=True

    
print(coin)