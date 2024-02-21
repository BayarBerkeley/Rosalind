# method fr findng the scores for each matching sequence using "find" 
def score_find(string1, string2):
    pre_index = 0
    for i in range(1, len(string1) + 1):
        # frist sequence from back to front
        str_check = string1[-i:]
        index = string2.find(str_check)
        if index == -1:
            return pre_index, string2.find(string1[-pre_index:])
        else:
            pre_index = i
    # output: highest index(score) of matching sequence on first string and
            # match on second (actually we are looking for 0)
    return pre_index, string2.find(string1[-pre_index:])


def join_strings(pre_index, string1, string2):
    return string1 + string2[pre_index:]


with open('c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/Genome Assembly as Shortest Superstring/rosalind_long.txt', 'r') as file:
    list_of_sequences = {}
    key, sequence = '', ''

    for line in file:
        if line.startswith('>'):
            if key:
                list_of_sequences[key] = sequence
                sequence = ''
            key = line.rstrip()
        else:
            sequence += line.rstrip()
    list_of_sequences[key] = sequence

superstr = ''
seqs = list(list_of_sequences.values())

# key is not actually used but we need the iteration 
for key in list_of_sequences:
    if not superstr:
        # superstr is the superstring we are looking for 
        superstr = list_of_sequences[key]
        seqs.remove(list_of_sequences[key])

    score = []
    compare_seq = ''

    # seqs is decreasing eventually it will be emptied. 
    if not seqs:
        break

    for seq in seqs:
        matching_index, boolean = score_find(superstr, seq)
        score.append((matching_index, boolean))

    max_index = max(range(len(score)), key=lambda i: score[i][0])

    indices_strings = score[max_index] # ex: (546, 0)

    # used for index boolean if the second index is not 0
    switch = False

    if indices_strings[1]:
        score = []
        for seq in seqs:
            matching_index, boolean = score_find(seq, superstr)
            score.append((matching_index, boolean))
        max_index = max(range(len(score)), key=lambda i: score[i][0])
        indices_strings = score[max_index]
        switch = True

    # Check whether the sequence needs to be reversed
    if indices_strings[0] != -1:
        compare_seq = seqs[max_index]
        if switch:
            superstr = join_strings(indices_strings[0], compare_seq, superstr)
        else:
            superstr = join_strings(indices_strings[0], superstr, compare_seq)
        seqs.remove(compare_seq)

# Output the final superstring
with open("result.txt", "w") as file:
    file.write(superstr)
