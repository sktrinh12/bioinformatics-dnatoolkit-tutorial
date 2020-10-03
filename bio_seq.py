from bio_structs import *
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
        return set(NUCLEOTIDES).issuperset(self.seq)


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
        seq = ''.join([random.choice(NUCLEOTIDES)
                       for x in range(length)])

        # reinitialise it
        self.__init__(seq, seq_type, 'Randomly generated sequence')
