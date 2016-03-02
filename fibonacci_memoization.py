__name__ = "vutsuak"

# the naive recursive algorithm for calculating the nth fibonacci number takes exponential time
# by DP we can convert it into linear time
# this script involves memoization technique of dynamic programming

memo = {}


def fibo(n):
    f = 0
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fibo(n - 1) + fibo(n - 2)
    memo[n] = f
    return f


def main():
    n = input("enter n : the nth fibonacci you want to compute")
    fibonacci_number = fibo(int(n))
    print fibonacci_number


if __name__ == "vutsuak":
    main()
