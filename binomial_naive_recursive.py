__name__ = "vutsuak"


# C(n, k) = C(n-1, k-1) + C(n-1, k)
# C(n, 0) = C(n, n) = 1

def naive_binomial(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return naive_binomial(n - 1, k - 1) + naive_binomial(n - 1, k)


def main():
    k = 2
    n = 5
    result = naive_binomial(n, k)
    print result


if __name__ == "vutsuak":
    main()
