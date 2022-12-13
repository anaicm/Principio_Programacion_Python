#1.string
def comparastr(s1,s2):
    a=s1.upper()
    b=s2.upper()
    if a==b:
        return True
    return False
    
d=("python")
e=("PytHon")
print(comparastr(d,e))