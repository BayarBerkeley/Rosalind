# Attention! this problem only works in 2.7.8
def count_ATCG(seq):
    count = {'A':0,'U':0,'C':0,'G':0}
    for nc in seq:
        if nc == 'A':
            count['A'] +=1
        elif nc == 'U':
            count['U'] +=1
        elif nc == 'C':
            count['C'] +=1
        elif nc == 'G':
            count['G'] +=1
    print(count)
    return count
    
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)
    
def find_lowest_nd_find(dic_count_nc):
    au = 0
    gc = 0
    if dic_count_nc['A'] > dic_count_nc['U']:
        au = factorial(dic_count_nc['A'])/factorial(dic_count_nc['A']-dic_count_nc['U'])
    else:
        au = factorial(dic_count_nc['U'])/factorial(dic_count_nc['U']-dic_count_nc['A'])
    if dic_count_nc['C'] > dic_count_nc['G']:
        gc = factorial(dic_count_nc['C'])/factorial(dic_count_nc['C']-dic_count_nc['G'])
    else:
        gc = factorial(dic_count_nc['G'])/factorial(dic_count_nc['G']-dic_count_nc['C'])

    return au*gc





if __name__ == '__main__':
 #   from Bio import SeqIO
 #   f = open('rosalind_mmch.txt', 'r')
 #   record = SeqIO.read(f,'fasta')
 #   print(record.seq)
    with open('result.txt', 'w') as file:
        result = find_lowest_nd_find(count_ATCG('GCUGAAUGUUACAGACAGCAUAAAUGGUGUGGAGCUUUAGUAAUAAGAUGAGGUACCUAUCUGUCUAAACUCGAACCGUUGCCGACUUGCAUC'))
        print(result)
 #       result_formatted_fstring = f'{result:.0f}'
 #       file.write(str(result_formatted_fstring))

