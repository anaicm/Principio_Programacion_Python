#1.cadenas
def posACGT(seq,nuc):
    lista=[]
    igual=0
    for i in range(len(seq)):
        if seq[i]==nuc:
            igual=i
            
            lista.append(igual+1)
    return lista
    
#[1, 5, 10, 15, 17, 19, 23, 31, 37, 40, 42, 46, 47, 48, 51, 52, 53]

d='ATCCATTCGACTCCACACAGCTAGCGTGGCACTTTCACGACATCTAAACGAAAGGTCTCG'
nuc="A"
print(posACGT(d,nuc))
