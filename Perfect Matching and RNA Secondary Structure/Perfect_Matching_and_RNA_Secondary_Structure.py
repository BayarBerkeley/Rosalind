with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/Perfect Matching and RNA Secondary Structure/rosalind_pmch.txt', 'r') as file:
    sequence = ''
    for line in file:
        if line.startswith('>'):
            continue
        else:
            sequence += line.rstrip()


count_A = 0
count_C = 0
for i in sequence:
    if i == 'A':
        count_A +=1
    elif i == 'C':
        count_C +=1
print(count_A, count_C)
def factorial(num):
    if num == 1:
        return 1
    else:
        return num*factorial(num-1)

with open('result.txt', 'w') as file:
    file.write(str(factorial(count_A)*factorial(count_C)))
