# Given: A positive integer n(n=<1000).
# Return: The total number of subsets of {1,2,...,n} modulo 1,000,000

# On and off swiches, in another word, exlude or include subsets.

def counting_subset(total_number: int) -> int:
    return pow(2,total_number,1000000)

if __name__ == '__main__':
    with open('rosalind_sset.txt','r') as file:
        t_num = int(file.readline())
    
    with open('result.txt','w') as file:
        file.write(str(counting_subset(t_num)%1000000))
