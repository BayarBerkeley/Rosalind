nuc = ['A','C','G','T']
collect_kmer = {}
def k_mer_lexicograph(num,give_lex = ''):
    if len(give_lex) == num:
        collect_kmer[give_lex] = 0
        return None
    for nc in nuc:
        k_mer_lexicograph(num,give_lex + nc)
    


def count_kmer(seq, num):
    k_mer_lexicograph(num)
    length_seq = len(seq)
    for i in range(length_seq - num + 1):
        collect_kmer[seq[i:i+4]] +=1



if __name__ == "__main__":
    from Bio import SeqIO
    f = open('rosalind_kmer.txt','r')
    record = SeqIO.read(f,'fasta')

    count_kmer(record.seq,4)

    with open('result.txt','w') as file:
        file.write(' '.join([str(num) for num in collect_kmer.values()]))

