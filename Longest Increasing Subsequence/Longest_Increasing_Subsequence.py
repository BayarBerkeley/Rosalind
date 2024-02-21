# length = input("Enter Length n: ")
# gene_sizes = input("Enter Gene Sizes: ")
# length = ""
# gene_sizes = ""
with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/rosalind_lgis.txt', 'r') as file:
    lines = file.readlines()
    length = lines[0]
    gene_sizes = ''.join([s[:-1] for s in lines[1:]])

# gene_sizes = '0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15'
# gene_sizes = list(map(int, gene_sizes.split()))


try:
    length = len(gene_sizes)
    print(f"length n is {length} and gene sizes {gene_sizes}")
except:
    print("Your input must be integer")

Predes = [] # store the index of the predecessor of gene_sizes in longest at 
Mindex = [-1] # store the index of the longest subsequence

L = 0 # store the length of the the longest subsequence found so far
for i in range(length): # i = 3
    low = 1 
    high = L + 1 
    while low < high:
        middle = low + int((high - low)/2)
        if gene_sizes[Mindex[middle]] >= gene_sizes[i]: # You can change this code to have decreasing or increasing subsequence.
            high = middle
        else:
            low = middle + 1
    
    newL = low

    Predes.append(Mindex[newL - 1])
    if len(Mindex) > newL:
        Mindex[newL] = i
    else:
        Mindex.append(i)

    if newL > L:
        L = newL
    
Longest_inc = []
k = Mindex[L]
for j in range(L):
    Longest_inc.append(str(gene_sizes[k]))
    k = Predes[k]

with open("result.txt","w") as file:
    file.write(' '.join(Longest_inc[::-1]))