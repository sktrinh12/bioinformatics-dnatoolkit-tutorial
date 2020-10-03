from bio_seq import *


test_dna = bio_seq('ATCGGCTAGCTAGCTAGCTAGCTACG', 'DNA', 'Test label')

print(test_dna.get_seq_info())
# print(test_dna.get_seq_biotype())
test_dna.generate_rnd_seq(40, 'DNA')
print(test_dna.get_seq_info())
