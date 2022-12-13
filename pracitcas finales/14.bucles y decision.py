n=int(input("número"))
cont=0
cont1=1
prim=0
seg=0
while n!=0:
    cont+=1
    if n==12 and  prim==0:
        prim=cont
    if n==12 and  prim!=0:
        seg=cont1
    n=int(input("número"))
    cont1+=1
print(prim,seg)