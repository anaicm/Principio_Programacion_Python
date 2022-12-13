#ejercicio 8 futbol
def equipoPartidos(nombFich):
    liga=[]
    f=open(nombFich)
    for linea in f:
        r={}
        r["equipo"],datos=linea.split(":")
        datos=datos.split()
        r['puntosTotales']=int(datos[0])
        r['partidosTotJugados']=int(datos[1])
        r['partidosTotGanados']=int(datos[2])
        r['partidosTotEmpatados']=int(datos[3])
        r['partidosTotPerdidos']=int(datos[4])
        r['golesTotFavor']=int(datos[5])
        r['golesTotContra']=int(datos[6])
        r['puntosCasa']=int(datos[7])
        r['partidosCasaJugados']=int(datos[8])
        r['partidosCasaGanados']=int(datos[9])
        r['partidosCasaEmpatados']=int(datos[10])
        r['partidosCasaPerdidos']=int(datos[11])
        r['golesCasaFavor']=int(datos[12])
        r['golesCasaContra']=int(datos[13])
        r['puntosFuera']=int(datos[14])
        r['partidosFueraJugados']=int(datos[15])
        r['partidosFueraGanados']=int(datos[16])
        r['partidosFueraEmpatados']=int(datos[17])
        r['partidosFueraPerdidos']=int(datos[18])
        r['golesFueraFavor']=int(datos[19])
        r['golesFueraContra']=int(datos[20])
        liga.append(r)
    return liga
def sumaGoles(liga):
    s=0
    for lin in liga:
        s +=lin['golesTotFavor']+lin['golesTotContra']
    return s//2
def maximPartidosPerdi(liga):
    maxPartidos=0
    for i in range(1,len(liga)):
        if liga[i]['partidosCasaPerdidos']>maxPartidos:
            maxPartidos=i
    return maxPartidos
def equipMasPierde(liga):
    imasPierde=[]
    for i in range(len(liga)):
        if liga[i]['partidosCasaPerdidos']==maximPartidosPerdi:
            imasPierde.append(liga[i]['equipo'])
    return imasPierde
    
        
#----------------------------------
d=equipoPartidos("liga2018.txt")
print(d)
print(sumaGoles(d))
print(maximPartidosPerdi(d))
print(equipMasPierde(d))