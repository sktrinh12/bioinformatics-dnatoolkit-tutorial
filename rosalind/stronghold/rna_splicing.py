from import_template import *

# sample dataset
# SEQ = 'ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
# intron1 = 'ATCGGTCGAA'
# intron2 = 'ATCGGTCGAGCGTGT'
# introns = [intron1, intron2]

def splice_dna(sequence, introns):
    """
    remove introns in sequence and expose only exons
    """
    for intron in introns:
        len_intron = len(intron)
        for i in range(0, len(sequence) - len_intron+1, 1):
                if sequence[i:i + len_intron] == intron:
                    start = i
                    end = i+len_intron
                    sequence = sequence[0: start:] + sequence[end : :]

    return sequence


# read FASTA file as dictionary
dct_dna = read_FASTA('rosalind_splc.txt')

# assuming fasta file has the dna string at the beginning and subsequent
# entries are the introns
keys = list(dct_dna.keys())
dna_str = dct_dna[keys[0]]
introns = [dct_dna[k] for k in keys[1:]]

# splice the dna string to expose exons
exons = splice_dna(dna_str,introns)
# print(exons)

# transcribe into rna string
rna = bio_seq(exons).transcription()

# translate into protein
prot = bio_seq(rna, 'RNA').translate_seq()

# remove the stop codon, underscore
prot = [aa for aa in prot if aa != '_']
print(''.join(prot))
