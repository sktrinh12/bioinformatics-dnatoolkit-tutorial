from import_template import *
# from itertools import product
import numpy as np
# import multiprocessing
import time
import os
import random


# file_content = read_FASTA('find_spliced_motif.txt')
file_content = read_FASTA('rosalind_sseq.txt')

# def find_all_idx(seq, subseq, start, end):
#     """
#     returns sequence of matching indices
#     """
#     while True:
#         start = seq.find(subseq, start, end)
#         if start == -1: return
#         yield start
#         start += 1

print()
print('='*50)
for k,v in file_content.items():
    print(f'key: {k} : seq: {v}')

print()

keys = list(file_content.keys())
dna_str = file_content[keys[0]]
subseq = file_content[keys[1]]

# # the characters of t appear in the same order within s
# indices = []
# first = True
# avail_len = len(dna_str)
# sbsq_len = len(subseq)
# for i,sq in enumerate(subseq):
#     try:
#         # idx = dna_str.index(sq)
#         # if all(map(lambda x: idx > x, indices)):
#         end = avail_len - i
#         if end == sbsq_len:
#             break
#         idx = list(find_all_idx(dna_str, sq, i, end))
#         if i> 0:
#             min_ix = min(indices[i-1])
#             indices.append([ix+1 for ix in idx if ix+1 > min_ix])
#         else:
#             indices.append([ix+1 for ix in idx])

#     except Exception as e:
#         print(e)

# print(indices)
# # print(indices)
# print('='*50)

# # first_iter = True
# # subseq_idx = []
# # for idx in indices:
# #     if first_iter:
# #         subseq_idx.append(idx[0])
# #         first_iter = False
# #     else:
# #         current_idx = subseq_idx[-1]
# #         for ix in idx:
# #             if ix > current_idx:
# #                 subseq_idx.append(ix)
# #                 break


# # print()
# # print(subseq_idx)

def check_gt(list_tuples):
    """
    Numpy module provides a function diff() that calculate the n-th discrete difference along the given axis.
    We find the iterative difference of the list and check if it is less than 1. Idea is to have consecutively
    bigger numbers. Returns True or False
    """
    chk = np.diff(list_tuples)
    # print(chk)
    for d in chk:
        if d < 1:
            return False
    return True


# def product_(indices, iters = 1):
#     pools = map(tuple, indices)
#     result = [[]]
#     for i,pool in enumerate(pools):
#         result = [x+[y] for x in result for y in pool if all(y>xs for xs in x)]
#         print(f'{i} - {result}')

#     return list(result)

    # product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)

def find_motif(data, motif, position=-1):
    ix = []
    # position, indices = -1, ''
    for nucleotide in motif:
        position = data.find(nucleotide, position+1)
        # indices += str(position+1) + ' '
        ix.append(position+1)
    # print(indices)
    return ix

if __name__ == "__main__":
    start = time.time()
    # procs = os.cpu_count()
    # print(f'processes: {procs}')
    # chunksize = int(procs/4)
    # print(f'chunksize: {chunksize}')
    print('='*50)
    print()


    dct_motif_ix = {}
    dct_motif_ix[0] = find_motif(dna_str, subseq)
    # loop up to the index number + length of the subsequence that equals the
    # total length of the dna string; in practice it cycled to the beginning again;
    # so added the logic to check greater than between indices
    for ix in range(len(dna_str)-len(subseq)-1):
        m = find_motif(dna_str, subseq, ix)
        if check_gt(m):
            dct_motif_ix[ix] = m
        else:
            break

    for k,v in dct_motif_ix.items():
        print(f'{k} -> {v}')
        print()


    print('='*50)
    print()
    dct_len = len(dct_motif_ix.keys())
    rand_select = random.randint(0,dct_len-1)
    # print(rand_select)
    indices = dct_motif_ix[rand_select]
    print(' '.join([str(ix) for ix in indices]))

    # print(' '.join(list(map(lambda x: dna_str[x-1],ix))))

    # print(product_(indices))
    # with multiprocessing.Pool(processes=procs) as pool:
    #         valid_sbsq_idx = (tup_lst for tup_lst in pool.map(check_gt,
    #                                                           list(product_(indices)),
    #                                                           chunksize) if
    #                                                           tup_lst)

# valid_sbsq_idx = [perm for perm in list(product(*indices)) if check_gt(perm)]

    # for vs in valid_sbsq_idx:
    #     print(vs)
    # print(list(map(tuple, indices)))


    end = time.time()
    print()
    print(f'time elasped: {round(end - start,3)}')
