### Rearrangements Power Large-Scale Genomic Changes
import sys
from time import sleep

"""
Point mutations can create changes in populations of organisms from the same species, but they lack the power to create and differentiate entire species. This more arduous work is left to larger mutations called genome rearrangements, which move around huge blocks of DNA. Rearrangements cause major genomic change, and most rearrangements are fatal or seriously damaging to the mutated cell and its descendants (many cancers derive from rearrangements). For this reason, rearrangements that come to influence the genome of an entire species are very rare.

Because rearrangements that affect species evolution occur infrequently, two closely related species will have very similar genomes. Thus, to simplify comparison of two such genomes, researchers first identify similar intervals of DNA from the species, called synteny blocks; over time, rearrangements have created these synteny blocks and heaved them around across the two genomes (often separating blocks onto different chromosomes, see Figure 1.).

A pair of synteny blocks from two different species are not strictly identical (they are separated by the action of point mutations or very small rearrangements), but for the sake of studying large-scale rearrangements, we consider them to be equivalent. As a result, we can label each synteny block with a positive integer; when comparing two species' genomes/chromosomes, we then only need to specify the order of its numbered synteny blocks.
"""

### PROBLEM
"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).


3
-----
6
1 2 3
1 3 2
3 1 2
3 2 1
2 3 1
2 1 3

"""
# def transpose(nbr, inv, x, y):
#     # Transpose x and y in permutation nbr while maintaining inv as nbr's
#     # inverse.
#     i, j = inv[x], inv[y]
#     inv[x], inv[y] = j, i
#     nbr[i], nbr[j] = nbr[j], nbr[i]

# def permute(number: int) -> int:
#     # pad on both sides to allow for a natural stop
#     nbr = [number + 1] + list(range(1, number+1)) + [number + 1]
#     print(nbr)
#     inv = nbr[:]
#     print(inv)
#     # keep track of directions, all starting negative (move left)
#     d = [-1] * (number + 2)
#     # print(d)
#     x = number # x is the active element
#     # print(x)
#     yield nbr[1:-1]
#     check_nbr = x>0
#     print("="*25)
#     while check_nbr:
#         y = nbr[inv[x] + d[x]] # y is the element next to the x in direction d[x]
#         if x < y:
#             d[x] = -d[x] # switch direction
#             x -= 1 # change active elemtn to x-1
#         else:
#             transpose(nbr, inv, x, y)
#             yield nbr[1:-1] # new permutation is generated (indexing on second up to n-1)
#             x = nbr # change active element to nbr
#             print(x)

            # check_nbr = False


# def main():
#     num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
#     perm_ls = [p for p in permute(num)]
#     print(len(perm_ls))
#     print('\n'.join(' '.join(str(x) for x in p) for p in perm_ls))

##################################################


def nobody():
    while True:
        yield False


# The term "troll" is taken from Knuth's choice of word
def sjt(nbr, inv, i, trolls):
    """
    Steinhaus–Johnson–Trotter algorithm
    The sequence of permutations for a given number n can be formed from the
    sequence of permutations for n − 1 by placing the number n into each possible
    position in each of the shorter permutations. When the permutation on n − 1
    items is an even permutation (as is true for the first, third, etc.,
                                  permutations in the sequence) then the number n is
    placed in all possible positions in descending order, from n down to 1; when the
    permutation on n − 1 items is odd, the number n is placed in all the possible
    positions in ascending order
    """
    d = -1  # Directoin. -1 is descending, +1 is ascending.
    while True:
        j = inv[i]  # j is the position of the current "troll"
        if nbr[j] < nbr[j + d]:
            d = -d
            yield next(trolls[i - 1])
        else:
            nbr[j], nbr[j + d] = nbr[j + d], nbr[j]
            inv[i] += d
            inv[nbr[j]] -= d
            yield True


def setup(n):
    # Pad nbr with n + 2, so that nbr[i] will always be < the two ends.
    nbr = [n + 2] + [i for i in range(1, n + 1)] + [n + 2]
    inv = nbr[:-1]
    # nobody simply continuously yields False. By adding a "nobody" generator
    # at both ends of trolls, False is autmatically yieded by sjt when needed.
    trolls = [nobody()]
    trolls.extend(sjt(nbr, inv, i + 1, trolls) for i in range(n))
    trolls += [nobody()]
    # The lead troll will be the item n in the permutation
    lead_troll = trolls[-2]
    return nbr, lead_troll


def permutations(n):
    nbr, lead_troll = setup(n)
    yield nbr[1:-1]
    while next(lead_troll):
        yield nbr[1:-1]


# def cyclic_test(n):
#     nbr, lead_troll = setup(n)
#     c = 0
#     while True:
#         print('Output: ', ''.join(str(x) for x in nbr[1:-1]))
#         c += 1
#         if not next(lead_troll):
#             print('-------')
#             print(c)
#             print('-------')
#             sleep(1)
#             c = 0

## ALTERNATIVE METHOD USING RECURSION
def permute2(l):
    return [ (m[:i] + [l[0]] + m[i:]) for m in permute2(l[1:]) for i in range(len(m)+1) ] if len(l) >1 else [l]

# p = permute2(range(1, n+1))
# print(len(p))
# for l in p:
#     prin(' '.join(map(str,l)))

if __name__ == '__main__':
    num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    perm_ls = [p for p in permutations(num)]
    # print(len(perm_ls))
    # print('\n'.join(' '.join(str(x) for x in nbr) for nbr in perm_ls))
    # cyclic_test(3)
    with open('enum_gene_output.txt', 'w') as f:
        f.write(f"{len(perm_ls)}\n")
        for nbr in perm_ls:
            # print(join_nbr)
            join_nbrs = ""
            for i,x in enumerate(nbr):
                join_nbrs += f"{x} "
                if i == num-1:
                    join_nbrs = join_nbrs.rstrip()
                    join_nbrs += "\n"
                    f.write(join_nbrs)
                    # print(join_nbrs)
