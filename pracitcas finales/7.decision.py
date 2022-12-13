a=int(input("numero"))
b=int(input("numero"))
c=int(input("numero"))
if a>b and b>c:
    print("El mayor es:",a)
elif b>a and b>c:
    print("El mayor es:",b)
else:
    print("El mayor es:",c)
    