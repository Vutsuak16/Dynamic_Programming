__name__ = "vutsuak"

# this is the bottoms up fibonacci approach
# this uses topological sort

memo = {}


def fibo(n):
    for k in range(1, n + 1):
        if k <= 2:
            memo[k] = k
        else:
            memo[k] = memo[k - 1] + memo[k - 2]

    return memo[n-1]


def main():
    n = input("enter n : the nth fibonacci you want to compute")
    fibonacci_number = fibo(int(n))
    print fibonacci_number


if __name__ == "vutsuak":
    main()
