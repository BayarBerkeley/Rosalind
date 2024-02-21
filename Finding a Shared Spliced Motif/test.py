def lcs_backtrack(v, w):
    s = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]
    backtrack = [[0] * (len(w) + 1) for _ in range(len(v) + 1)]

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            if v[i - 1] == w[j - 1]:
                s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + 1)
            else:
                s[i][j] = max(s[i - 1][j], s[i][j - 1])

            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = "right"
            else:
                backtrack[i][j] = "diagonal"

    return backtrack

def output_lcs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "down":
        return output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "right":
        return output_lcs(backtrack, v, i, j - 1)
    else:
        return output_lcs(backtrack, v, i - 1, j - 1) + v[i - 1]

def lcs(v, w):
    backtrack = lcs_backtrack(v, w)
    return output_lcs(backtrack, v, len(v), len(w))

with open('rosalind_lcsq.txt', 'r') as file:
    sequences = []
    current_sequence = ""
    for line in file:
        if line.startswith('>'):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line.strip()
    sequences.append(current_sequence)

seq1, seq2 = sequences

result = lcs(seq1, seq2)

with open('result.txt', 'w') as file:
    file.write(result)

print(result)
