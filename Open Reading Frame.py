filename = input('Please enter file name:')

# fasta file with single dna into the dna sequence or it could be used the protein sequence. 
def single_file(file_name):
    with open(file_name, 'r') as fasta:
        content = fasta.read()

    seq = [line for line in content.splitlines()[1:]]
    return ''.join(seq)
 
# "c:/Users/maiba/Desktop/Rosaline/Bioinformatics Stronghold/Open_reading_frame.txt"

# return incomplete protein and input could be rna or dna depend on the codons
def incomp_traslate(mRNA):
    protein = []
    length = len(mRNA)
    protein = [codon_to_amino_acid.get(mRNA[i:i+3]) for i in range(0,length,3) if codon_to_amino_acid.get(mRNA[i:i+3])]
    return ''.join(protein)

# translate the incomplite protein sequence into the complete protein sequence with methionine and end before the stop codon
# input incomplete protein
# output complite protein
def comp_translate(protein):
    proteins = []
    for i in range(len(protein)):
        if protein[i] == 'M':
            for j in range(i,len(protein)):
                if protein[j] == '_':
                    proteins.append(protein[i:j])
                    break
    return proteins

# return the dna into complimentary dna sequence
def reverse_dna(dna):
    dict_rev = {'A':'T','T':'A','G':'C','C':'G'}
    rev_lst = [dict_rev.get(nuc) for nuc in reversed(dna) if dict_rev.get(nuc)]
    return ''.join(rev_lst)

codon_to_amino_acid = {
    "ATA": "I", "ATC": "I", "ATT": "I", "ATG": "M",
    "ACA": "T", "ACC": "T", "ACG": "T", "ACT": "T",
    "AAC": "N", "AAT": "N", "AAA": "K", "AAG": "K",
    "AGC": "S", "AGT": "S", "AGA": "R", "AGG": "R",
    "CTA": "L", "CTC": "L", "CTG": "L", "CTT": "L",
    "CCA": "P", "CCC": "P", "CCG": "P", "CCT": "P",
    "CAC": "H", "CAT": "H", "CAA": "Q", "CAG": "Q",
    "CGA": "R", "CGC": "R", "CGG": "R", "CGT": "R",
    "GTA": "V", "GTC": "V", "GTG": "V", "GTT": "V",
    "GCA": "A", "GCC": "A", "GCG": "A", "GCT": "A",
    "GAC": "D", "GAT": "D", "GAA": "E", "GAG": "E",
    "GGA": "G", "GGC": "G", "GGG": "G", "GGT": "G",
    "TCA": "S", "TCC": "S", "TCG": "S", "TCT": "S",
    "TTC": "F", "TTT": "F", "TTA": "L", "TTG": "L",
    "TAC": "Y", "TAT": "Y", "TAA": "_", "TAG": "_",
    "TGC": "C", "TGT": "C", "TGA": "_", "TGG": "W",
}

def orfs(file_name):

    dna_seq = single_file(file_name)
    reverse_dna_seq = reverse_dna(dna_seq)

    frame = []
    for i in range(3):
        dna = dna_seq[i:]
        rev_dna = reverse_dna_seq[i:]
        in_prt = incomp_traslate(dna)
        in_prt1 = incomp_traslate(rev_dna)
        prt = comp_translate(in_prt) # list
        prt1 = comp_translate(in_prt1) # list
        total_prt = prt + prt1
        for prot in total_prt:
            if prot not in frame and prot != '':
                frame.append(prot)
    
    return frame

proteins = orfs(filename)
for prt in proteins:
    print(prt)

