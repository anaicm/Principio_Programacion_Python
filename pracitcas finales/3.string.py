def fechasApartes(fecha):
    a=fecha.split()
    b=a[0].split("-")
    c=a[1].split(":")
    año=b[0]
    mes=b[1]
    dia=b[2]
    hora=c[0]
    minutos=c[1]
    return año,mes,dia,hora,minutos
    
    
d=("1492-10-12 13:05")
print(fechasApartes(d))