#15.hay repes
def hayRepes(a):
    for i in range (len(a)-1):
        for j in range(len(a)-1):
            if i!=j and a[i]==a[i+1]:
                return True
    return False
    
    
   
   
d=[2,4,1,6,7,8,4,5,9]
print(hayRepes(d))