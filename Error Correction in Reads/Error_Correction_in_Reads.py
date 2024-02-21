# dna sequence turns into reverse compliment sequence
def reverve_complement(dna_seq):
    nuc = {'A':'T','T':'A','G':'C','C':'G'}
    comp_seq = dna_seq[::-1]
    comp_seq = ''.join([nuc[nc] for nc in comp_seq])
    return comp_seq

# Return True if there is a Hamming distance of 1 between the given sequences; otherwise, return False.
def hamming_distance_for_1(dna_seq1, dna_seq2):
    if dna_seq1 == dna_seq2:
        return False
    
    count = 0
    for nc1, nc2 in zip(dna_seq1,dna_seq2):
        if nc1 != nc2:
            count +=1
        if count > 1:
            return False
    return True

if __name__ == "__main__":
    from Bio import SeqIO
    records = list(SeqIO.parse("rosalind_corr.txt", "fasta"))

    dic_seq = {}
    # Count all sequences. Meanwhile, find the reverse complement and count occurrences in the original sequence. 
    # This way, there are non-repeated DNA sequences in the list.
    for seq in records:
        if reverve_complement(seq.seq) not in dic_seq and seq.seq not in dic_seq:
            dic_seq[seq.seq] = 1
        elif seq.seq in dic_seq:
            dic_seq[seq.seq] +=1
        elif reverve_complement(seq.seq) in dic_seq:
            dic_seq[reverve_complement(seq.seq)] +=1
    
    err_seq = []
    cor_seq = []
    
    for seq in dic_seq:
        if dic_seq[seq] == 1:
            err_seq.append(seq)
        else:
            cor_seq.append(seq)
# Calculate the Hamming distance and write the result into 'result.txt'.
with open('result.txt','w') as file:
    for err in err_seq:
        found_seq = ''
        for cor in cor_seq:
            if hamming_distance_for_1(err, cor):
                found_seq = cor
                file.write(str(err + '->' + cor + '\n'))
                break
            elif hamming_distance_for_1(err,reverve_complement(cor)):
                file.write(str(err + '->' + reverve_complement(cor) + '\n'))
                found_seq = cor
                break
        if found_seq:
            cor_seq.remove(cor)


    