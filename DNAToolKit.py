from collections import Counter
from structures import *

#check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


# count nucleotides
def countNucFrequency(seq):
    # tmpFreqDict = {"A" : 0, "C":0, "G":0, "T":0}
    # for nuc in seq:
    #     tmpFreqDict[nuc] += 1
    # return tmpFreqDict
    return dict(Counter(seq))

def transcription(seq):
    """
    DNA -> RNA transcription (replace Thymine to Uracil)
    """
    return seq.replace("T", "U")

def reverse_complement(seq):
    """
    swap Thymine with Uracil for RNA complement string
    """
    # return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]

# {
def gc_content(seq):
    """
    GC Content in DNA/RNA sequence
    """
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)
#}


#{
def gc_content_subsec(seq, k=20):
    """
    GC Content in DNA/RNA sub-sequence length k, k =20 by default
    """
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res
#}

#{
def translate_seq(seq, init_pos = 0):
    """
    Translates a DNA sequence into an amino acid sequence; jumps of 3
    """
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2,
                                                          3)]
#}

#{
def codon_usage(seq, aminoacid):
    """
    Provides the frequency of each codon encoding a given aminoacid in a DNA
    sequence
    """
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict
#}
