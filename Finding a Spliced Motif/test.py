# Too Too slow 
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

seq_len = len(data['sequence'])
seq = data['sequence']
begin = 0
mot = data['motif']
order = []
for nt in mot:
    new_nuc = []
    for int in range(seq_len):
        if seq[int] == nt:
            new_nuc.append(int + 1)
    order.append(new_nuc)

def collect_order(list_order, n=0):
    list = []
    if not list_order:
        return [[n]]
    
    result = []
    for nt_ind in list_order[0]:
        if n < nt_ind:
            list_ind = collect_order(list_order[1:],nt_ind)
            length = len(list_ind)
            for i in range(length):
                if n == 0:
                    result.append(list_ind[i])
                else:
                    result.append([n] + list_ind[i])
        else:
            continue
    return result

with open('result.txt','w') as file:
    list_order = collect_order(order)
    for lst in list_order:
        file.write(' '.join([str(i) for i in lst]) + '\n')
