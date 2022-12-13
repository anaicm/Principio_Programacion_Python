def lcs(a):
    cont=1
    contMayor=1
    for i in range(len(a)):
        if a[i]==a[i-1]:
            cont+=1
            if cont>conMayor:
                contMayor=cont
            else:
                cont=1
        return contMayor
    
d=[2,5,4,2,2,5,6,6,6,3]
print(lcs(d))