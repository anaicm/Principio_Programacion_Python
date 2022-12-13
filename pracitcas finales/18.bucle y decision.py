n=int(input("número"))
suma=0
perfecto=False
for i in range(1,n-1):
    suma+=i
    if suma==n:
        perfecto=True
if perfecto:
    print("Es perfecto")
else:
    print("No es perfecto")
        