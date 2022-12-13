def primeryUltimo(a,x):
    posP=-1
    PosF=-1
    for i in range (int(len(a))):
        for j in range (int(len(a))):
            if i!=j and a[i]==a[j]:
                posF=i
            if i!=j and a[i]==a[j] and posF!=-1:
                posP=j
    return posP, posF



d=[1,5,9,4,5,7]
print(primeryUltimo(d,5))