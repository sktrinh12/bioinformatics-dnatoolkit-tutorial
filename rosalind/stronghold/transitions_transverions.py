from import_template import *
import re


# orig_dna_str = bio_seq('GAGCCTACTAACGGGAT')
# cmpr_dna_str = 'CATCGTAATGACGGCCT'
# print(orig_dna_str.hamming_distance(cmpr_dna_str))

# input_seq = read_FASTA('transitions_transversions_test.txt')
input_seq = read_FASTA('rosalind_tran.txt')

# print(input_seq)
descriptions = list(input_seq.keys())
orig_dna_str = input_seq[descriptions[0]]
cmpr_dna_str = input_seq[descriptions[1]]

# print(orig_dna_str)
# print(cmpr_dna_str)

# dna_str = bio_seq(orig_dna_str)
# print(dna_str.hamming_distance(cmpr_dna_str)) # 31


def pt_mutation_type(nuc_a, nuc_b, seq_length):
    """
    assign transition or transversion
    1 - transition
    0 - transversion
    """
    if re.search('[A|G]', nuc_a) and re.search('[A|G]', nuc_b):
        return 1
    elif re.search('[C|T]', nuc_a) and re.search('[C|T]', nuc_b):
        return 1
    elif re.search('[A|G]', nuc_a) and re.search('[C|T]', nuc_b):
        return 0
    elif re.search('[C|T]', nuc_a) and re.search('[A|G]', nuc_b):
        return 0


seq_length = len(orig_dna_str)
types_list = []
# cnt = 0
for nuc_a, nuc_b in zip(orig_dna_str, cmpr_dna_str):
    if nuc_a != nuc_b:
        check = pt_mutation_type(nuc_a, nuc_b, seq_length)
        types_list.append(check)
        # print(f'{cnt} - {check} / {nuc_a}|{nuc_b}')
        # cnt+=1

nbr_transitions = sum(types_list)
print(nbr_transitions/(len(types_list)-nbr_transitions))
