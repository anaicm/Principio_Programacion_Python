#17.listas
def lcs(a):
    contMax =1
    cont=1
    for i in range (len(a)-1):
        if a[i]==a[i+1]:
            cont+=1
            if cont > contMax:
                contMax = cont
        else:
            cont=1
            
    return contMax
            


d=[2,5,4,2,2,5,6,6,6,3]
print(lcs(d))