def freqs(s):
    c=[]
    for i in s:
        if i not in c:
            c.append(i)
    return "".join(c)
def freqs2(a):
    f={}
    repe=0
    cont=0
    for i in freqs(a):
        if i in a:
            repe+=1
        cont+=1
        f[i]=repe
    return f
            
d=("Las gafas")
print(freqs2(d))