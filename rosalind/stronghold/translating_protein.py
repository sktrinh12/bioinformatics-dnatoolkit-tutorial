from import_template import *

if __name__ == "__main__":
    dna_input = readTextFile('rosalind_prot.txt')
    # dna_input = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    protein =  bio_seq(dna_input, seq_type = 'RNA').translate_seq(show_end = False, return_type = str)
    print(protein)
