from import_template import *


dna_str = readTextFile('vibrio_cholerae_seq.txt')
# print(dna_str[:100])
res = bio_seq(dna_str).nucleotide_frequency()

print(res)


# OriC in Vibrio cholorae is a specific sequence that initiates replication in the circular genome.  As the proteins that replicate DNA are similar across many similar organisms, the OriC must be similar.  This is the known Vibrio sequence, using this sequence we can try to find the unknown origin of replication in E. coli, Campylobacter, etc.


# "Nothing in Biology Makes Sense except in the Light of Evolution".  If a word has some biological meaning, then the more copies of the word, the more likely that this word will be recognized, and the less likely it is that a mutation will disrupt the process
