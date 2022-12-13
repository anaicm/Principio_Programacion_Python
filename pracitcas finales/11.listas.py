def sumaListas(a,b):
    suma=0
    lista=[]
    if len(a)==len(b):
        for i in range(len(a)):
             suma=a[i]+b[i]
             lista.append(suma)
        return lista
        
    
    
d=[1,2,3,4]
e=[1,2,3,4]
print(sumaListas(d,e))