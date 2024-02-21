def hamming_distance(seq1, seq2):
    count = 0
    for nc1, nc2 in zip(seq1, seq2):
        if nc1 != nc2:
            count += 1
    return count/len(seq1)



def transfer_to_matrix(seqs: list):
    dis_matrix = []
    dic_dis = {}
    seq_len = len(seqs)
    for i in range(seq_len):
        row_matrix = []
        for j in range(seq_len):
            if seqs[i].seq == seqs[j].seq:
                row_matrix.append(str(0))
                continue
            else:
                if (i,j) in dic_dis:
                    row_matrix.append(dic_dis[(i,j)])
                else:
                    dis = round(hamming_distance(seqs[i].seq,seqs[j].seq),5)
                    dic_dis[(i,j)] = str(dis)
                    dic_dis[(j,i)] = str(dis)
                    row_matrix.append(str(dis))
        dis_matrix.append(row_matrix)
    return dis_matrix

if __name__ == '__main__':
    from Bio import SeqIO
    records = list(SeqIO.parse("rosalind_pdst.txt", "fasta"))

    with open('result.txt','w') as file:
    
        mtrx = transfer_to_matrix(records)
        for line in mtrx:
            file.write(' '.join(line) + '\n')



