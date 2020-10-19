from import_template import *


# To compute Count(Text, Pattern), our plan is to “slide a window” down Text,
# checking whether each k-mer substring of Text matches Pattern.
# We say that Pattern is a most frequent k-mer in Text if it maximizes
# Count(Text, Pattern) among all k-mers

# dna_str = 'GCGCG'
# motif = 'GCG'
file_content = readTextFile('dataset_2_7.txt', '\n')
print(file_content)
print()
dna_str, motif = file_content.split('\n')
find_motif = bio_seq(dna_str).substring_repeats(motif)

print(len(find_motif))
