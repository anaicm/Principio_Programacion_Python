n=int(input("Número"))
primo=True
for i in range(2,n-1):
    if n%i==0:
        primo=False
if primo:
    print("es primo")
else:
    print("no es primo")