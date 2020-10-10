from import_template import *

# dna_str = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


dna_str = readTextFile('rosalind_ini.txt')
# print(dna_str)
seq = bio_seq(dna_str)
seq_cnts = seq.nucleotide_frequency()
# print(seq_cnts)

# output result based on sorted nucleotides: A,C,G,T
print(' '.join([str(cnt) for nuc, cnt in sorted(seq_cnts.items(), key=lambda s:s[0])]))


