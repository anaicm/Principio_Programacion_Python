def posACGT (seq,nuc):
    cont=1
    lista=[]
    pos=0
    for i in range(len(seq)):
        if seq[i]==nuc and seq[i] in seq:
            cont+=1
            pos=i
            lista.append(pos)
    return lista




seq=("ATCCATTCGACTCCACACAGCTAGCGTGGCACTTTCACGACATCTAAACGAAAGGTCTCG")
nuc=("A")
print(posACGT(seq,nuc))