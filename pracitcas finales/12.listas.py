def prodEScalar(a,b):
    producto=0
    suma=0
    for i in range (len(a)):
        producto=a[i]*a[i]
        suma+=producto
    return suma
    

        
    
    
d=[1,2,3,4]
e=[1,2,3,4]
print(prodEScalar(d,e))