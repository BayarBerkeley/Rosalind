def identity_permutation(num1: list ,num2: list) -> list:
    new_num = []
    for i in range(len(num1)):
        new_num.append(num1.index(num2[i]) + 1)
    return new_num

def bp_pair(ident_list: list) -> dict:
    break_point = {}
    dec = []
    inc = []
    for i in range(len(ident_list)-1):
        if abs(ident_list[i] - ident_list[i + 1]) != 1:
            break_point[(ident_list[i],ident_list[i+1])] = i
        if ident_list[i] + 1 == ident_list[i + 1]:
            inc.append(ident_list[i])
    return inc,break_point

def reversal_pi_p(pi_list: list, i: int, j:int) -> list:
    return pi_list[:i] + pi_list[i:j+1][::-1] + pi_list[j+1:]

def find_closest(break_points: list, inc: list, i: int) -> list:
    print(inc)
    lowest = break_points[i]
    for bp in break_points:
        if (bp[0] + 1) not in inc and not lowest:
            lowest = bp
            break

    def in_break_point(break_points, intial_break_point):
        if break_points == []:
            return []
        for bp in break_points:
            if (intial_break_point[0] - bp[0]) == 1 and (intial_break_point[1] - bp[1]) == -1:
                return [intial_break_point, bp]
            elif (intial_break_point[0] - bp[0]) == -1 and (intial_break_point[1] - bp[1]) == 1:
                return [intial_break_point, bp]
        return in_break_point(break_points[1:],break_points[0])   
     
    double_bp = in_break_point(break_points[1:], break_points[0])

    if double_bp != []:
        return double_bp
    else:
        return [lowest]

def reversal_distance(ident_list: list) -> int:
    ident_list = [0] + ident_list + [len(ident_list)+1]
    count = 0
    count_bps = len(ident_list) - 1
    pre_ident = ident_list
    locat_bp = 0
    while ident_list != [0,1,2,3,4,5,6,7,8,9,10,11]:
        inc,break_point = bp_pair(ident_list)
        if count_bps <= len(break_point.keys()):
            ident_list = pre_ident
            locat_bp +=1
            count -=1
        else:
            pre_ident = ident_list
            count_bps = len(break_point.keys())
            locat_bp = 0
        print(break_point)
        changing_point = find_closest(list(break_point.keys()), inc, locat_bp)
        print(changing_point)
        count +=1
        if len(changing_point) == 1:
            j = ident_list.index(changing_point[0][0] + 1)
            i = break_point[changing_point[0]] + 1
            ident_list = reversal_pi_p(ident_list,i,j)
        else:
            i = break_point[changing_point[0]] + 1
            j = break_point[changing_point[1]]
            ident_list = reversal_pi_p(ident_list,i,j)
    return count

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


for pi_sigma in reversal:
    pi = [int(i) for i in pi_sigma[0].split(' ')]
    sigma = [int(i) for i in pi_sigma[1].split(' ')]

    ident_list = identity_permutation(pi, sigma)

    print(reversal_distance(ident_list))
    
    print('---------------------')




        


