__name__ = "vutsuak"


def matrix_chain_order(p, n):  # p is the chain order matrix and n is the length
    m = [[0 for i in range(n)] for j in range(n)]
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+L-1
            

