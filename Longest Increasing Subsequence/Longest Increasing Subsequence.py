# length = input("Enter Length n: ")
# gene_sizes = input("Enter Gene Sizes: ")
length = ""
gene_sizes = ""
with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/rosalind_lgis.txt', 'r') as file:
    lines = file.readlines()
    length = lines[0]
    gene_sizes = ''.join([s[:-1] for s in lines[1:]])

gene_sizes = gene_sizes.split(" ")


try:
    length = int(length)
    print(f"length n is {length} and gene sizes {gene_sizes}")
except:
    print("Your input must be integer")

subsequences_inc = []
subsequences_dec = []
length_e = len(gene_sizes)
for i in range(length_e):
    size_i = int(gene_sizes[i])
    saved_dec = []
    saved_inc = []
    i = max(len(subsequences_dec), i, len(subsequences_inc))
    for j in range(i):
        if len(subsequences_dec) > j and subsequences_dec[j][-1] > size_i:
            saved_dec.append(subsequences_dec[j].copy())
            subsequences_dec[j].append(size_i)
        if len(subsequences_inc) > j and subsequences_inc[j][-1] < size_i:
            saved_inc.append(subsequences_inc[j].copy())
            subsequences_inc[j].append(size_i)

    if saved_dec:
        subsequences_dec = subsequences_dec + saved_dec
    if saved_inc:
        subsequences_inc = subsequences_inc + saved_inc
    subsequences_inc.append([size_i])
    subsequences_dec.append([size_i])
print(subsequences_dec)
print(subsequences_inc)
max_inc = []
max_dec = []
for sizes in subsequences_inc:
    if len(max_inc) <= len(sizes):
        max_inc = sizes
for sizes in subsequences_dec:
    if len(max_dec) <= len(sizes):
        max_dec = sizes

with open("result.txt","w") as file:
    file.write(' '.join([str(int) for int in max_dec]) + '\n')
    file.write(' '.join([str(int) for int in max_inc]))

print(max_inc)
print(max_dec)