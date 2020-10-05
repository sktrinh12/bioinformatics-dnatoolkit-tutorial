import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..', '..'))
from bio_seq import *
from utils import readTextFile


DNAString = bio_seq('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
result = DNAString.nucleotide_frequency()
# print(result)
print(' '.join([str(val) for key, val in result.items()]))


DNAString = bio_seq(readTextFile('rosalind_dna.txt'))
result = DNAString.nucleotide_frequency()
print(' '.join([str(val) for key, val in result.items()]))
