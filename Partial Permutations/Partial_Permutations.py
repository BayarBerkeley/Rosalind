with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/Partial Permutations/rosalind_pper.txt') as file:
    content = file.read()

str_list = content.split()
print(str_list)
int_list = [int(i) for i in str_list]
print(int_list)
def permutations(n,k):
    if n == k:
        return 1
    else:
        return n*permutations(n-1,k)
print(permutations(int_list[0],int_list[0]-int_list[1]))
with open('result.txt', 'w') as file:
    file.write(str(permutations(int_list[0],int_list[0]-int_list[1])%1000000))
