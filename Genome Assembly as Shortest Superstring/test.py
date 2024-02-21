# ChatGPt version 

def overlap(str1, str2):
    """
    Returns the maximum overlap length of two strings.
    """
    max_overlap = 0
    for i in range(1, len(str1)):
        if str2.startswith(str1[i:]):
            max_overlap = max(max_overlap, len(str1) - i)
    return max_overlap


def merge_strings(str1, str2):
    """
    Merges two strings based on their maximum overlap.
    """
    max_overlap = overlap(str1, str2)
    return str1 + str2[max_overlap:]


def find_shortest_superstring(strings):
    """
    Finds the shortest superstring containing all given strings.
    """
    while len(strings) > 1:
        max_overlap_length = 0
        merge_indices = (0, 1)

        for i in range(len(strings)):
            for j in range(i + 1, len(strings)):
                current_overlap = overlap(strings[i], strings[j])

                if current_overlap > max_overlap_length:
                    max_overlap_length = current_overlap
                    merge_indices = (i, j)

        merged_string = merge_strings(strings[merge_indices[0]], strings[merge_indices[1]])
        strings.pop(max(merge_indices))
        strings.pop(min(merge_indices))
        strings.append(merged_string)

    return strings[0]


# Example usage:
fasta_data = [
    ">read1",
    "ATCGTACGTA",
    ">read2",
    "TACGTACGTA",
    ">read3",
    "GTACGTACGT",
]

# Extracting DNA strings from FASTA data
dna_strings = [line.strip() for line in fasta_data if not line.startswith(">")]

result_superstring = find_shortest_superstring(dna_strings)
print(result_superstring)
