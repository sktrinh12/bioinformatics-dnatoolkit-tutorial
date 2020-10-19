def frequent_codons(seq, k):
    """
    Provides the frequency of each codon encoding a given amino acid sequence
    or a k-mers motif; computes how many times each k-mer appears in the
    sequence and returns a dictionary of those values
    """
    k = int(k)
    cnt_kmer = {}
    for i in range(0, len(seq) - k+1 , 1):
        kmer = seq[i:i + k]
        # print(f'{i} - {kmer}')
        if kmer in cnt_kmer:
            cnt_kmer[kmer] += 1
        else:
            cnt_kmer[kmer] = 1


    return cnt_kmer

def get_max_count(dct):
     v=list(dct.values())
     k=list(dct.keys())
     return max(v)

# test sample datasets
# res = frequent_codons('ACGTTGCATGTCGCATGATGCATGAGAGCT',4)
# res = frequent_codons('ACTGACTCCCACCCC', 3)

with open('dataset_2_10.txt', 'r') as f:
    content = f.readlines()

# print(content)
SEQ = content[0].strip()
k = content[1].strip()
res = frequent_codons(SEQ, k)
max_val = get_max_count(res)

print(' '.join([kmer for kmer,cnt in res.items() if cnt == max_val]))
