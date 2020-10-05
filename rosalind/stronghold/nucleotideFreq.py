from import_template import *

DNA_str = bio_seq(readTextFile('./rosalind/stronghold/sample_sequence.txt'))
result = DNA_str.nucleotide_frequency()
# print(result)
print(' '.join([str(v) for k,v in result.items()]))
