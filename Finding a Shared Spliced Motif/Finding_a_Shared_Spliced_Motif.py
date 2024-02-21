with open('rosalind_lcsq.txt', 'r') as file:
    seqs = []
    sequence = ''
    for line in file:
        if line.startswith('>') and sequence:
            seqs.append(sequence)
            sequence = ''
        elif line.startswith('>'):
            continue
        else:
            sequence += line.strip()

    seqs.append(sequence)

    seq1 = seqs[0]
    seq2 = seqs[1]

def lcs_matrix(seq1, seq2):
    len1 = len(seq1)
    len2 = len(seq2)

    seq_mat = [[0 for c in range(len1 + 1)] for r in range(len2 + 1)]

    for r in range(1,len2 + 1):
        for c in range(1, len1 + 1):
            if seq2[r-1] == seq1[c-1]:
                seq_mat[r][c] = seq_mat[r-1][c-1] + 1
            else:
                seq_mat[r][c] = max(seq_mat[r-1][c],seq_mat[r][c-1])
    return seq_mat

def traceback(lcs_matrix, seq1, seq2):
    r, c = len(seq2), len(seq1)
    result = ''

    while r > 0 and c > 0:
        if seq2[r - 1] == seq1[c - 1]:
            result = seq2[r - 1] + result
            r -= 1
            c -= 1
        elif lcs_matrix[r - 1][c] > lcs_matrix[r][c - 1]:
            r -= 1
        else:
            c -= 1

    return result


with open('result.txt','w') as file:
    file.write(traceback(lcs_matrix(seq1,seq2), seq1,seq2))
