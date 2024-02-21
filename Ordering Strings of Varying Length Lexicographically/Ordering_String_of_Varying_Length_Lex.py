coll = []
def length_lex_order(str_order, str_to_return, num):
    if num == 0:
        return None
    for n in str_order:
        coll.append(str_to_return + n)
        length_lex_order(str_order,str_to_return + n, num - 1 )

if __name__ == '__main__':
    with open('rosalind_lexv.txt', 'r') as file:
        given_str = file.readlines()
        str_order = given_str[0].strip().split(' ')
        num = int(given_str[1])

    length_lex_order(str_order,'',num)

    
    with open('result.txt','w') as file:
        for line in coll:
            file.write(line + '\n')
