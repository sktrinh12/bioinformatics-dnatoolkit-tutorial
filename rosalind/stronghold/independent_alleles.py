from itertools import product
from scipy.special import binom as binom_spec
from scipy.stats import binom
import re

# binom_spec - the number of combinations of N things taken k at a time

# bernoulli trial is a random experiment with 
# exactly two possible outcomes; i.e. flip of coin
# Closely related to a Bernoulli trial is a binomial 
# experiment, which consists of a fixed number 
# n of statistically independent Bernoulli trials,
# each with a probability of success p, and counts the 
# number of successes. A random variable corresponding 
# to a binomial is denoted by B(n,p), and is said to have
# a binomial distribution. The probability of exactly k 
# successes in the experiment B(n,p) is given by: 

# P(k) = (n choose k)(p**k)(q**(n-k))
# where p is probability offspring belongs to Aa Bb
# where q is probability offspring does not belong to 

# k-th generation of Tom's family tree (not counting Aa Bb
# mates at each level)
# mendels second law holds for the factors: traits are 
# inherited independently of each other


# Question: Two positive integers k (k ≤ 7) and N (N ≤ 2k)
# In this problem, we begin with Tom, who in the 0th 
# generation has genotype Aa Bb. Tom has two children 
# in the 1st generation, each of whom has two children,
# and so on. Each organism always mates with an organism
# having genotype Aa Bb.

# The probability that at least N Aa Bb organisms will 
# belong to the k-th generation of Tom's family tree 

# product(A, repeat=4) means the same as 
# product(A, A, A, A)
# crossing = list(product('Aa', 'Bb', repeat=2))
# print(crossing)
# print()
# crossing = [''.join(sorted(x, key=lambda x: x.lower())) for x in crossing]
# print(crossing)

# offspring_cnt = 0
# for ofspg in crossing:
#     # find all letters in any order using look ahead
#     if re.search(r'(?=.*A)(?=.*a)(?=.*B)(?=.*b)', ofspg):
#         offspring_cnt+=1

# print(offspring_cnt/len(crossing))


# compute the probability to observe n Aa Bb offspring after k 
# generations. This involves a succession of Bernoulli trials 
# until we reach the k-th generation,
# Pr(n,k) = (2**k choose n) (1/4)**n (1-1/4)**(2**k -n)
# n = 2k
# this is the pmf of a random variable that follows a Binomial distribution
# there are two children at each step) and p=1/4 (bc in two factor
# punnet square, the probability of any offspring of this subtype is 
# evenly the same for each crossing. For example, the subtype is aa, BB
# are both 1/4 (refer to punnet square)

# pmf = In probability and statistics, a probability mass
# function is a function that gives the probability that a 
# discrete random variable is exactly equal to some value

# PUNNET SQUARE with two factors
# +-----+--------+--------+--------+-------+
# |     |  AB    |  Ab    |  aB    |  ab   |
# +-----+--------+--------+--------+-------+
# | AB  | AA BB  | AA Bb  | Aa Bb  | Aa Bb |
# | Ab  | AA bB  | AA bb  | Aa bB  | Aa bb |
# | aB  | aA BB  | aA Bb  | aa BB  | aa Bb |
# | ab  | aA bB  | aA bb  | aa bB  | aa bb |
# +-----+--------+--------+--------+-------+

def binom_prob_allele(k, N):
    def p(n,k):
        return binom_spec(2**k, n) * 0.25**n * 0.75**(2**k - n)
    return 1 - sum(p(n,k) for n in range(N))

def binom_pmf(k, N, p):
    return 1 - sum(binom.pmf(k_, 2**k, p) for k_ in range(N))

# k = 2
# N = 1
p = 1/4

# print(binom_spec(2**k,k) * 0.25**k * 0.75**(2**k - k))
# binom.pmf(k, n, p)
# print(binom.pmf(k, 2**k,1/4))

# print(round(binom_prob_allele(k, N),3))
# print()
# print(round(binom_pmf(k, N, p),3))

with open('rosalind_lia.txt', 'r') as f:
    k, N = map(int, f.readline().split())


print(round(binom_prob_allele(k, N),3))
