from import_template import *


DNA_str = bio_seq(readTextFile('./rosalind/stronghold/rosalind_rna.txt'))

print()
print('='*50)
print()
print(DNA_str.transcription())
print()
print('='*50)
