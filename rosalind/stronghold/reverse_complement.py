from import_template import *


DNA_str = bio_seq(readTextFile('./rosalind/stronghold/rosalind_revc.txt'))
# DNA_str = bio_seq('AAAACCCGGT')

print()
print('='*50)
print()
print(DNA_str.reverse_complement())
print()
print('='*50)
