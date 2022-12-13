def comparastrs(s1,s2):
    a=s1.upper()
    b=s2.upper()
    son=False
    for i in a:
        if i in b and len(a)==len(b):
            son=True
    return son
            
d=("Python")
e=("pytHon")
print(comparastrs(d,e))