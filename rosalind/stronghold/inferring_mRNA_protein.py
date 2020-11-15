from import_template import *
from bio_structs import RNA_CODONS

a = 29
b = 73
c = 10
d = 32
n = 11

# reverse the dictionary
PROTEIN_RNA_CODONS = {aa : [] for codon, aa in RNA_CODONS.items()}
for k,v in RNA_CODONS.items():
    PROTEIN_RNA_CODONS[v].append(k)

print(PROTEIN_RNA_CODONS)

print()

# Two useful facts in modular arithmetic are that if a≡b mod n
# and c≡d mod n, then a+c≡b+d mod n and a×c ≡ b×d mod n. To check
# your understanding of these rules, you may wish to verify
# these relationships for a=29, b=73, c=10, d=32, and n=11

for i in [a,b,c,d]:
    print(f'{i} mod {n} -> {i % n}')

print()

for i,j in [(a,c), (b,d)]:
    print(f'{i}+{j} mod {n} -> {(i+j) % n}')
    print(f'{i}x{j} mod {n} -> {(i*j) % n}')


#######################

# A protein string of length at most 1000 aa
# The total number of different RNA strings from 
# which the protein could have been translated, 
# modulo 1,000,000. (Don't neglect the importance 
# of the stop codon in protein translation)

# must multiple each possibility by 3 since there are 
# three ways to terminate (stop) the protein translation

with open('rosalind_mrna.txt', 'r') as f:
    AA = f.readline().strip()
print()
print('='*50)
print(AA)
# AA = 'MA'

combos = len(PROTEIN_RNA_CODONS['_']) # three stop codons
for aa in AA:
    combos = combos * len(PROTEIN_RNA_CODONS[aa]) % 1e6

print()
print(int(combos))

####ANOTHER METHOD#####

# with open('RNA_codon_table.txt', 'r') as input_data:
#         rna_to_protein = [line.strip().split() for line in input_data.readlines()]

# rna_dict = {}
# for translation in rna_to_protein:
#     rna_dict[translation[0]] = translation[1]

# rna_num = list(rna_dict.values()).count('Stop') # 3
# print()
# # print(rna_dict)
# for aa in AA:
#     rna_num = rna_num * list(rna_dict.values()).count(aa) % 1e6

# print(int(rna_num))
