from import_template import *


# orig_dna_str = bio_seq('GAGCCTACTAACGGGAT')
# cmpr_dna_str = 'CATCGTAATGACGGCCT'
# print(orig_dna_str.hamming_distance(cmpr_dna_str))

input_seq = readTextFile('rosalind_hamm.txt', delim=',')

input_seq_list = [x for x in input_seq.split(',')]

orig_dna_str = input_seq_list[0]
cmpr_dna_str = input_seq_list[1]

dna_str = bio_seq(orig_dna_str)
print(dna_str.hamming_distance(cmpr_dna_str))
