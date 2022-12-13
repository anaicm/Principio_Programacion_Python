#5.listas
def menor(a):
    men=a[0]
    for i in range(len(a)):
        if a[i]<men:
            men=i
    return men
    
    

d=[3,2,6,7,8,1,9,10]
print(menor(d))