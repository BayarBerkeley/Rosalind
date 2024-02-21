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

def shortest_path(Left_bp: dict, Right_bp: dict, find: tuple, path: list, pos: str):
    if find == path[-1] and len(path) > 1:
        return path
    elif pos == 'L' and (path[-1][0] + 1) in Left_bp:
        next_bp = (path[-1][0] + 1, Right_bp[path[-1][0] + 1])
        pos = 'R'
    elif pos == 'R' and (path[-1][1] + 1) in Right_bp:
        next_bp = (Left_bp[path[-1][1] + 1], path[-1][1] + 1)
        pos = 'L'
    else:
        return None
    return shortest_path(Left_bp, Right_bp, find, path.append(next_bp),pos)
    
                  


def find_shortest_path(break_points:list) -> list:
    bp_length = len(break_points)
    Left_0 = {}
    Right_1 = {}
    for bp in break_points:
        Left_0[bp[0]] = bp[1]
        Right_1[bp[1]] = bp[0]
    for bp in break_points:
        print(shortest_path(Left_0, Right_1,bp,[bp], 'L'))
    print(Left_0.keys())
    print(Right_1.keys())

bp_dic = {(0, 7): 6, (1, 5): 7, (6, 4): 9}
find_shortest_path(list(bp_dic.keys()))



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
    
