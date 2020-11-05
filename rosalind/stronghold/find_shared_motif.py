from import_template import *
import multiprocessing
import time
# from math import ceil
from itertools import compress
import os
# import sys

# def generate_motifs(seq):
#     """
#     generate substring motifs from the dna string sequence
#     """
#     motifs = []
#     sq_len = len(seq)
#     for i in range(sq_len):
#         decrement = sq_len - i
#         for j in range(decrement):
#             sbseq = seq[i:i+j+1]
#             if len(sbseq) > 1:
#                 motifs.append(sbseq)
#     # print(f'{i} {j} {decrement} {seq}')
#     return motifs

def match_seq(subseq, srch_sequence):
    """
    check if each sub-sequence string exists in all of the dna sequences in the
    FASTA dictionary variable
    Returns a list of Trues or Falses
    """
    trues = []
    for sq in srch_sequence:
        trues.append(subseq in sq)
    return trues

# def longest_motif(motifs):
#     """
#     return the longest motif length
#     """
#     min_nbr = -sys.maxsize
#     for m in motifs:
#         length = len(m)
#         if length > min_nbr:
#             min_nbr = length
#     return min_nbr


# def shorest_motif(motifs):
#     """
#     return the shortest motif length
#     """
#     max_nbr = sys.maxsize
#     for m in motifs:
#         length = len(m)
#         if length < max_nbr:
#             max_nbr = length
#     return max_nbr

# file_content = read_FASTA('find_shared_motif_test.txt')
file_content = read_FASTA('rosalind_lcsm.txt')
# sort based on shortest sequence first
file_content = sorted(file_content.items(), key = lambda x: len(x[1]), reverse = True)
# print(file_content)

# given the test data the longest dna sequence string was 7 bp long;
# and the longest sub string was 2 bp long (2/7) ~ 0.28 (28%) of the
# max bp length; so this number should be roughly higher than 25%
# but in practice, the number was lowered to around 2%
size_threshold = 0.02

# for sq in file_content.values():
#     if first_iter:
#         motifs = generate_motifs(sq)
#         first_iter = False
#     else:
#         # add more motifs from the dna sequence
#         motifs = motifs + generate_motifs(sq)
#         max_nbr = longest_motif(motifs)
#         min_nbr = shorest_motif(motifs)
#         # filter out motifs that are same length as the query string
#         motifs = list(filter(lambda x: len(x) < max_nbr, motifs))
#         # filter out motifs that are too short based on DNA strings of 1 kbp
#         motifs = list(filter(lambda x: len(x) > int(size_threshold*max_nbr), motifs))
#         for m in motifs:
#             print(m)
#         print('='*40)
#         print()
#         # break

#         substrs = []
#         for m in motifs:
#             # print(m)
#             for j in range(ceil(len(sq)/len(m))+1):
#                 subseq = sq[j:j+len(m)]
#                 # print(subseq)
#                 if subseq == m:
#                     substrs.append(m)
#                 else:
#                     if m in motifs:
#                         motifs.remove(m)


# def main():
#     first_iter = True
#     substrs = []
#     all_sequences = []
#     for tup_dat in file_content:
#         if first_iter:
#             # generate motifs from shortest sequence
#             motifs = generate_motifs(tup_dat[1])
#             # filter out motifs that are same length as the sequence string itself
#             max_nbr = len(max(motifs, key=len))
#             motifs = list(filter(lambda x: len(x) < max_nbr, motifs))
#             # filter out motifs that are too short based on DNA strings of 1 kbp
#             motifs = list(filter(lambda x: len(x) > int(size_threshold*max_nbr), motifs))
#             # add the sequence
#             all_sequences.append(tup_dat[1])
#             # to just run the above in the first iteration
#             first_iter = False
#         else:
#             all_sequences.append(tup_dat[1])
#             for m in motifs:
#                 if m in tup_dat[1]:
#                     substrs.append(m)


def make_motifs(seqs):
    # generate motifs from shortest sequence
    motifs = generate_motifs(seqs)
    # filter out motifs that are same length as the sequence string itself
    max_nbr = len(max(motifs, key=len))
    motifs = list(filter(lambda x: len(x) < max_nbr, motifs))
    # filter out motifs that are too short based on DNA strings of 1 kbp
    motifs = list(filter(lambda x: len(x) > int(size_threshold*max_nbr), motifs))
    return motifs

def find_shared_motif(seqs):
    substrs = []
    for m in motifs:
        if m in seqs:
            # print(f'{m} in {seqs}')
            substrs.append(m)
    return substrs


if __name__ == '__main__':
    start = time.time()
    procs = os.cpu_count()
    print(f'processes: {procs}')
    chunksize = int(procs/2)
    print(f'chunksize: {chunksize}')
    print('='*50)
    print()
    motifs = make_motifs(file_content[0][1])
    # print(motifs)
    all_sequences = [x[1] for x in file_content[1:]]
    # print(all_sequences)
    with multiprocessing.Pool(processes=procs) as pool:
            substrs = pool.map(find_shared_motif, all_sequences, chunksize)

    # print ('Result:\n' + str(substrs[0]))
    substrs = substrs[0]
    # print(substrs)
    valid_substrs = [all(match_seq(sbsq, all_sequences)) for sbsq in substrs]
    # Make an iterator that filters elements from data returning only those that have a corresponding element in selectors that evaluates to True
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    substrs = list(compress(substrs, valid_substrs))
    # print(substrs)
    print(f'longest shared motif amongst {len(all_sequences)+1} different sequences\n')
    print(max(substrs, key=len))
    # print(valid_substrs)
    end = time.time()
    print()
    print(f'time elasped: {round(end - start,3)}')
