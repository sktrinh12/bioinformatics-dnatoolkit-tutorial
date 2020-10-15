def fibo(n):
    """
    use of memoisation and recursion
    """

    # if the cached value exists then return it
    if n in fibo_cache:
        return fibo_cache[n]

    # compute the nth term
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibo(n-1) + fibo(n-2)

    # cache the value otherwise
    fibo_cache[n] = value
    return value


# ANOTHER WAY USING PYTHON TOOLS

from functools import lru_cache

@lru_cache(maxsize = 1000) # how many to cache
def fibo_lru(n):
    # check n is a positive int
    assert type(n) == int, "n must be a positive integer"
    assert n >= 0, "n must a be positive integer"

    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo_lru(n-1) + fibo_lru(n-2)


def bottom_up_fib(n):
    """
    using the bottom up approach which is the fastest
    """
    if type(n) != int:
        n = int(n)
    if n ==1 or n == 2:
        return 1
    # instantiate the number of elements in sequence
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


if __name__ == "__main__":
    # fibo_cache = {}
    # for n in range(1,20):
    #     print(f'n={n} : {fibo(n)}')

    # print("="*50)
    # print()

    # for n in range(1,20):
    #     print(f'n={n} : {fibo_lru(n)}')

    # observe the golden ratio as it converges to 1.618...
    # for n in range(1,51):
    #     print(fibo(n+1) / fibo(n))

    with open('rosalind_fibo.txt') as f:
        n = f.readline()
    print(n)
    # print(fibo(int(n)))
    print(bottom_up_fib(n))
