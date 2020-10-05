from bio_structs import *
from collections import Counter
from bio_structs import NUCLEOTIDES_BASE, DNA_CODONS, RNA_CODONS
import random

class bio_seq:
    """
    DNA sequence class. Default value: ATCG, DNA, no label
    """

    def __init__(self, seq='ATCG', seq_type='DNA', label='No label'):
        """
        Sequence initialisation validation
        """
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} type"

    # double underscore makes it a private function that won't be accessible
    # outside of the class; won't be exposed
    def __validate(self):
        """
        check the sequence to make sure it is a valid DNA string
        """
        # is the parent set of the set in question; returns True or False
        return set(NUCLEOTIDES_BASE[self.seq_type]).issuperset(self.seq)


    def get_seq_biotype(self):
        """
        Returns sequence type
        """
        return self.seq_type

    def get_seq_info(self):
        """
        Returns 4 strings: Full sequence information
        """
        return f'[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}'

    def generate_rnd_seq(self, length = 10, seq_type = 'DNA'):
        """
        Generate random DNA sequence, provided the length
        """
        seq = ''.join([random.choice(NUCLEOTIDES_BASE[seq_type]) for x in range(length)])

        # reinitialise it
        self.__init__(seq, seq_type, 'Randomly generated sequence')

    def nucleotide_frequency(self):
        """
        Count nucleotides in  a given sequence. Reutnrs a dictionary
        """
        return dict(Counter(self.seq))

    def transcription(self):
        """
        DNA -> RNA Transcription, replacing Thymine with Uracil
        """
        if self.seq_type == 'DNA':
            return self.seq.replace('T', 'U')
        return 'Not a DNA sequence'

    def reverse_complement(self):
        """
        Swapping adenine with thymine and guanine with cyosine. Reversing newly
        generated string
        """
        if self.seq_type == 'DNA':
            mapping = str.maketrans('ATCG', 'TAGC')
        else:
            mapping = str.maketrans('AUCG', 'UAGC')
        return self.seq.translate(mapping)[::-1]

    def gc_content(self, within_fx_seq=None):
        """
        GC content in DNA/RNA sequence
        """
        seq_ = self.seq
        if within_fx_seq:
            seq_ = within_fx_seq
        gc_content = 100*(seq_.count('C') + seq_.count('G')) /len(seq_)
        return round(gc_content, 7)

    def gc_content_subsec(self, k=20):
        """
        GC Content in a DNA/RNA sub-sequence length k, k=20 by default
        """
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i + k]
            res.append(self.gc_content(subseq))
        return res

    def translate_seq(self, init_pos=0):
        """
        Translates a DNA sequence into an amino acid sequence; jumps of 3
        """
        if self.seq_type == 'DNA':
            return [DNA_CODONS[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) -2, 3)]
        elif self.seq_type == 'RNA':
            return [RNA_CODONS[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq) -2, 3)]

    def codon_usage(self, aminoacid):
        """
        Provides the frequency of each codon encoding a given aminoacid in a DNA
        sequence
        """
        tmpList = []
        if self.seq_type == 'DNA':
            for i in range(0, len(self.seq) - 2, 3):
                if DNA_CODONS[self.seq[i:i + 3]] == aminoacid:
                    tmpList.append(self.seq[i:i + 3])
        elif self.seq_type == 'RNA':
            for i in range(0, len(self.seq) - 2, 3):
                if RNA_CODONS[self.seq[i:i + 3]] == aminoacid:
                    tmpList.append(self.seq[i:i + 3])

        freqDict = dict(Counter(tmpList))
        totalWeight = sum(freqDict.values())
        for seq in freqDict:
            freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
        return freqDict


    def gen_reading_frames(self):
        """
        Generate the six reading frames of a DNA sequence, including the reverse
        complement
        """
        frames = []
        # read from the beginning frame and then second and third

        # DNA has two strands, the ribosome can read an RNA derived
        # from one strand or another, and it can read it in 1-2-3s
        # that are separated one from another so you can actually
        # get three reading frames reading in one direction, three
        # reading frames going in the other direction. So it's actually
        # six different reading frames for every piece of DNA, which
        # might give you an open reading frame.
        frames.append(self.translate_seq(0))
        frames.append(self.translate_seq(1))
        frames.append(self.translate_seq(2))
        # reverse_complement returns a copy
        tmp_seq = bio_seq(self.reverse_complement(), self.seq_type)
        frames.append(tmp_seq.translate_seq(0))
        frames.append(tmp_seq.translate_seq(1))
        frames.append(tmp_seq.translate_seq(2))
        # help garbage collector clean up
        del tmp_seq
        return frames


    def proteins_from_rf(self, aa_seq):
        """
        Compute all possible proteins in an amino acid sequence and return a list of possible proteins
        """
        current_prot = []
        proteins = []
        for aa in aa_seq:
            if aa == "_":
                # STOP accumulating amino acids if _ - STOP was found
                if current_prot:
                    for p in current_prot:
                        proteins.append(p)
                    # reset for next protein
                    current_prot = []
            else:
                # START accumlating amino acids if M - START was found
                if aa == "M":
                    # dummy variable to add the first amino acid of the start codon
                    current_prot.append("")
                for i in range(len(current_prot)):
                    current_prot[i] += aa
        return proteins

    def all_proteins_from_orfs(self, startReadPos=0, endReadPos=0, ordered=False):
        """
        Compute all possible proteins for all open reading frames. Protein search
        DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2
        API can be used to pull protein info
        """
        # generate from a slice or subset
        if endReadPos > startReadPos:
            tmp_seq = bio_seq(
                self.seq[startReadPos: endReadPos],
                self.seq_type)
            rfs = tmp_seq.gen_reading_frames()
        # or whole sequence
        else:
            rfs = self.gen_reading_frames()

        res = []
        for rf in rfs:
            # generate a protein
            prots = self.proteins_from_rf(rf)
            for p in prots:
                res.append(p)

        # sort by length of entries, longest to shortest
        # typically interested in longest sequences
        if ordered:
            return sorted(res, key=len, reverse=True)
        return res
