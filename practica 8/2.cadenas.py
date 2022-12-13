#2.cadenas
def iguales (a,b):
    s=a.upper()
    r=b.upper()
    for i in range(len(s)):
        if not s[i]==r[i]:
            return False
    return True
    
    
d=("Hole")
e=("holA")
print(iguales (d,e))