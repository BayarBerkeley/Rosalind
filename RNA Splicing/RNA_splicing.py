# Importing the translation function from the translation module.
from translation import translation

def read_fasta_splice(file_name):
    """
    Reads a FASTA file, extracting a main DNA sequence and a list of intron sequences.
    Assumes the first sequence in the file is the main one.
    """
    with open(file_name, 'r') as fasta:
        list_seq = fasta.read().splitlines()[1:]
        sequence_list = [] # To store the main DNA sequence.
        intron = [] # To store all the intron sequences.
        main_sequence = True # Flag to check if we're reading the main sequence.

        for line in list_seq:
            if line.startswith('>'):
                if sequence_list: # If we've started reading the main sequence
                    main_sequence = False # Switch to reading introns.
                continue # Skip the descriptor lines.
            
            if main_sequence:
                sequence_list.append(line)
            else:
                intron.append(line)
        return ''.join(sequence_list), intron

def DNA_to_pre_mRNA(seq):
    # Converts a DNA sequence to a pre-mRNA sequence by replacing Thymine with Uracil.
    return seq.replace('T','U')

def pre_mRNA_to_mRNA(seq, introns):
    # Removes introns from the pre-mRNA sequence to produce the final mRNA sequence.
    for intron in introns:
        seq = seq.replace(DNA_to_pre_mRNA(intron),"")
    return seq

def main():
    # Main function to orchestrate the reading, splicing, and translation processes.
    file_name = input('Enter File Name: ')
    sequence, introns = read_fasta_splice(file_name)
    pre_mRNA = DNA_to_pre_mRNA(sequence)
    mRNA = pre_mRNA_to_mRNA(pre_mRNA,introns)
    protein = translation(mRNA)
    with open("result.txt","w") as file:
        file.write(protein)

        
if __name__ == "__main__":
    main()
