from DNAToolKit import *
import random
from utils import coloured

rndDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(rndDNAStr)
print(f'\nSequence: {coloured(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(coloured(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {coloured(transcription(DNAStr))}\n')
print(f"[4] + DNA String + Complement + Reverse Complement: \n3' {coloured(DNAStr)} 5' [Complement]")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"5' {coloured(reverse_complement(DNAStr))} 3' [Rev. Complement]\n")

print(f"[5] + GC Content: {gc_content(DNAStr)}%\n")

print(f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')

print(f'[7] + Amino acids sequence from DNA: {translate_seq(DNAStr, 0)}\n')
print(f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')
