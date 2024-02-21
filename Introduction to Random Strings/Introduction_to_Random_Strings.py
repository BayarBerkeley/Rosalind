from math import log10, pow, trunc

with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/Introduction to Random Strings/rosalind_prob.txt', 'r') as file:
    content = file.read()
    content = content.split('\n')

    sequence = content[0]
    GC_probs = content[1].split()
    GC_probs = [float(i) for i in GC_probs]

    AT = 0
    GC = 0
    for aa in sequence:
        if aa == 'T' or aa == 'A':
            AT +=1
        else:
            GC +=1
    
    log_probs = []
    for prob in GC_probs:
        float_num = str(trunc(log10(pow(prob/2,GC)*pow((1-prob)/2,AT))*1000)/1000)
        if len(float_num) != 6:
            float_num += '0'
        log_probs.append(float_num)

with open('result.txt','w') as file:
    file.write(' '.join(log_probs))
