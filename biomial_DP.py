__name__ = "vutsuak"


# C(n, k) = C(n-1, k-1) + C(n-1, k)
# C(n, 0) = C(n, n) = 1
# here there are two parameters so we need 2 loops
# we can use dictionary of lists but 2D array would be simpler

def bottomsUp_binomial(n, k):
    memo = [[0 for i in range(k+1)] for j in  range(n+1)]  # a way to create 2D array in python we need to initialize outer list
    for i in range(0, n + 1):
        for j in range(0, min(i, k) + 1):
            if i == j or j == 0:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j] + memo[i - 1][j - 1]
    return memo[n][k]


def main():
    k = 1
    n = 5
    result = bottomsUp_binomial(n, k)
    print result


if __name__ == "vutsuak":
    main()
