#{’Alumno 1’: {’c1’:5, ’c2’:2, ’fi’:7, ’F’:7.375}}
#wf = (10 - 0.15*c1 - 0.25*c2)/10
#f*wf + 0.15*c1 + 0.25*c2.
def leeFich(nomfich):
    f=open(nomfich)
    r={}
    wf=0
    fi=0
    for i in f:
        s={}
        alumno,notas=i.split(":")
        nota=notas.strip().split()
        s["c1"]=float(nota[0])
        s["c2"]=float(nota[1])
        s["fi"]=float(nota[2])
        wf=(10-0.15*s["c1"]-0.25*s["c2"])/10
        fi=s["fi"]*wf +0.15*s["c1"]+0,25*s["c2"]
        s["F"]=fi
        r[alumno]=s
    return r


d=leeFich("nota.txt")
print(d)