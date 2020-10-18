from import_template import *

def mendel_simulation(k, m, n, verbose=False):
    from itertools import product

    # AA - homozygous dominant
    # m - Aa  heterozygous
    # n - aa  homozygous recessive

    k = int(k)
    m = int(m)
    n = int(n)
    population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)

    # all possibilities of offspring
    all_children = []
    for parent1 in population:
        # remove selected parent from population. Same as outcome without
        # replacement
        if verbose:
            print(f'first parent: {parent1}')
        chosen = population[:]
        chosen.remove(parent1)
        for parent2 in chosen:
            if verbose:
                print(f'remainigng parents: {parent2}')
            # get all possible children from 2 parents. Punnet square
            # arr1 = [1, 2, 3]
            # arr2 = [5, 6, 7]
            # [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]
            children = product(parent1, parent2)
            # join pairs of alleles
            all_children.extend([''.join(c) for c in children])

    if verbose:
        print(f'{all_children}\nlength: {len(all_children)}')
    # filters the list so that only pair of alleles have the dominant type
    dominants = filter(lambda c: 'A' in c, all_children)
    # divide the length of the dominants by the total length (120) to get the
    # probability; in the test case (2,2,2) -> # of dominants = 94
    # so 94/120 = 0.783333
    prob = float(len(list(dominants))) / len(all_children)
    return prob


def mendel_prob(k,m,n):
    k = int(k)
    m = int(m)
    n = int(n)
    # calculate the probability of recessive traits only
    # then take the difference to get the dominant traits
    total = k+m+n # total number of organisms
    # probabilities of each outcome without replace (thus the second selection
    # must have a minus 1)
    twoRecess = (n/total)*((n-1)/(total-1)) # probability of picking two recessive
    twoHetero = (m/total)*((m-1)/(total-1)) # probability of picking two heteros
    # probabilitm of picking one hetero and one recessive
    heteroRecess = (n/total)*(m/(total-1)) + (m/total)*(n/(total-1))

    # if you draw the punnett square, the probability of recessive alleles when
    # two heteros mate is: 1/4
    # likewise if a hetero and recessive mate; the probability of recessive
    # alleles is: 1/2
    # +---+----+----+
    # |   | A  | a  |
    # +---+----+----+
    # | A | AA | Aa |  --> 1/4
    # | a | Aa | aa |
    # +---+----+----+

    # +---+----+----+
    # |   | A  | a  |
    # +---+----+----+
    # | a | Aa | aa |  --> 1/2
    # | a | Aa | aa |
    # +---+----+----+
    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    return (1-recessProb) # take the complement


def mendl_prob_v2(k,m,n):
    """
    translated from F# from this blog post:
    https://nadrees.wordpress.com/2015/01/09/rosalind-in-f-mendels-first-law/
    """
    k = int(k)
    m = int(m)
    n = int(n)
    population = k + m + n
    # odds when we pick a dominate first
    # The probability that parent 1 is AA
    pK = k / population

    # according to the Punnett squares above, we know with what probability
    # each pair of parents will produce an offspring with a dominant allele.
    # Substituting those numbers as percentages we obtain the probabilities

    # odds when we pick a heterozygous first
    # The probability that parent 1 is Aa * the probability parent 2 is AA * 100%
    pMK = (m / population) * (k / (population - 1)) # due to no replacement
    # The probability that parent 1 is Aa * the probability parent 2 is Aa * 75%
    pMM = (m / population) * ((m - 1) / (population - 1)) * 0.75
    # The probability that parent 1 is Aa * the probability parent 2 is aa * 50%
    pMN = (m / population) * (n / (population - 1))*0.5

    # odds when we choose a recessive first
    # The probability that parent 1 is aa * the probability parent 2 is aA * 50%
    pNM = (n / population) * (m / (population - 1)) * 0.5
    # The probability that parent 1 is aa * the probability parent 2 is AA * 100%
    pNK = (n / population) * (k / (population - 1))

    result = pK + pMK + pMM + pMN + pNK + pNM
    return result



input_vaues = readTextFile('rosalind_iprb.txt')
k, m, n = input_vaues.split(' ')
print()
print(f'k={k}, m={m}, n={n}')

if k and m and n:
    res_1 = mendel_prob(k,m,n)
    res_2 = mendel_simulation(k,m,n)
    res_3 = mendl_prob_v2(k,m,n)
    print(res_1)
    print('='*20)
    print(res_2)
    print('='*20)
    print(res_3)
