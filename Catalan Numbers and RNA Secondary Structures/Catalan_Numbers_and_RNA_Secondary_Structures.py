def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)

def catalan_num(n):
    return (factorial(2*n)/(factorial(n+1)*factorial(n)))

def find_even_base(sequence):
    first_base = sequence[0]
    base_seq = {'A':'U','U':'A','G':'C','C':'G'}
    even_m = []
    count_base = {'A':0,'U':0,'G':0,'C':0}
    for i in range(len(sequence)):
        if i == 0:
            continue

        if sequence[i] == base_seq[first_base] and i%2==1 and count_base['A'] == count_base['U'] and count_base['C'] == count_base['G']:
            even_m.append(i + 1)

        if sequence[i] == 'A':
            count_base['A'] += 1
        elif sequence[i] == 'U':
            count_base['U'] += 1
        elif sequence[i] == 'G':
            count_base['G'] += 1
        elif sequence[i] == 'C':
            count_base['C'] += 1
        
    return even_m

def catal_num1(list_k, len):
    total_cat = 0.0
    for i in list_k:
        total_cat += catalan_num(int(i/2))*catalan_num(int(len/2 - i/2))

    return total_cat

with open('rosalind_cat.txt','r') as file:
    sequence = ''
    for line in file:
        if line.startswith('>'):
            continue
        else:
            sequence += line.rstrip()

count = 0
for base in sequence:
    if base == 'A' or base == 'C':
        count+=1

total_cat = 0
for i in range(1,count):
    total_cat += catalan_num(i)*catalan_num(count - i)
print (total_cat%1000000)
print(find_even_base(sequence))
print(catal_num1(find_even_base(sequence),len(sequence)))
