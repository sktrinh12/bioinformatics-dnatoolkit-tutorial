def rabbit_pairs(months, offspring):
    """
    calculate the number of pairs of rabbits given the month (m) and the number of
    offspring conceived for each birth cycle. Another value
    for this variable is (k). Recursive way with memoisation
    """
    months = int(months)
    offspring = int(offspring)

    if months in cache:
        return cache[months]

    if months <= 2: # bc the pair of rabbits became adults, or just the pair of young rabbits
        value = 1
    else:
        first_gen = rabbit_pairs(months -1, offspring)
        sec_gen = rabbit_pairs(months -2, offspring)
        value = first_gen + (sec_gen * offspring)

    # cache the value
    cache[months] = value
    return value


def rabbit_pairs_rc(months, offspring):
    """
    slow recursive way to calculate the number of pairs of rabbits given the
    month (m) and the number of offspring conceived for each birth cycle,
    without memoisation; copied from website medium.com
    """
    months = int(months)
    offspring = int(offspring)

    if months == 1:
        return 1

    elif months == 2: # the output for the second months is incorrect?
        return offspring

    first_gen = rabbit_pairs_rc(months -1, offspring)
    sec_gen = rabbit_pairs_rc(months -2, offspring)

    if months <= 4:
        return (first_gen + sec_gen)

    return (first_gen + (sec_gen * offspring))


def rabbit_pairs_py(months, offspring):
    """
    more pythonic way to calculate the number of pairs of rabbits given the month
    (m) and the number of offspring conceived for each birth cycle
    """
    months = int(months)
    offspring = int(offspring)
    parent, child = 1, 1
    for itr in range(months -1):
        child, parent = parent, parent + (offspring * child)
    return child



if __name__ == "__main__":
    m = 4
    k = 3
    # with open('rosalind_fib.txt', 'r') as f:
    #     m,k = f.readline().split(' ')
    cache = {}
    # print(m)
    # print(k)
    print(f'with memo: {rabbit_pairs(m,k)}')
    print(f'without memo: {rabbit_pairs_rc(m,k)}')
    print(f'pythonic: {rabbit_pairs_py(m,k)}')

"""
o - small (children) rabbits. they have to mature and reproduce in the next cycle only
0 - mature (parents) rabbits. they can reproduce and move to the next cycle

for month = 5 and offspring = 2
===============================
Month 1: [o]
Month 2: [0]
Month 3: [0 o o]
Month 4: [0 o o 0 0]
Month 5: [0 o o 0 0 0 o o 0 o o]
Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]
"""
