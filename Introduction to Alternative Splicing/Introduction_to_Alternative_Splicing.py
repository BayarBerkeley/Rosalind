# Positive integers n and m with 0 =< m =< 2000
# The sum of combinations C(n,k) for all k satisfying m=<k=<n modulo 1000000. In shorthand, sum of (permutaion of n and k).
import math 

def sum_combinations(n: int, m:int) -> int:
    sum = 1
    for k in range(m, n):
        sum+=math.comb(n,k)

    return sum

if __name__ == '__main__':
    with open('rosalind_aspc.txt','r') as file:
        n_m = file.readline().split(' ')

        n = int(n_m[0])
        m = int(n_m[1])
    
    with open('result.txt','w') as file:
        file.write(str(sum_combinations(n,m)%1000000))