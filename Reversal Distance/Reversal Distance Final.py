def identity_permutation(num1: list ,num2: list) -> list:
    new_num = []
    for i in range(len(num1)):
        new_num.append(num1.index(num2[i]) + 1)
    return [0] + new_num + [len(new_num) + 1]

def bp_pair(ident_list: list) -> dict:
    break_point = {}
    dec = []
    for i in range(len(ident_list)-1):
        if abs(ident_list[i] - ident_list[i + 1]) != 1:
            break_point[(ident_list[i],ident_list[i+1])] = i
    return break_point

def reversal_pi_p(pi_list: list, i: int, j:int) -> list:
    return pi_list[:i] + pi_list[i:j+1][::-1] + pi_list[j+1:]

def possible_rev(pi_rev: list) -> list:
    pi_rev_bps = bp_pair(pi_rev)
    if list(pi_rev_bps.keys()) == []:
        return [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
#    print(pi_rev_bps.keys())
    bp_index_0s = []
    bp_index_1s = []
    possible_revs = []

   
    for bp in pi_rev_bps.keys():
        bp_index_0s.append(bp[0])
        bp_index_1s.append(bp[1])

    max_point = max(bp_index_1s)
    
    for bp_0 in bp_index_0s:
        if bp_0 + 1 not in bp_index_0s:
            continue

        i = pi_rev.index(bp_0)
        j = pi_rev.index(bp_0 + 1)

        if i < j:
            pi_revs = reversal_pi_p(pi_rev,i + 1,j)
        else:
            pi_revs = reversal_pi_p(pi_rev,j + 1,i)
        pi_revs_bps = bp_pair(pi_revs)
        if pi_revs not in possible_revs and len(pi_revs_bps) < len(pi_rev_bps):
            possible_revs.append(pi_revs)
        
    for bp_1 in bp_index_1s:
        if bp_1 + 1 not in bp_index_1s or bp_1 + 1 == max_point:
            continue

        i = pi_rev.index(bp_1)
        j = pi_rev.index(bp_1 + 1)

        if i < j:
            pi_revs = reversal_pi_p(pi_rev,i + 1,j)
        else:
            pi_revs = reversal_pi_p(pi_rev,j + 1,i)

        pi_revs_bps = bp_pair(pi_revs)
        if pi_revs not in possible_revs  and len(pi_revs_bps) < len(pi_rev_bps):
            possible_revs.append(pi_revs)

    
    
    

    k = pi_rev.index(max_point-1)
    max_k = pi_rev.index(max_point)
    possible_revs.append(pi_rev[:k] + pi_rev[k:max_k][::-1] + pi_rev[max_k:])
    return possible_revs

def shortest_path(pi_rev: list) -> int:
    min_step = float('inf')
    def shortest_path_finder(pi_rev: list, step: int) -> int:
        nonlocal min_step
        if pi_rev == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            if step < min_step:
                min_step = step
            return None

        poss_rev = possible_rev(pi_rev)

        for pi_rev in poss_rev:
            shortest_path_finder(pi_rev, step + 1)

    shortest_path_finder(pi_rev, 0)

    return min_step


if __name__ == '__main__':
    with open('rosalind_rear.txt', 'r') as file:
        pi = ''
        sigma = ''
        reversal = []
        for line in file:
            if line == '\n':
                reversal.append([pi,sigma])
                pi = ''
                sigma = ''
                continue
            elif pi == '':
                pi = line.strip()
            else:
                sigma = line.strip()
        reversal.append([pi,sigma])
        print(reversal)

with open('result.txt','w') as file:
    for pi_sigma in reversal:
        pi = [int(i) for i in pi_sigma[0].split(' ')]
        sigma = [int(i) for i in pi_sigma[1].split(' ')]

        ident_list = identity_permutation(pi, sigma)
        file.write(' ' + str(shortest_path(ident_list)))