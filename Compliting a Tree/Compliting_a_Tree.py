with open('rosalind_tree.txt', 'r') as file:
    count = 0 
    for line in file:
        line = line.split(' ')
        if len(line) == 1:
            num_nodes = int(line[0])
        else:
            count += 1
    
with open('result.txt','w') as file:
    file.write(str(num_nodes-count - 1))