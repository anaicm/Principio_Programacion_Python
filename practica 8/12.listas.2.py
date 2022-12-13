#12.lista
def productoEscalar(a,b):
    producto=0
    for i in range(len(a)):
        producto +=a[i]*b[i]
    return producto
                   
 
 
 
d=[3,2,8,7,8,1,9,10]
e=[3,2,8,7,8,1,9,10]
print(productoEscalar(d,e))