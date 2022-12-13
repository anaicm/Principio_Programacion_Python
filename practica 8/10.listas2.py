#.listas
def primerYultimo(a):
    pos1=-1
    pos2=-1
    i=0
    while i<len(a):
        if a[i]==a[i]+1:
            pos1=i
        if a[i]==a[i]+1 and pos1!=-1:
            pos2=i
        i+=1
    return pos1,pos2



d=[3,2,8,7,8,1,9,10]
print(primerYultimo(d))