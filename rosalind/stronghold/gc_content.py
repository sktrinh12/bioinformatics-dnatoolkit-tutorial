from import_template import *


# returns a dictionary
# fasta = read_FASTA('./rosalind/stronghold/sample_rosalind_gc_content.fasta')
fasta = read_FASTA('./rosalind/stronghold/rosalind_gc.txt')
# print(fasta)

result_dct = {}
for label, seq in fasta.items():
    DNA_str = bio_seq(seq)
    result_dct[label.replace('>', '')] = DNA_str.gc_content()

# sort dictionary based on highest GC content
result = {label:gc for label, gc in sorted(result_dct.items(), key= lambda x : x[1], reverse = True)}
first_label = [l for l in result.keys()][0]

print(result)
print()
print('='*50)
print()
print(first_label)
print(result[first_label])
print()
print('='*50)
