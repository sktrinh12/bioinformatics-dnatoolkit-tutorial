from import_template import *

# dna_str = 'GATATATGCATATACTT'
# motif = 'ATAT'

file_content = readTextFile('rosalind_subs.txt', '\n')
# print(file_content)
dna_str, motif = file_content.split('\n')
print(dna_str)
print(len(dna_str))
print()
print(motif)
print(len(motif))
find_motif = bio_seq(dna_str).substring_repeats(motif)
find_motif = ' '.join([str(nuc) for nuc in find_motif])
print(find_motif)
