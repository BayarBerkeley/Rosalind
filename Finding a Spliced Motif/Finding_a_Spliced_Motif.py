with open('rosalind_sseq.txt','r') as file:
    data = {}
    data = {'sequence':'','motif':''}
    sequence = ''
    for line in file:
        if line.startswith('>') and sequence:
            data['sequence'] = sequence
            sequence =''
        elif line.startswith('>'):
            continue
        else:
            sequence += line.rstrip()

data['motif'] = sequence

seq = data['sequence']
mot = data['motif']
print(len(mot))
print(mot)
len_seq = len(data['sequence'])
len_mot = len(data['motif'])
begin = 0
order = []
for i in range(len_mot):
    for j in range(begin, len_seq):
        if mot[i] == seq[j]:
            begin = j + 1
            order.append(j + 1)
            break

with open('result.txt','w') as file:
    file.write(' '.join([str(i) for i in order]))