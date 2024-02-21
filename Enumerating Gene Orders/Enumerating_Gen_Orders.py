numb = input('Enter Positive Integer:')

try:
    numb_int = int(numb)
    print("You entered the integer: {}".format(numb_int))
except ValueError:
    print("Please enter a valid integer.")


list_of_number = [str(i + 1) for i in range(numb_int)]

def get_premutation(list_num):
    # Base case: If only one element, return it wrapped in a list
    if len(list_num) == 1:
        return [list_num]
    
    list_output = []
    for s in list_num:
        # Create a new list without the current element s
        new_list = [t for t in list_num if t != s]
        # Recursively get the permutations of the new list
        last = get_premutation(new_list)
        for premut in last:
            # Add the current element s to the beginning of each permutation
            list_output.append([s] + premut)
    
    return list_output

with open('result.txt', 'w') as file:
    list = get_premutation(list_of_number)
    file.write(str(len(list)) + '\n')
    for lst in list:
        file.write(' '.join(lst) + '\n')

'''
1

1 2
2 1

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
'''
