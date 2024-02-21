with open('rosalind_tran.txt','r') as file:
    data = {'origin':'','mutated':''}
    sequence = ''
    for line in file:
        if line.startswith('>') and sequence:
            data['origin'] = sequence
            sequence = ''
        elif line.startswith('>') and not sequence:
            continue
        else:
            sequence += line.rstrip()
    data['mutated'] = sequence

seq_origin = data['origin']
seq_mutated = data['mutated']
transitions = 0
transversions = 0

trans = {'A':'G','T':'C','G':'A','C':'T'}
for base_ori, base_mut in zip(seq_origin, seq_mutated):
    if base_ori == base_mut:
        continue
    elif base_ori == trans[base_mut]:
        transitions +=1
    else:
        transversions +=1

with open('result.txt','w') as file:
    file.write(str(transitions/transversions))