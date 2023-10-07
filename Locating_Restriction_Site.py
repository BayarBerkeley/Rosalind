
def read_fasta(file_path):
    """Reads a fasta file and returns the sequence as a single string."""
    with open(file_path, 'r') as fasta:
        lines = fasta.read().splitlines()[1:]
        return ''.join(lines)

def reverse_complement(seq):
    """Returns the reverse complement of a DNA sequence."""
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join([comp[nucleotide] for nucleotide in seq[::-1]])

def palindromic_length(seq):
    rev_seq = reverse_complement(seq)
    for i in range(12,3,-1):
        if seq[:i] == rev_seq[-i:] and len(seq) >= i:
            return i
    return 0

def find_restriction_sites(seq):
    """Finds and returns positions and lengths of palindromic sequences within the given DNA sequence."""
    location = []
    for i in range(len(seq) - 3):
        window = seq[i:i+12]
        length = palindromic_length(window)
        if length:
            print(str(i+1) + " " + str(length))
            location.append([i+1, length])
    return location

def main():
    file_path = input("Enter your fasta file: ")
    sequence = read_fasta(file_path)
    rest_site = find_restriction_sites(sequence)

    with open('result.txt', 'w') as txt:
        for site in rest_site:
            txt.write("{} {}\n".format(site[0], site[1]))
            print("{} {}".format(site[0], site[1]))


if __name__ == "__main__":
    main()

    

            
        

