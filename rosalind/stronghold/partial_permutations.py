import sys

if __name__ == "__main__":
    p_perm = 1
    if len(sys.argv) < 2:
        n = 21
        k = 7
    if len(sys.argv) == 3:
        try:
            n = int(sys.argv[1])
            k = int(sys.argv[2])
        except Exception as e:
            print("must have two integer arguments (n) and (k)")
            sys.exit()
    elif len(sys.argv) > 2:
        print("must have two arguments (n) and (k)")
        sys.exit()

    for i in range(k):
        p_perm *= (n - i)
        p_perm %= 10**6

    print(p_perm)
