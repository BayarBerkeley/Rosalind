# this methods find failure function array 
# this array is usefull for future repeating in the motif looking for in certain sequence
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#Description_of_pseudocode_for_the_table-building_algorithm

def build_T(seq):
    T = [0 for i in seq]
    T[0] = -1
    pos = 1
    cnd = 0

    while pos < len(seq):
        if seq[pos] == seq[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and seq[pos] != seq[cnd]:
                cnd = T[cnd]
        pos +=1
        cnd +=1
    return(T)

def found_motif(seq):
    j = 1
    k = 0
    P = [0 for i in range(len(seq))]
    T = build_T(seq)
    print(T)
    len_seq = len(seq)
    while j < len_seq:
        if seq[k] == seq[j]:
            j = j+1
            k = k+1
            P[j - 1] = k
        else:
            k = T[k]
            if k < 0:
                j +=1
                k +=1
    return(P)


if __name__ == '__main__':
    from Bio import SeqIO
    f = open('rosalind_kmp.txt','r')
    record = SeqIO.read(f,'fasta')

    with open('result.txt','w') as file:
        file.write(' '.join([str(i) for i in found_motif(record.seq)]))

            
