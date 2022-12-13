n=int(input("número"))
mayor=0
while n!=0:
    if n>mayor:
        mayor=n
    n=int(input("número"))
print(mayor)