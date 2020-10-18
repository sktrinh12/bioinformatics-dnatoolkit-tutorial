from import_template import *

# The integers correspond to the number of couples in a population
# possessing each genotype pairing for a given factor (gene or hereditary unit).
# there are six different couples with their genotype
# +---+-------+
# | 1 | AA-AA |
# | 2 | AA-Aa |
# | 3 | AA-aa |
# | 4 | Aa-Aa |
# | 5 | Aa-aa |
# | 6 | aa-aa |
# +---+-------+

# PUNNET SQUARE
# +---+----+----+
# |   | A  | A  |
# +---+----+----+
# | A | AA | AA |  --> 1 (100%)
# | A | AA | AA |
# +---+----+----+

# +---+----+----+
# |   | A  | A  |
# +---+----+----+
# | A | AA | AA |  --> 1 (100%)
# | a | Aa | Aa |
# +---+----+----+

# +---+----+----+
# |   | A  | A  |
# +---+----+----+
# | a | Aa | Aa |  --> 1 (100%)
# | a | Aa | Aa |
# +---+----+----+

# +---+----+----+
# |   | A  | a  |
# +---+----+----+
# | A | AA | Aa |  --> 1/4 (25%)
# | a | Aa | aa |
# +---+----+----+

# +---+----+----+
# |   | A  | a  |
# +---+----+----+
# | a | Aa | aa |  --> 1/2 (50%)
# | a | Aa | aa |
# +---+----+----+

# +---+----+----+
# |   | a  | a  |
# +---+----+----+
# | a | aa | aa |  --> 0 (0%)
# | a | aa | aa |
# +---+----+----+

# 6 pairings for given factor
genotypes_list = [
        'AA-AA',
        'AA-Aa',
        'AA-aa',
        'Aa-Aa',
        'Aa-aa',
        'aa-aa'
    ]

# probabilities for dominant trait for each of the 6 pairings
probabities = [1,1,1,0.75,0.5,0]

# zip into a dictionary
genotypes_prob = {g:p for g,p in zip(genotypes_list,probabities)}

# EXPECTED VALUE =
# number of offspring from AA-AA parents * 100% +
# number of offspring from AA-Aa parents * 100% +
# number of offspring from AA-aa parents * 100% +
# number of offspring from Aa-Aa parents * 75% +
# number of offspring from Aa-aa parents * 50% +
# number of offspring from aa-aa parents * 0%

# sample dataset given:
# counts = [1,0,0,1,0,1]

counts = [c for c in readTextFile('rosalind_iev.txt').split(' ')]
print(counts)

def calc_expt_offspring(counts):
    """
    calculate the expected value for the number of offspring that display the
    dominant phenotype in the next generation
    """
    # ensure the inputs are integers
    counts = list(map(int, counts))
    input_count_genotypes = {g:c for g,c in zip(genotypes_list, counts)}
    # multiple by 2 bc every couple has two offspring
    expected_val = sum([2*genotypes_prob[g]*c for g,c in
                    input_count_genotypes.items()])
    # print(expected_val)
    return int(expected_val)

print(calc_expt_offspring(counts))
