#Hacer el programa pr2.py: averiguar el número
#total de veces que aparece en concreto el nucle-ótido ’G’ en un fichero FASTA.
#Para ello hacer una función def numNuc(nomfich, letraBuscada) que
#reciba el nombre del fichero y devuelva ese número. Supondremos que en el fichero
#sólo hay una secuen-cia de nucleótidos de forma que sólo la primera línea
#del fichero contiene su identificador que comienza con el carácter
#’>’ al principio de la primera línea del fichero, con lo cual debemos leer e ignorar esa
#primera línea entera. Después podemos leer el resto del fichero y contar las
#’G’ en esa lista leída.
#NOTA: Para hacer este problema debemos construir
#una función que reciba tanto el nombre del fichero como la letra del nucleótido
#que se está buscando y devuelva el número entero de veces que esa letra (’G’
#en nuestro ejemplo) aparece. Hay que construir el fichero
#"seq.fasta", para ello hacer un fichero nuevo vacío escribir en él sólo literalmente
#lo que sigue (guardarlo este fichero con el nombre "seq.fasta" junto al programa pr2.py):
#>Pepe ACTTTGGCTCCAAGTAACCGGGGCAGCCATAGAGTCCTTCGCGGCGATCACCCTCGCCCGGTGACGTTGCCAGGGGTCCACA
#En pantalla deberá salir: El fichero seq.fasta contiene 24 bases G;
def numNuc(nombfich, letraBuscada):
    f=open(nombfich)
    nomb = f.readline()
    cadena = f.read()
    cont=0
    for i in cadena:
        if i==letraBuscada:
            cont+=1
    return cont,nomb
letraBuscada="G"
d=numNuc("seqfasta.txt",letraBuscada)

print(d)


