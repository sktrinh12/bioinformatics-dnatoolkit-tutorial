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



# side note: this is O( (n * len(seq)-k + 1)*k ) time complexity
# bc we are running the loop from 0 to len(seq) -k + 1 times
# and we have to compare k letters or characters in each iteration


# also to note: The chance of any one base occurring next in the
# sequence is 0.25. The chance of three specified bases occurring
# is therefore 0.25*0.25+0.25 = 0.015625. The number of trials at
# which this can occur is given by the length of the sequence minus
# the length of the k-mer + 1. In this case 540 - 3 + 1 = 538. The
# event of three specified bases occurring in order would therefore be
# likely to occur 538*0.01562 = 8.40625 times in a sequence of 540 bases.

# if k = 8; we expect an 8-mer to appear every 4^8 = 65536 nucleotides,
# so that seeing one occur four times is quite surprising.
