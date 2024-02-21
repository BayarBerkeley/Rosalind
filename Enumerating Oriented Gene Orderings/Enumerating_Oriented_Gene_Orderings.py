with open('rosalind_sign.txt', 'r') as file:
    num_genes = int(file.read())
    print(num_genes)

# input is number of genes between 1-6
# output is list of posible gene position including reverse as negative
def get_premutation(num_genes):

    list_num = [str(i) for i in range(1,num_genes + 1)]
    # input is list of genes from 1 to num_genes
    def enumerating_order(list_num):
        if len(list_num) == 1:
            # reverse gene included
            return [['-' + list_num[0]], list_num]
        
        list_output = []
        for g in list_num:

            new_list = [j for j in list_num if j != g]
            last = enumerating_order(new_list)
            for i in last:
                # reverse numbered gene included 
                list_output.append([g] + i)
                list_output.append(['-' + g] + i)

        return list_output
    
    return enumerating_order(list_num)

with open('result.txt', 'w') as file:
    enum_pos = get_premutation(num_genes)
    file.write(str(len(enum_pos)) + '\n')
    for lst in enum_pos:
        file.write(' '.join(lst) + '\n')


print(get_premutation(num_genes))
