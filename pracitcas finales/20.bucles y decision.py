n=int(input("número"))
suma=0
primer=0
perfecto=False
for i in range(1,n-1):
    suma+=i
    if suma==n:
        perfecto=True
        if primer>28:
            primer=suma
print(primer)

        no esta bien 